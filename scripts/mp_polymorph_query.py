#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S-C1 MP形成能交叉核验: 查询 MP API 各关键系多形体 formation_energy_per_atom + spacegroup
在 3090 (有代理) 上运行; 输出 JSON 落盘
"""
import urllib.request, os, json, urllib.parse, time, sys

KEY = os.environ['MP_API_KEY'].strip()
proxy = urllib.request.ProxyHandler({'https': 'http://127.0.0.1:7890', 'http': 'http://127.0.0.1:7890'})
opener = urllib.request.build_opener(proxy)

def mp_get(path, **params):
    q = '&'.join(f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items())
    url = f"https://api.materialsproject.org{path}?{q}" if q else f"https://api.materialsproject.org{path}"
    req = urllib.request.Request(url, headers={'X-API-KEY': KEY, 'Accept': 'application/json', 'User-Agent': 'Mozilla/5.0'})
    try:
        r = opener.open(req, timeout=40)
        return json.loads(r.read().decode())
    except Exception as e:
        return {"error": repr(e)[:300]}

def query_formula(formula, limit=60):
    d = mp_get('/materials/thermo/', formula=formula, _all_fields='true', _limit=limit)
    out = []
    if 'error' in d:
        return {"formula": formula, "error": d['error']}
    for doc in d.get('data', []):
        sym = doc.get('symmetry', {}) or {}
        out.append({
            "material_id": doc.get('material_id'),
            "formula_pretty": doc.get('formula_pretty'),
            "spg": sym.get('symbol'),
            "spg_number": sym.get('number'),
            "formation_energy_per_atom": doc.get('formation_energy_per_atom'),
            "energy_above_hull": doc.get('energy_above_hull'),
            "is_stable": doc.get('is_stable'),
            "thermo_type": doc.get('thermo_type'),
        })
    return {"formula": formula, "entries": out}

if __name__ == '__main__':
    formulas = sys.argv[1:]
    results = {}
    for f in formulas:
        print(f"querying {f} ...", flush=True)
        results[f] = query_formula(f)
        time.sleep(0.3)
    outfile = "/tmp/mp_results.json"
    json.dump(results, open(outfile, 'w'), ensure_ascii=False, indent=1)
    print("saved to", outfile)
    # summary
    for f in formulas:
        r = results[f]
        if 'error' in r:
            print(f"  {f}: ERROR {r['error']}")
            continue
        entries = sorted(r['entries'], key=lambda x: x['formation_energy_per_atom'] or 0)
        print(f"\n  {f}: {len(entries)} MP entries (r2SCAN), sorted by Ef:")
        for e in entries[:12]:
            print(f"    {e['material_id']:12s} {str(e['spg']):12s} Ef={e['formation_energy_per_atom']:.5f} hull={e['energy_above_hull']:+.4f} stable={e['is_stable']}")
