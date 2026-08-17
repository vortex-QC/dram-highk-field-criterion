#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S-C1 第六枪·口径D全局重算与敏感性扫描 v0.1
第五枪修复落盘方案执行:
  ①546 组分按口径D(能量窗口内非负min-C44)重算 → 新清单落盘
  ②窗口敏感性扫描 ΔE∈{0.05,0.10,0.20,0.30}
  ③小正值异常清单(<1 GPa)
  ④56 共振候选 v2(-ZnTiO₃)
纪律: 机器验算; 数据缺失标记不硬填; 源条目 jid/spg 全记录。
"""
import json, re
from collections import defaultdict

JAR = "/home/vortex/涡肉身壳/field_reasoner/harmonic_db/jarvis_dft_3d.json"
LST = "/home/vortex/涡肉身壳/papers/SPTF跨通道联合排序_v1.0.json"
RES = "/home/vortex/涡肉身壳/papers/SPTF剪切软模候选_56_v0.9.json"
OUT = "/home/vortex/涡肉身壳/papers/SPTF联合排序_v1.0_D口径_v0.1.json"
OUT_RES = "/home/vortex/涡肉身壳/papers/SPTF剪切软模候选_56_v0.2.json"

def parse_comp(f):
    toks = re.findall(r'([A-Z][a-z]?)(\d*)', f)
    d = defaultdict(int)
    for el, n in toks:
        d[el] += int(n) if n else 1
    return tuple(sorted(d.items()))

def parse_vortex(f):
    toks = re.findall(r'([A-Za-z]+)\s*(\d*)', f)
    d = defaultdict(int)
    for el, n in toks:
        d[el] += int(n) if n else 1
    return tuple(sorted(d.items()))

print("加载 JARVIS...")
jar = json.load(open(JAR))
index = defaultdict(list)
for x in jar:
    et = x.get('elastic_tensor')
    if not et or len(et) < 6:
        continue
    mn = min(et[3][3], et[4][4], et[5][5])
    index[parse_comp(x['formula'])].append(
        dict(ef=x['formation_energy_peratom'], c44=mn, jid=x['jid'],
             spg=x.get('spg_symbol', '')))

def window_min(entries, de):
    ef_min = min(e['ef'] for e in entries)
    cand = [e for e in entries if e['ef'] <= ef_min + de and e['c44'] >= 0]
    return min(cand, key=lambda e: e['c44']) if cand else None

def main():
    lst = json.load(open(LST))
    rows = []
    missing, small_pos = [], []
    for x in lst:
        if x.get('c44') is None:
            continue
        key = parse_vortex(x['formula'])
        entries = index.get(key, [])
        if not entries:
            continue
        w = window_min(entries, 0.10)
        row = dict(formula=x['formula'], c44_old=x['c44'], ds_max=x.get('ds_max'),
                   n_phases=x.get('n_phases'))
        if w is None:
            row['c44_d'] = None
            row['flag'] = '数据缺失(窗口内无有效弹性)'
            missing.append(x['formula'])
        else:
            row['c44_d'] = round(w['c44'], 2)
            row['d_jid'] = w['jid']
            row['d_spg'] = w['spg']
            row['flag'] = 'OK'
            if 0 <= w['c44'] < 1.0:
                small_pos.append((x['formula'], w['c44'], w['spg'], w['jid']))
        rows.append(row)
    print(f"口径D 重算: {len(rows)} 组分 | 数据缺失 {len(missing)} | 小正值异常 {len(small_pos)}")
    json.dump(rows, open(OUT, 'w'), ensure_ascii=False, indent=1)
    print("落盘:", OUT)

    # ② 窗口敏感性扫描
    print("\n窗口敏感性（软模= c44_d<=22.7）:")
    lst2 = [x for x in lst if x.get('c44') is not None]
    for de in [0.05, 0.10, 0.20, 0.30]:
        n_soft, n_ok = 0, 0
        for x in lst2:
            key = parse_vortex(x['formula'])
            entries = index.get(key, [])
            if not entries: continue
            w = window_min(entries, de)
            if w is None: continue
            n_ok += 1
            if w['c44'] <= 22.7: n_soft += 1
        print(f"  ΔE={de:.2f}eV: 软模 {n_soft}/{n_ok} ({n_soft/n_ok*100:.1f}%)")
    # 关键系窗口稳定性
    print("\n关键系窗口稳定性:")
    for f in ['O2 Zr1','Hf1 O2','O2 Ti1','Al2 O3','Hf1 O4 Zr1']:
        key = parse_vortex(f)
        entries = index.get(key, [])
        vals = []
        for de in [0.05, 0.10, 0.20, 0.30]:
            w = window_min(entries, de)
            vals.append(f"{w['c44']:.1f}({w['spg']})" if w else "缺失")
        print(f"  {f:10s} " + " | ".join(vals))

    # ③ 小正值异常清单
    if small_pos:
        print("\n小正值异常清单(<1 GPa, 人工审查候选):")
        for f, c, spg, jid in small_pos:
            print(f"  {f:16s} {c:5.2f} ({spg}, {jid})")

    # ④ 56 共振候选 v2
    res = json.load(open(RES))
    out_res = []
    for r in res:
        key = parse_vortex(r['formula'])
        entries = index.get(key, [])
        w = window_min(entries, 0.10)
        if w is not None and w['c44'] <= 22.7:
            r2 = dict(r)
            r2['c44_d'] = round(w['c44'], 2)
            r2['d_jid'] = w['jid']
            r2['d_spg'] = w['spg']
            out_res.append(r2)
    print(f"\n56共振候选 v2: {len(out_res)}/56 保持（剔除 {56-len(out_res)}）")
    json.dump(out_res, open(OUT_RES, 'w'), ensure_ascii=False, indent=1)
    print("落盘:", OUT_RES)

if __name__ == "__main__":
    main()
