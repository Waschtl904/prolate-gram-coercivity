# Prolate–Weil Program: Sampling, Frame Stability, and Spectral Structure

This repository contains a sequence of research papers on discrete sampling,
frame stability, and spectral structure in Paley–Wiener spaces using prolate
spheroidal wave functions (PSWFs), with connections to operator-theoretic
approaches to Weil positivity.

**Current state: Papers I–VIII complete. Paper IX (WKB attack on ass:gap) in preparation.**

---

## Core Idea

The central concept developed in this series is the
**Discrete Spectral Transfer Property (DSTP)**:

> Discrete sampling preserves the spectral decay structure of PSWF
> interactions, leading to Schur-summable defect matrices and stable
> frame operators.

The main result of Paper I is a **reduction principle**: frame stability holds —
with explicit bounds — provided the DSTP is satisfied. Papers II–VII develop the
operator-theoretic, arithmetic, semiclassical, and dyadic consequences of this
principle. **Paper VIII** completes the conditional reduction to the
Dyadic Separation Principle, depending only on Assumption ass:gap and B-strong.

---

## Papers in This Repository

| File | Title | Status |
|---|---|---|
| `paper1.tex` | Frame coercivity and defect decomposition; introduction of DSTP | Complete |
| `paper2.tex` | Scaling limits, trace formula, conditional coercivity; Weil connection | Complete |
| `paper2_quadrature.tex` | XRY quadrature compatibility; conditional DSTP verification framework | Complete |
| `paper3.tex` | PSWF product spectral tail estimates; edge obstruction (bandwidth doubling) | Complete |
| `paper4_semiclassical.tex` | Semiclassical equidistribution of PSWF densities via Prüfer analysis | Complete |
| `paper5.tex` | Galerkin operator norm estimates; coercivity structure | Complete |
| `paper6.tex` | Galerkin norm estimates for the prolate phase operator (B-strong framework) | Complete |
| `paper7_skeleton.tex` | Dyadic cancellation for PSWF Galerkin operators; abstract Theorem 2.1 | Complete |
| `paper8_scale_separated.tex` | Scale-separated dyadic cancellation; Dyadic Separation Principle | **Submission-ready v6** |
| `section5_numerical_evidence.tex` | Numerical experiments supporting the analytic results | Supplementary |

Additional files:

| File | Description |
|---|---|
| `numerics/` | Computational experiments and scripts |
| `DEPENDENCIES.md` | Logical dependency graph between all papers |
| `context_summary.md` | Internal working summary (session context scaffold) |
| `assumption_2_4_target.md` | Proof strategies for the remaining open bulk convolution assumption |
| `PROMPT.md` | Internal prompt scaffolding |

---

## Paper VIII: The Dyadic Separation Principle

**Paper VIII** (`paper8_scale_separated.tex`) is the most recent completed paper
in the series. It establishes two classes of results:

### Rigorous core

Under **Assumption ass:gap** (uniform spectral gap lower bound at scale
`(c/2)^{−1/3}`) and **B-strong** (from Paper VI), the three hypotheses
(H1)–(H3) of Paper VII's abstract dyadic cancellation theorem are verified
via the **Dyadic Separation Principle**:

> For `j ∈ B_m(i)`, the ratio `|λ_j − λ_{j+1}| / |λ_i − λ_j|` is bounded
> by `C · 2^{−m}` independently of `c`, because the factor `(c/2)^{−1/3}`
> cancels exactly between numerator and denominator.

This cancellation is a **scale-combinatorial mechanism** requiring only
monotonicity and a uniform gap lower bound — independent of any detailed
spectral asymptotics beyond that local gap condition.

### Three-scale architecture

| Scale | Layer | Content | Status |
|---|---|---|---|
| Combinatorial `c^{−1/3}` | Dyadic Separation | Lemma F (DSP), Corollary C | ✅ Rigorous (under ass:gap) |
| Local Airy `(c/2)^{−1/3}` | Airy / WKB | Proposition U (U'), Lemma A | ⚠️ Open (Prop U unproved) |
| Global Landau–Widom `(log c)^{2/3}` | erfc profile | Conjecture ULW | 📊 Empirical only |

### Empirical evidence (Conjecture ULW)

Numerical evidence for the **Landau–Widom global scaling law**:
```
λ_l ≈ (1/2) erfc( ln2 · (l − N_Sh − β(c)) / S(c) ),   S(c) = (log c/π)^{2/3}
```
with cross-bandwidth residuals ≈ 2·10^{−2} across c ∈ {50, 100, 200},
decreasing with c. The centering parameter β(c) drifts slowly
(β(50) ≈ −0.42, β(200) ≈ −0.36); its limit is an open problem.

---

## Open Problems (May 2026)

The program has a clean three-tier structure:

### Tier 1 — Rigorous core (complete under stated assumptions)

- Dyadic Separation Principle (Paper VIII, Lemma F) ✅
- Abstract dyadic cancellation theorem (Paper VII, Theorem 2.1) ✅
- Conditional reduction: ass:gap + B-strong → contraction estimate ✅

### Tier 2 — Open inputs (required to make the core unconditional)

| Problem | Location | Planned route |
|---|---|---|
| **ass:gap**: uniform spectral gap `λ_l − λ_{l+1} ≥ κ_0 (c/2)^{−1/3}` | Paper VIII Assumption 1 | WKB monotone comparison (Paper IX) |
| **Proposition U (and U')**: uniform Airy approximation `|λ_l − F_Ai(x_l)| ≤ C₁ c^{−2/3}` | Paper VIII Proposition 1 | WKB + Airy matching |
| **B-strong**: `P_{kl} ≤ C₂ c^{1/2}` in the transition zone | Paper VI/VIII | Galerkin norm bound |
| **Bulk convolution decay** (Assumption 2.4 of Paper III) | Paper III | Schur test on product kernel |
| DSTP for prime sampling | Paper I | — |

### Tier 3 — Empirical (no analytic proof at present)

| Problem | Evidence |
|---|---|
| **Conjecture ULW**: erfc global scaling law | Numerical residuals ≈ 2·10^{−2} |
| Limit of β(c) as c → ∞ | Fitting suggests β(∞) ∈ [−0.30, −0.21] |
| XRY stability conjecture (Paper II quad) | Heuristic |

---

## Planned: Paper IX

**Paper IX** will attack **Assumption ass:gap** via the WKB route:

1. First-order WKB comparison for PSWF eigenvalue increments
2. Monotone comparison argument at leading order (without full Airy matching)
3. Goal: prove `λ_l − λ_{l+1} ≥ κ_0 (c/2)^{−1/3}` unconditionally

This is the highest-priority open problem since ass:gap is the **sole remaining
gap** between the current conditional reduction and a fully rigorous proof of
the contraction estimate.

---

## Logical Dependency Chain

```
Paper IX (WKB — planned)
    ↓ will prove
Assumption ass:gap (uniform gap lower bound)
    ↓
Paper VIII Lemma F (Dyadic Separation Principle)
    ↓ + B-strong (Paper VI, open)
Paper VIII Corollary: (H1)–(H3) verified
    ↓
Paper VII Theorem 2.1 (abstract dyadic cancellation)
    ↓
Contraction estimate: ‖D T_c^{(N)}‖ < 1 for large c

───────────────────────────────────────────────────

Paper IV (PSWF equidistribution)
    ↓ supplies hypothesis (6.1)
Paper III Lemma 6.3 (bulk decorrelation) + Ass. 2.4 (open)
    ↓ conditional bulk tail bound
Paper II (quad) + XRY stability conjecture (open)
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
