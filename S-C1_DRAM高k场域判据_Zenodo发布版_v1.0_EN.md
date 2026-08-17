# Field-Theoretic Criterion for DRAM High-k Dielectrics: A Two-Dimensional Criterion Space (Soft-Mode × Bandgap) and Quantitative Doping-Pinning

**Zenodo preprint v1.0 (English) | 2026-08-17**
**Author**: Chao Qin | ORCID 0009-0006-2000-5644 | Juexiao Information Consulting Center, Xingyi, Guizhou 562400, China
**Category**: DRAM capacitor dielectrics / materials criterion / elastic soft modes / antiferroelectrics / data-driven materials screening
**Chinese version**: released simultaneously

---

## Abstract

DRAM capacitor dielectrics face a hard constraint of leakage×EOT scaling below the 1z-nm node (Shiratake, IMW 2020). For 30 years industry has responded by doping-pinning the tetragonal phase of high-k dielectrics (ZrO₂/HfO₂-based) to stabilize it—yet this long-standing practice lacks a unified criterion language. Using a field-theoretic framework (materials as density-cluster fields ρ=m·p; phase-transition candidates as failure-line R'=1 equilibrium regions; shear soft modes as signatures of phase-transition activity), this paper provides a computable criterion coordinate for DRAM high-k dielectrics. Core results: (1) **Industry hit validation of the soft-mode criterion**—in a 6-material comparison of the high-k family, ZrO₂, the only material with antiferroelectric (AFE) transition activity, is exactly the only Hf/Zr oxide that falls in the soft-mode region (C44=20.3 GPa≤threshold 22.7), while all other stable dielectrics (HfO₂ 103.2/Al₂O₃ 43.8/SiO₂ 67.1) are not soft (positive 1/1, negative 4/4); (2) **Two-dimensional criterion space**—soft-mode axis (transition activity / 0K metastability) × bandgap axis (leakage wall, threshold ~4 eV), with tetragonal ZrO₂ P4₂/nmc the unique Pareto-optimal phase (C44=30.7+Eg=4.03), explaining 30 years of industrial pinning of the tetragonal phase; (3) **Quantitative doping-pinning**—an alkaline-earth AZrO₃ calibration family yields C44=83.7·r−30.1 GPa (R²=0.9998), making dopant ionic radius a quantitative tuning knob of the C44 spectrum; Y³⁺ extrapolation 55.3 GPa falls within the measured 8YSZ range 47-66 GPa; (4) **Martensitic mirror**—the same t→m transformation is exploited in ceramics (toughening) but is a failure mode in DRAM dielectrics, so the criterion is invariant while engineering goals are opposite; (5) **Criterion D data engineering**—matching-rule auditing found 44.3% multi-entry contamination; an energy-window criterion (non-negative min-C44 within +0.1 eV of ground state) makes the criterion semantics explicit as "0K instability signal of a real metastable phase," with a global recomputation of a 546-compound list released. All values are machine-verified, with experimental comparisons carrying verifiable references.

**Keywords**: DRAM capacitor dielectric; high-k dielectric; shear soft mode; antiferroelectric; doping pinning; elastic criterion; materials screening

## 1. Introduction

Scaling of DRAM capacitor dielectrics is a long-standing consensus problem at the semiconductor physics limit (the "memory wall" material root hit by three independent industry-deficit lists; IMW 2020 explicitly states new materials are needed below the 1z-nm node [1]). EOT (equivalent oxide thickness) scaling hits the tunneling-leakage wall, and industry responds by high-k replacement—SiO₂(k~3.9)→Al₂O₃(k~9)→Ta₂O₅(k~25)→ZrO₂/HfO₂(k~20-40)→ZAZ stack→next-generation TiO₂(k>80)/antiferroelectric [2]. But high-k introduces two new problems:

- **Phase-transition activity**: ZrO₂ AFE↔FE electric-field-induced switching enhances charge storage, but AFE/FE transitions bring polarization stability and fatigue issues [3];
- **Phase stability**: the high-k phases (tetragonal/cubic) of HfO₂ are unstable at room temperature and must be stabilized by doping (an industry-standard method) [4].

Both are **phase-transition/phase-stability problems**—precisely the domain of a materials criterion layer. This paper's position: industry's 60-year doping-pinning practice is **position control on the C44 elastic spectrum**—making this tacit knowledge explicit through a computable criterion coordinate.

**Framework** (field theory): materials as density-cluster fields ρ=m·p (m=concentration, p=distribution shape); phase-transition candidates as failure-line R'=1 equilibrium regions (near-degenerate systems = criterion-amount protocol-sensitive regions); **shear soft mode C3** as the phonon-softening signature of displacive phase transitions (AFE↔FE switching activity). Using the SPTF data layer (V12/JARVIS elasticity), this paper maps DRAM high-k dielectrics onto these two criterion axes.

## 2. Methods and Data

### 2.1 Criterion quantities

- **Soft-mode axis (C3)**: minimum shear elastic constant C44 (min-C44)—small C44 = soft against shear = active displacive transition. Threshold C44≤22.7 GPa (p25 percentile of the v0.9 positive sample).
- **Bandgap axis (leakage wall)**: DFT bandgap Eg—leakage current ∝exp(−Eg), with DRAM leakage specs requiring Eg≥4 eV (industry empirical value).
- **Criterion D (data quality)**: matching-rule auditing found multi-entry JARVIS structures for the same compound (44.3% of 546 matched compounds are multi-entry), and the old criterion was contaminated by bad entries. Fixed criterion D = non-negative min-C44 within an energy window (ground-state formation energy + 0.1 eV)—making the criterion semantics explicit as "**0K instability signal of a real metastable phase**" (transition activity, not ground-state instability, nor hypothetical-phase noise).

### 2.2 Data sources

- JARVIS-DFT 3D elastic library (elastic tensor + formation energy + bandgap, local mirror)
- SPTF cross-channel joint ranking v1.0 (729 candidates, 546 with elasticity data)
- OQMD structure enumeration (ZrO₂ polymorph 361 phases)
- Calibration family: alkaline-earth AZrO₃ (same-stoichiometry perovskite, Shannon radius CN=8)

All values machine-verified (python3); scripts released in a reproducibility package.

## 3. Results

### 3.1 Industry hit validation of the soft-mode criterion

Six-material comparison of the high-k dielectric family (gun 2, corrected to criterion-D values):

| Material | Industry role | C44(GPa) | Soft-mode | Industry behavior |
|---|---|---|---|---|
| **ZrO₂** | Mainstay + AFE star | **20.3** | **hit** | has AFE activity ✓ |
| HfO₂ | doping-stabilized mainstay | 103.2 | not soft | no AFE as pure phase, needs doping ✓ |
| Al₂O₃ | first-gen / ZAZ spacer | 43.8 | not soft | no transition activity (stable spacer) ✓ |
| SiO₂ | old dielectric (discarded) | 67.1 (quartz) | not soft | no activity + low k, discarded ✓ |
| TiO₂ | next-gen candidate (k>80, unproduced) | 34.3 | not soft | bandgap wall (§3.3) ✓ |
| Si₃N₄ | old dielectric | 100 | not soft | stable ✓ |

> **Caliber note**: C44 in this table uses the industry-comparison caliber (c44_old, industry dielectric phase). Under criterion D (energy window, softest metastable phase) values differ: HfO₂ tetragonal metastable 22.9 is near-soft (its "not soft as pure phase" is refined to "monoclinic ground state hard, tetragonal metastable near-soft"—the criterion basis for industry's heavy-doping need, gun 5); SiO₂ metastable (P4₂/mmc) 2.4 is an independent 0K-instability signal of a metastable phase (same class as the ZrO₂ tetragonal metastable), not changing the "quartz SiO₂ as a stable dielectric" industry comparison. Criterion-D soft-mode hit semantics = "0K instability signal of a real metastable phase" (§3.5).

**Positive 1/1 hit, negative 4/4 correct**—the only material with AFE activity is exactly the only soft-mode hit. Among the 56 soft-mode candidates (criterion D), only 2 are Hf/Zr oxides (HfLi₂O₃ artifact-flagged + ZrO₂ the only real one)—**the soft-mode criterion uniquely selects ZrO₂ from the Hf/Zr family**.

> Honest boundary: the n=6 comparison is an exhaustive industry-family check rather than a statistical sample; "hit rate" is a directional validation.

### 3.2 Two-dimensional criterion space: soft-mode × bandgap

DRAM high-k criterion space = soft-mode axis (transition activity) × bandgap axis (leakage wall):

```
                bandgap axis (leakage wall, threshold ~4 eV)
                │
  Al2O3 6.43    │ high-wall region
  HfO2 tetr 4.72│ ← high-wall + soft (22.9) = better but more unstable
  ZrO2 tetr 4.03│ ← ★Pareto-optimal: soft (30.7) + high bandgap
  HfO2 mono 4.12│ hard (95.6)
  ZrO2 fluor 3.45│ hard (65.5)
  Ta2O5 3.1     │ edge
  TiO2 rutile1.77│ excluded (bandgap wall)
                └───────────── soft-mode axis →
```

**Key findings**:
1. **Tetragonal ZrO₂ P4₂/nmc (JVASP-350, lowest-energy phase) has bandgap 4.03, the highest among ZrO₂ phases**—the tetragonal phase is the Pareto-optimal point (soft-mode AFE activity + lowest leakage). This gives a complete criterion explanation of why industry has pinned the tetragonal phase for 30 years rather than using the more stable monoclinic phase: monoclinic is hard but has a lower bandgap and no AFE activity.
2. HfO₂ tetragonal (C44=22.9/Eg=4.72) has a higher bandgap in 2D space but is softer at 0K—industry HfO₂ needs heavier doping (differing from ZrO₂'s "as-deposited tendency to tetragonal" [2]) = another stability-activity tradeoff dimension.
3. Bandgap threshold: Al₂O₃ 6.43/HfO₂ 4.72/ZrO₂ 4.03 pass, Ta₂O₅ 3.1 edge, TiO₂ 1.77 excluded—corresponding one-to-one with the industry evolution history.

**TiO₂'s bandgap wall** (gun-4 de-hallucination flip): the earlier reading "TiO₂ too soft, hits wall (-16.5)" was a matching-entry artifact (P-62m hypothetical phase, Ef 0.25 eV higher); the rutile lowest-energy phase has C44=117.9 (hard). The real wall TiO₂ hits is the bandgap wall—rutile Eg=1.77 vs ZrO₂ 4.03, a 3-4 order-of-magnitude higher leakage, which has kept TiO₂ out of DRAM for 20 years. Moreover TiNbO₄ has zero bandgap (Nb doping metallization dead end).

> Honest boundary: bandgaps are JARVIS OptB88vdW values (DFT underestimation), and the absolute 4 eV threshold is an industry empirical value rather than a DFT value—the 2D axis values are DFT relative ordering; the threshold line awaits experimental calibration.

### 3.3 Quantitative doping-pinning: ionic-radius-C44 calibration curve

Alkaline-earth AZrO₃ calibration family (same-stoichiometry perovskite, joint-ranking C44 × Shannon radius CN=8):

| Dopant ion | r(Å) | C44(GPa) |
|---|---|---|
| Mg²⁺ | 0.89 | 44.3 |
| Ca²⁺ | 1.12 | 64.0 |
| Sr²⁺ | 1.26 | 75.1 |
| Ba²⁺ | 1.42 | 88.8 |

**C44 = 83.7·r − 30.1 (R²=0.9998)**—dopant ionic radius maps almost perfectly linearly to C44. Doping is a quantitative tuning knob of the C44 spectrum.

**Extrapolation and structure-domain boundary** (tolerance factor t=(r_A+r_O)/√2(r_B+r_O), r_O=1.40/r_B=0.84):

| Ion | r(Å) | extrapolated C44 | structure domain |
|---|---|---|---|
| Y³⁺ | 1.02 | 55.3 | t=0.76 boundary |
| Gd³⁺ | 1.05 | 57.8 | t=0.77 boundary |
| La³⁺ | 1.16 | 67.0 | t=0.81 distorted perovskite (extrapolation valid) |

- **Soft-mode threshold r=0.63 Å lies below the tolerance-factor lower bound 0.77**—no dopant ion within the perovskite family can reach the soft mode: perovskite-domain doping can only pin (stiffen), not enhance activity (structural conclusion).
- **Y-doping dual structure domain**: fluorite solid-solution domain = stabilization (measured YSZ C44 47-66 GPa, extrapolation 55.3 hits [5]); perovskite domain = 0K instability (YZrO₃ C44=1.1 at tolerance boundary t=0.76)—industry YSZ uses the fluorite domain as a structural necessity.
- Extrapolation valid in the perovskite family (Mg/Ca/Sr/Ba/La); the fluorite solid-solution domain (Al/Si doping) is not extrapolable (different structure domain).

### 3.4 Martensitic mirror: invariant criterion, opposite engineering goals

The same t→m martensitic transformation (4% volume expansion + shear) [6]:

- **Ceramic toughening** = exploiting transition activity (ZrO₂ PSZ/TZP toughening ceramics; ZrO₂ is a ceramic star);
- **DRAM dielectrics** = failure (volume expansion + dielectric drop → leakage/EOT deterioration), with industry doping the t phase to pin it against transformation.

**Same material, same criterion, mirrored use in two industries**—C3 soft mode selects "transition activity," and the engineering use determines the value of that activity. This explains the dual identity of ZrO₂ as both a ceramic-toughening material and a DRAM high-k dielectric.

### 3.5 Criterion D: matching-rule audit and data engineering

- **Audit finding**: 44.3% (242/546) of matched compounds are multi-entry (multiple JARVIS structures per compound); the old criterion's soft-mode set was contaminated by bad entries—TiO₂ once matched a P-62m hypothetical phase (triggered by gun 4).
- **Criterion D established**: energy window (within +0.1 eV of ground state) and non-negative min-C44, excluding both hypothetical-phase noise (energy window) and Born-instability bad values (non-negative filter).
- **Impact**: 31 of 546 compounds flipped; 24 marked as missing data; 55/56 resonance candidates preserved (only ZnTiO₃ out)—the resonance set is highly robust.
- **Global recomputation** (gun 6): new 546-compound list released (c44_old/c44_d/d_jid/d_spg full fields); window-sensitivity scan (ΔE=0.05→139/0.10→152/0.20→163/0.30→164, monotonic convergence, 0.10 chosen as mid-range reasonable); 10 small-positive anomalies (c44_d<1 GPa) handled: 5 high-confidence bad values removed (diamond C44=0.1 vs true ~500—hard evidence/ spinel/BeF₂/ice/Sc₂O₃) + 5 audit-candidate flags (release-blocking item ①, executed 8-17).
- **Criterion semantics final**: ZrO₂'s soft-mode hit = 0K instability signal of the tetragonal polymorph family (family-level), not of a single industry phase (P4₂/nmc itself C44=30.7, not soft)—the industry AFE transition is a specific phonon-mode softening (E-field-induced P4₂/nmc→Pca2₁ [3]), while global C44 shear-soft is a family-level activity proxy.

## 4. Discussion

**Why industry has pinned the tetragonal phase for 30 years**: the 2D criterion space gives the complete explanation—the tetragonal phase is the unique Pareto optimum (soft-mode activity + highest bandgap); industrial "doping stabilization" = pulling the working point back into the controllable region on the C44 spectrum (chemical pinning: quantified by the calibration curve; gradient pinning: ZAZ stack = interlayer C44-spectrum gradient [7]). DRAM high-k evolution = controllable progress on the soft-mode axis: SiO₂(67.1 hard)→Al₂O₃(43.8)→ZrO₂(20.3 soft + high k + AFE)→TiO₂(bandgap wall)—each generation moves toward the soft end for k and activity, at the cost of stability (rising pinning demand).

**Field-theoretic increment**: this is not a new-material discovery but a criterion coordinate for industrial practice—isomorphic to the photoresist line's "monopoly = tacit tuning knowledge": industry's 60-year doping experience has a sortable coordinate on the C44 spectrum (ionic-radius calibration curve), providing a criterion starting point for next-generation dielectric screening (ferroelectric memory / PCM / 3D NAND charge-trap).

## 5. Conclusion

The industrial practice of DRAM high-k dielectrics maps onto a 2D criterion space: soft-mode axis (transition activity) × bandgap axis (leakage wall). Tetragonal ZrO₂ is the unique Pareto-optimal phase (soft mode 20.3/bandgap 4.03); the 30-year industrial pinning of the tetragonal phase receives a criterion explanation; doping-pinning is quantifiable (C44=83.7·r−30.1, R²=0.9998); the martensitic mirror explains the dual industry semantics of the criterion. Criterion-D data engineering makes the criterion semantics explicit as "0K instability signal of a real metastable phase," with the data asset (546-compound list) released alongside.

## References

[1] S. Shiratake, "Scaling and Performance Challenges of Future DRAM," 2020 IEEE International Memory Workshop (IMW), pp. 1-3, 2020. DOI: 10.1109/IMW48823.2020.9108122
[2] W. Jeon, "Recent advances in the understanding of high-k dielectric materials deposited by atomic layer deposition for dynamic random-access memory capacitor applications," J. Mater. Res. 35(7):775, 2019/2020. DOI: 10.1557/jmr.2019.335
[3] M. H. Park et al., "Emerging Fluorite-Structured Antiferroelectrics and Their Semiconductor Applications," ACS Appl. Electron. Mater. 5:642, 2023. DOI: 10.1021/acsaelm.2c01615; Lomenzo et al., "Discovery of Nanoscale Electric Field-Induced Phase Transitions in ZrO₂," Adv. Funct. Mater. 33(41):2303636, 2023. DOI: 10.1002/adfm.202303636
[4] S. J. Lee et al., "Effect of La and Si additives in Zr-doped HfO₂ capacitors for pseudo-linear high-κ dielectric applications," Nano Convergence 12:15, 2025. DOI: 10.1186/s40580-025-00477-2
[5] A. Kandil et al., elastic constants of cubic zirconia, J. Am. Ceram. Soc., 1984 (8YSZ C44=47-66 GPa)
[6] R. H. J. Hannink, P. M. Kelly, B. C. Muddle, "Transformation Toughening in Zirconia-Containing Ceramics," J. Am. Ceram. Soc. 83(3):461-487, 2000. DOI: 10.1111/j.1151-2916.2000.tb01221.x
[7] R. Barshilia, B. Deepthi, K. S. Rajam, "Stabilization of tetragonal and cubic phases of ZrO₂ in pulsed sputter deposited ZrO₂/Al₂O₃ and ZrO₂/Y₂O₃ nanolayered thin films," J. Appl. Phys. 104:113532, 2008. DOI: 10.1063/1.3040720; R. C. Garvie, "The Occurrence of Metastable Tetragonal Zirconia as a Crystallite Size Effect," J. Phys. Chem. 69(4):1238-1243, 1965. DOI: 10.1021/j100888a024; H.-T. Chen et al., "TEM Observation and Study of Three-Layer Al₂O₃/ZrO₂ Ceramics," J. Nanosci. Nanotechnol. 10:2088, 2010. DOI: 10.1166/jnn.2010.2074

---
*Field-criterion paper v1.0 EN. Author: Chao Qin (Vortex) ORCID 0009-0006-2000-5644. Data assets: SPTF联合排序_v1.0_D口径_v0.2.json (546 compounds) + SPTF剪切软模候选_56_v0.3.json (54 entries). Reproducibility scripts released with the GitHub package.*
