# DRAM High-k Field-Theoretic Criterion — Reproduction Package

Field-theoretic criterion for DRAM high-k dielectrics: a two-dimensional criterion space (soft-mode × bandgap) and quantitative doping-pinning.

Preprint v2.1: CN DOI 10.5281/zenodo.21990524 (concept 10.5281/zenodo.21972969) | EN DOI 10.5281/zenodo.21990528 (concept 10.5281/zenodo.21972972)

## Contents

- `scripts/S-C1核心数字复现_v1.0.py` — reproduces the three core result groups of the paper (calibration curve R²=0.9998 / soft-mode hit validation / 2D criterion space)
- `scripts/S-C1第六枪_口径D重算_v0.1.py` — criterion-D global recomputation (546-compound list, window-sensitivity scan, anomaly list)
- `scripts/S-C1发布阻断_异常剔除与重排序_v0.1.py` — anomaly triage (5 bad-value removal + 5 audit-candidate flags) and re-ranking
- `data/SPTF联合排序_v1.0_D口径_v0.2.json` — criterion-D joint ranking, 546 compounds (c44_old/c44_d/d_jid/d_spg/flag)
- `data/SPTF剪切软模候选_56_v0.3.json` — 54 soft-mode resonance candidates, ds_max descending
- `S-C1_DRAM高k场域判据_Zenodo发布版_v1.0_CN.md` / `_EN.md` — preprint sources (v2.1: five-dimensional unified storage-medium criterion, retention-spectrum extension)
- `pdf/` — v2.1 preprint PDFs (CN 6 pp / EN 7 pp)

## Requirements

Python 3, numpy. No GPU needed.

## Run

```bash
python3 scripts/S-C1核心数字复现_v1.0.py         # core numbers (calibration/hit/2D space)
python3 scripts/S-C1第六枪_口径D重算_v0.1.py      # criterion-D recomputation (needs JARVIS local mirror)
python3 scripts/S-C1发布阻断_异常剔除与重排序_v0.1.py  # anomaly triage + re-ranking
```

Note: `S-C1第六枪_口径D重算_v0.1.py` reads the JARVIS-DFT local mirror (elastic tensor database). The released `data/` files are the computed outputs, so the core-number script runs standalone.

## Caliber note

C44 values in the paper's §3.1 use the industry-comparison caliber (c44_old, industry dielectric phase). Under criterion D (energy window, softest metastable phase), SiO₂ metastable (P4₂/mmc) C44=2.4 is an independent 0K-instability signal of a metastable phase (same class as the ZrO₂ tetragonal metastable), not changing the "quartz SiO₂ as a stable dielectric" industry comparison.

## Author

Chao Qin | ORCID 0009-0006-2000-5644 | Juexiao Information Consulting Center, Xingyi, Guizhou, China
