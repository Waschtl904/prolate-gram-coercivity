# Prolate–Weil Program: Sampling, Frame Stability, and Spectral Structure

This repository contains a sequence of research papers on discrete sampling,
frame stability, and spectral structure in Paley–Wiener spaces using prolate
spheroidal wave functions (PSWFs), with connections to operator-theoretic
approaches to Weil positivity.

**Current state: Papers I–VIII complete. Hypotheses H1 and H2 of Paper VII are now unconditional.
The sole remaining open problem is B-strong.**

---

## Core Idea

The central concept developed in this series is the
**Discrete Spectral Transfer Property (DSTP)**:

> Discrete sampling preserves the spectral decay structure of PSWF
> interactions, leading to Schur-summable defect matrices and stable
> frame operators.

The main result of Paper I is a **reduction principle**: frame stability holds —
with explicit bounds — provided the DSTP is satisfied. Papers II–VIII develop the
operator-theoretic, arithmetic, semiclassical, and dyadic consequences of this
principle. **Paper VIII** establishes the three-scale architecture (combinatorial,
Airy/WKB, Landau–Widom) and completes the reduction to B-strong as the unique
remaining gap.

---

## Papers in This Repository

| File | Title | Status |
|---|---|---|
| `paper1.tex` | Frame coercivity and defect decomposition; introduction of DSTP | Complete |
| `paper2.tex` | Scaling limits, trace formula, conditional coercivity; Weil connection | Complete |
| `paper2_quadrature.tex` | XRY quadrature compatibility; conditional DSTP verification framework | Complete |
| `paper3.tex` | PSWF product spectral tail estimates; edge obstruction (bandwidth doubling) | Complete |
| `paper4_semiclassical.tex` | Semiclassical equidistribution of PSWF densities via Prüfer analysis | Complete |
| `paper5.tex` | WKB cover, Bridge Lemma, Schur control; ass:bulkconv proved for γ < 1/2 | Complete |
| `paper6.tex` | Galerkin norm estimates; No-Go theorem; B-strong framework | Complete |
| `paper7_skeleton.tex` | Dyadic cancellation for PSWF Galerkin operators; H1 unconditional | Complete |
| `paper8_scale_separated.tex` | Scale-separated dyadic cancellation; H2 unconditional; three-scale architecture | **Submission-ready** |

Companion notes (proved results, ready to insert into papers):

| File | Content | Status |
|---|---|---|
| `phase_nondeg_lemma.tex` | Phase Non-Degeneracy: α^(c) = π/2 + O(c^{−1/3}); H1 unconditional | **Proved** ✅ |
| `airy_discrete_stability_lemma.tex` | Proposition U(U') + ass:gap unconditional | **Proved** ✅ |
| `bridge_lemma.tex` | Bridge Lemma fully written out (to insert in paper5.tex) | **Proved** ✅ |
| `ax5_independence_remark.tex` | DSTP logically independent of AX1–AX4 (Riemann-rule witness) | **Proved** ✅ |
| `section5_numerical_evidence.tex` | Numerical evidence for spectral tail separation (for paper2_quadrature.tex) | Supplementary |

Internal documentation:

| File | Description |
|---|---|
| `numerics/` | Computational experiments and scripts |
| `DEPENDENCIES.md` | Full logical dependency graph between all papers and companion notes |
| `context_summary.md` | Internal working summary (session context scaffold) |
| `PROMPT.md` | Internal prompt scaffolding for AI-assisted sessions |
| `PHASE_NONDEG_NOTE.md` | **Superseded** — Phase Non-Degeneracy gap now closed; see `phase_nondeg_lemma.tex` |
| `assumption_2_4_target.md` | **Archived** — proof strategies for ass:bulkconv, superseded by Paper V |

---

## What is Now Unconditional

The following results hold **without any remaining assumptions**:

- **ass:bulkconv** (Assumption 2.4, Paper III): proved for γ < 1/2 via Bridge Lemma (Paper V) ✅
- **Phase Non-Degeneracy**: α^(c) = π/2 + O(c^{−1/3}), so dist(α^(c), {0,π}) ≥ π/4 for all large c;
  Conjecture 6.1 of Paper VI proved (`phase_nondeg_lemma.tex`) ✅
- **Proposition U and U'** (Paper VIII): ||λ_l − F_Ai(x_l)|| ≤ C₁c^{−2/3} and the discrete
  derivative stability bound, both proved (`airy_discrete_stability_lemma.tex`) ✅
- **ass:gap** (Assumption 1, Paper VIII): uniform spectral gap λ_l − λ_{l+1} ≥ κ₀ (c/2)^{−1/3}
  with κ₀ = c_min/2, proved unconditionally (`airy_discrete_stability_lemma.tex`) ✅
- **H1** (Paper VII, phase hypothesis): unconditional ✅
- **H2** (Paper VII/VIII, amplitude regularity): unconditional via ass:gap + Prop. U' ✅
- **Lemma F** (Dyadic Separation Principle, Paper VIII): unconditional ✅
- **Corollary C** (Paper VIII): unconditional ✅

---

## Paper VIII: Three-Scale Architecture

**Paper VIII** (`paper8_scale_separated.tex`) establishes the three-scale structure
of the dyadic cancellation mechanism:

| Scale | Layer | Content | Status |
|---|---|---|---|
| Combinatorial `c^{−1/3}` | Dyadic Separation | Lemma F (DSP), Corollary C | ✅ Unconditional |
| Local Airy `(c/2)^{−1/3}` | Airy / WKB | Proposition U(U'), Lemma A | ✅ Unconditional |
| Global Landau–Widom `(log c)^{2/3}` | erfc profile | Conjecture ULW | 📊 Empirical only |

The key algebraic mechanism: in Corollary C, Term 1, the factor `(c/2)^{−1/3}`
cancels exactly between numerator and denominator, yielding an O(2^{−m}) bound
**independent of c**.

### Empirical evidence (Conjecture ULW)

Numerical evidence for the **Landau–Widom global scaling law**:
```
λ_l ≈ (1/2) erfc( ln2 · (l − N_Sh − β(c)) / S(c) ),   S(c) = (log c/π)^{2/3}
```
with cross-bandwidth residuals ≈ 2·10^{−2} across c ∈ {50, 100, 200},
decreasing with c. The centering parameter β(c) drifts slowly;
its limit β(∞) ∈ [−0.30, −0.21] (empirical) is an open problem.

---

## Open Problems (May 2026)

The program now has a single remaining structural gap:

### The Sole Remaining Gap

| Problem | Location | Status |
|---|---|---|
| **B-strong**: `P_{kl} ≤ C₂ c^{1/2}` in the transition zone | Paper VI/VII H3 | 🔴 Open |

Once B-strong is proved: H3 ✅ → Theorem 1 (Paper VII) unconditional → contraction estimate
`‖DT_c^(N)‖ ≤ C c^{−1/2} log c < 1` for large c → Assumption A → complete theory.

**Why B-strong is hard:** two concrete failure modes (Paper VI, Remark 5.2):
- Non-uniform stationary phase in the transition zone
- Correlated Airy factors (eigenvalue spacing and amplitude not independent)

**Route:** WKB/Airy matching at s* = 1 − c^{−2/3}, model problem formulation —
likely a paper-level problem.

### Secondary Open Problems

| Problem | Evidence / Status |
|---|---|
| **Conjecture ULW**: erfc global scaling law | Numerical residuals ≈ 2·10^{−2} |
| Limit of β(c) as c → ∞ | Fitting suggests β(∞) ∈ [−0.30, −0.21] |
| Bridge Lemma extension to γ ≥ 1/2 | Geometry breaks; stationary phase route open |
| Off-diagonal decay (Assumption 3.1, Paper III) | Edge regime; Airy methods needed |
| Weil operator identification G_∞ (Paper II) | Structural; medium term |
| XRY stability conjecture (Paper II_quad) | Conditional; medium term |
| DSTP for prime sampling (Paper I) | Long term |

---

## Logical Dependency Chain

```
phase_nondeg_lemma.tex
    ↓ proves H1 (Paper VII) unconditionally
airy_discrete_stability_lemma.tex
    ↓ proves ass:gap + Prop. U(U') unconditionally
    ↓ proves H2 (Paper VII/VIII) unconditionally

B-strong (open)
    ↓ will prove H3 (Paper VII)

H1 ✅ + H2 ✅ + H3 (⚠️ B-strong)
    ↓
Paper VII Theorem 2.1 (abstract dyadic cancellation)
    ↓
Contraction estimate: ‖DT_c^{(N)}‖ < 1 for large c
    ↓
Assumption A → complete frame stability theory

───────────────────────────────────────────────

Paper IV (PSWF equidistribution)
    ↓ supplies Prüfer amplitude inputs
Paper V (Bridge Lemma)
    ↓ proves ass:bulkconv unconditionally for γ < 1/2
Paper III (spectral tail bounds)
    ↓ conditional bulk tail bound (edge regime open)
Paper II_quad + XRY stability conjecture
    ↓
Paper I (frame stability under DSTP)
    ↓
Conditional frame stability for PSWF-Gauss sampling
```

---

## Key References

- Osipov–Rokhlin–Xiao (2013): *Prolate Spheroidal Wave Functions of Order Zero*, Springer
- Slepian (1978): *Prolate spheroidal wave functions, Fourier analysis, and uncertainty V*, Bell Syst. Tech. J.
- Xiao–Rokhlin–Yarvin (2001): *Prolate spheroidal wave functions, quadrature, and interpolation*, Inverse Problems
- Connes–Consani–Moscovici (2022, 2025): UV prolate spectrum and zeros of zeta, PNAS; arXiv:2511.22755
- Levitan–Sargsjan (1991): *Sturm–Liouville and Dirac Operators*, Kluwer
- Weil (1952): *Sur les formules explicites de la théorie des nombres*
- Reed–Simon (1980): *Methods of Modern Mathematical Physics I*, Academic Press
- NIST DLMF (2023): Digital Library of Mathematical Functions, https://dlmf.nist.gov/
