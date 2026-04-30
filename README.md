# Prolate–Weil Program: Sampling, Frame Stability, and Spectral Structure

This repository contains a sequence of research papers on discrete sampling,
frame stability, and spectral structure in Paley–Wiener spaces using prolate
spheroidal wave functions (PSWFs), with connections to operator-theoretic
approaches to Weil positivity.

---

## Core Idea

The central concept developed in this series is the
**Discrete Spectral Transfer Property (DSTP)**:

> Discrete sampling preserves the spectral decay structure of PSWF
> interactions, leading to Schur-summable defect matrices and stable
> frame operators.

The main result of Paper I is a **reduction principle**: frame stability holds —
with explicit bounds — provided the DSTP is satisfied. Papers II–IV develop the
operator-theoretic, arithmetic, and semiclassical consequences of this principle.

---

## Papers in This Repository

| File | Title | Status |
|---|---|---|
| `paper1.tex` | Frame coercivity and defect decomposition; introduction of DSTP | Reinschrift |
| `paper2.tex` | Scaling limits, trace formula, conditional coercivity; Weil connection | Reinschrift |
| `paper2_quadrature.tex` | XRY quadrature compatibility; conditional DSTP verification framework | Reinschrift |
| `paper3.tex` | PSWF product spectral tail estimates; edge obstruction (bandwidth doubling) | Reinschrift |
| `paper4_semiclassical.tex` | Semiclassical equidistribution of PSWF densities via Prüfer analysis | Complete |
| `section5_numerical_evidence.tex` | Numerical experiments supporting the analytic results | In progress |

Additional files:

| File | Description |
|---|---|
| `numerics/` | Computational experiments and scripts |
| `DEPENDENCIES.md` | Logical dependency graph between all papers |
| `context_summary.md` | Internal working summary (session context scaffold) |
| `assumption_2_4_target.md` | Proof strategies for the remaining open bulk convolution assumption |
| `PROMPT.md` | Internal prompt scaffolding |

---

## Relationship Between the Papers

**Paper I** establishes the core reduction: frame stability of the prolate
sampling operator is equivalent to a spectral defect condition (DSTP).
An exact algebraic defect decomposition is proved
(`E_mn = R_mn^quad`; the PSWF orthogonality term vanishes exactly).
Unconditional coercivity holds for unisolvent sampling configurations;
DSTP is verified for random and Gauss–PSWF sampling.
Prime sampling is left open.

**Paper II** develops the operator-theoretic scaling limit: normalized
Gram operators along prime sampling sequences are unconditionally compact
(Banach–Alaoglu), and a trace formula connects the weighted Gram matrix to
the prime number theorem. Strong coercivity `λ_min → 1` in the scaling limit
is conditional on DSTP holding along prime sequences (Assumption H).
No claim is made about zeros of ζ(s).

**Paper II (quadrature)** organises the problem of verifying DSTP for
XRY PSWF-Gauss quadrature into two explicit conjectural inputs:
a PSWF product spectral tail conjecture and an XRY stability conjecture.
The scope is restricted to the bulk and off-diagonal regimes.
The edge regime (`m, n ~ N`) is identified as a **proved structural obstruction**
via bandwidth doubling (established in Paper III), not a conjecture.

**Paper III** provides the analytical foundation for the product spectral tail.
Three results are unconditional:
- Uniform off-diagonal bound `‖(I−P_N)f_mn‖ ≤ C T^{1/2}`.
- Mean spectral localization `𝔼_mn[χ_k] = μ_mn + E_mn`.
- Spectral lower bound `𝔼_mn[χ_k] ≥ μ_mn/2` (exact energy decomposition).

The bulk exponential tail bound is conditional on Assumption 2.4 (bulk
convolution decay; see Open Problems). The off-diagonal algebraic decay
is conditional on Assumption 3.1 (pointwise spectral localization).
The edge obstruction is proved.

A **Bulk Decorrelation Reduction** (Lemma 6.3) shows that the energy
equidistribution goal reduces to the weak convergence of `ψ_n²` to the
classical equilibrium density — a problem resolved unconditionally by Paper IV.

**Paper IV** proves the semiclassical equidistribution theorem for PSWF
densities by elementary ODE methods (Prüfer phase analysis, integration by
parts, drift cancellation identity), without microlocal machinery or
Riemann–Hilbert methods. The main result gives, for all `f ∈ C¹` and `n ≤ γN`:

```
∫ f ψ_n² dx  =  λ_n(c) ∫ f ρ^cl dx  +  O(λ_n ‖f‖_{C¹} / n)
```

uniformly in `n`. This supplies hypothesis (6.1) of Lemma 6.3 in Paper III
unconditionally, **closing the bulk decorrelation step** of the program.
The bulk tail bound itself remains conditional on Assumption 2.4 of Paper III.

---

## Current State of Open Problems (April 2026)

| Problem | Source | Status |
|---|---|---|
| DSTP for prime sampling | Paper I | 🔴 Open |
| Bulk convolution decay (Assumption 2.4 of Paper III) | Paper III | 🔴 Open — main remaining analytic gap |
| Off-diagonal spectral localization (Assumption 3.1 / specloc) | Paper III | 🔴 Open |
| XRY stability conjecture | Paper II (quad) | 🔴 Open |
| Identification of G_∞ as Weil operator | Paper II | 🔴 Open |
| Uniqueness and tr(G_∞) = 1 | Paper II | 🔴 Open |
| C⁰ extension of Paper IV equidistribution | Paper IV | 🟡 Partial (density argument gives rate-free convergence) |
| Off-diagonal analogue of Paper IV main theorem | Paper IV | 🔴 Open |
| Edge regime analysis (m, n ~ N) | Papers II(quad), III | 🔴 Open — requires Airy-scale methods |
| Critical density regime N/c → 2/π | Paper II | 🔴 Open |

**Closed by Paper IV:**

| Problem | Resolved in |
|---|---|
| Weak convergence of `ψ_n²` to `ρ^cl` (rate O(1/n)) — Problem prob:pswf-weak-limit of Paper III | Paper IV, Theorem 1 |
| Hypothesis of Bulk Decorrelation Reduction (Lemma 6.3 of Paper III) | Paper IV, Corollary 5.2 |

A full dependency and status graph is in [`DEPENDENCIES.md`](DEPENDENCIES.md).

---

## Logical Dependency Chain (Summary)

```
Paper IV (equidistribution)
    ↓ supplies Lemma III.6.3 unconditionally
Paper III (bulk reduction) + Assumption 2.4 (open)
    ↓ conditional bulk tail bound
Paper II(quad) + XRY stability conjecture (open)
    ↓ conditional DSTP for XRY quadrature (bulk/off-diagonal)
Paper I (frame stability under DSTP)
    ↓
Conditional frame stability for PSWF-Gauss sampling

Paper II (scaling limit)
    ↓ unconditional compactness + trace formula
    ↓ conditional coercivity under Assumption H (prime DSTP, open)
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
