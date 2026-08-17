#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S-C1 发布阻断·异常剔除与重排序 v0.1
任务: 第六枪落盘 10 条小正值异常(c44_d<1.0) 发布前处置。
处置规则(文献常识交叉, 非 JARVIS 内部数据):
  - 5 条高置信坏值 -> flag="坏值剔除" (金刚石 C / 尖晶石 Al2Mg1O4 / BeF2 / 冰 H2O / Sc2O3)
  - 5 条审查候选     -> flag="异常审查候选" (NaHO / CoO2 / Zn2P3S9 / CoLiS2 / KCO2), 保留不剔除
纪律: 不物理删除原文件, 保留全部 546 条(flag 标记), 新版本另存。
产物:
  - SPTF联合排序_v1.0_D口径_v0.2.json        (546 条全保留 + 新 flag)
  - SPTF剪切软模候选_56_v0.3.json            (剔除 H2O 坏值, NaHO 标记降级, 按 ds_max 重排)
"""
import json

D1_IN = "/home/vortex/涡肉身壳/papers/SPTF联合排序_v1.0_D口径_v0.1.json"
D2_IN = "/home/vortex/涡肉身壳/papers/SPTF剪切软模候选_56_v0.2.json"
D1_OUT = "/home/vortex/涡肉身壳/papers/SPTF联合排序_v1.0_D口径_v0.2.json"
D2_OUT = "/home/vortex/涡肉身壳/papers/SPTF剪切软模候选_56_v0.3.json"

# formula (以清单内原生字符串为准) -> 处置
# 高置信坏值(文献常识交叉: 金刚石 C44~500/尖晶石~180/BeF2 结构错误/冰固态介质语义/刚玉结构应硬)
BAD = {
    "C1": "坏值剔除",          # 金刚石 JVASP-25403 c44_d=0.1, 真值~500 GPa
    "Al2 Mg1 O4": "坏值剔除",  # 尖晶石 JVASP-95531 c44_d=0.00, 硬陶瓷
    "Be1 F2": "坏值剔除",      # JVASP-95484 c44_d=0.00
    "H2 O1": "坏值剔除",       # 冰 JVASP-135041 c44_d=0.7 (低置信剔除)
    "O3 Sc2": "坏值剔除",      # Sc2O3 JVASP-50097 c44_d=0.5 (中置信剔除)
}
# 审查候选(可能真实软材料, 层状/离子化合物; 保留但不计软模)
REVIEW = {
    "H1 Na1 O1": "异常审查候选",  # NaOH 层状氢氧化物
    "Co1 O2": "异常审查候选",      # CoO2 层状
    "P3 S9 Zn2": "异常审查候选",   # Zn2P3S9 单斜
    "Co1 Li1 S2": "异常审查候选",  # LiCoS2 层状 R3m
    "C1 K1 O2": "异常审查候选",    # KCO2
}

def main():
    d1 = json.load(open(D1_IN))
    d2 = json.load(open(D2_IN))
    print(f"加载: D1 {len(d1)} 条 | D2 {len(d2)} 条")

    # ---------- 文件1: 546 条全保留, flag 标记 ----------
    bad_hit, rev_hit = [], []
    for r in d1:
        f = r["formula"]
        if f in BAD:
            r["flag"] = BAD[f]
            bad_hit.append(f)
        elif f in REVIEW:
            r["flag"] = REVIEW[f]
            rev_hit.append(f)
    # 防御: 清单内没有的判定条目报出(不硬填)
    for f in BAD:
        if f not in bad_hit:
            print(f"  [警告] 坏值判定条目未命中: {f}")
    for f in REVIEW:
        if f not in rev_hit:
            print(f"  [警告] 审查判定条目未命中: {f}")

    # 软模候选统计 (c44_d<=22.7 且 c44_d>=0)
    def soft_stats(records, exclude_bad=False):
        tot = 0
        soft = 0
        for r in records:
            v = r.get("c44_d")
            if v is None:
                continue
            if exclude_bad and r.get("flag") == "坏值剔除":
                continue
            tot += 1
            if v <= 22.7 and v >= 0:
                soft += 1
        return soft, tot

    s_all, t_all = soft_stats(d1)
    s_nobad, t_nobad = soft_stats(d1, exclude_bad=True)
    # 全10条剔除版(参考口径): 从 tot 剔除所有 <1.0 异常
    tot_noall = sum(1 for r in d1 if r.get("c44_d") is not None and r["c44_d"] >= 1.0)
    soft_noall = sum(1 for r in d1 if r.get("c44_d") is not None and 1.0 <= r["c44_d"] <= 22.7)

    print(f"\n[文件1] 软模候选统计:")
    print(f"  剔除前(全量):   {s_all}/{t_all} ({s_all/t_all*100:.1f}%)")
    print(f"  剔除5高置信后:  {s_nobad}/{t_nobad} ({s_nobad/t_nobad*100:.1f}%)")
    print(f"  全部10条剔除后: {soft_noall}/{tot_noall} ({soft_noall/tot_noall*100:.1f}%)   [参考口径]")
    print(f"  flag 分配: 坏值剔除 {len(bad_hit)} 条 | 异常审查候选 {len(rev_hit)} 条")
    print(f"  保留总条数: {len(d1)} (不物理删除)")

    json.dump(d1, open(D1_OUT, "w"), ensure_ascii=False, indent=1)
    print("落盘:", D1_OUT)

    # ---------- 文件2: 56 共振候选 v0.3 ----------
    # 处置: H2O(坏值) 剔除; NaHO(审查候选) 保留并标记降级; 其余 OK
    # 记录移除清单
    removed = []
    kept = []
    for r in d2:
        f = r["formula"]
        if f in BAD:                       # H2 O1
            removed.append(dict(r, flag="坏值剔除"))
            continue
        if f in REVIEW:                    # H1 Na1 O1
            r2 = dict(r, flag="异常审查候选")
            kept.append(r2)
            continue
        r2 = dict(r, flag="OK")
        kept.append(r2)
    # 重排序: 按 ds_max 降序 (v0.9/v0.2 沿用排序键)
    kept.sort(key=lambda x: x["ds_max"], reverse=True)

    print(f"\n[文件2] 56共振候选 v0.3:")
    print(f"  原 v0.2 条数: {len(d2)}")
    print(f"  剔除(坏值): {len(removed)} 条 -> {[r['formula'] for r in removed]}")
    print(f"  保留: {len(kept)} 条 (含审查标记 {sum(1 for r in kept if r['flag']=='异常审查候选')})")
    print(f"  排序键: ds_max 降序, 已重排: {all(kept[i]['ds_max']>=kept[i+1]['ds_max'] for i in range(len(kept)-1))}")

    json.dump(kept, open(D2_OUT, "w"), ensure_ascii=False, indent=1)
    print("落盘:", D2_OUT)

    # ---------- 汇总摘要(供报告) ----------
    print("\n=== 异常处置汇总 ===")
    for r in d1:
        if r.get("flag") in ("坏值剔除", "异常审查候选"):
            print(f"  {r['formula']:14s} c44_d={r['c44_d']:<5} {r['d_jid']} {r['d_spg']:<8} -> {r['flag']}")

if __name__ == "__main__":
    main()
