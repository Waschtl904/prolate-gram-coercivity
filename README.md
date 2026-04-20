# Prolate Gram Coercivity — Paper Series I–XVII

> **Revised & consolidated repository** for the PSWF–Hilbert–Pólya paper series.
> Original drafts: [`Waschtl904/prolate-primes-paper`](https://github.com/Waschtl904/prolate-primes-paper)
> This repo contains corrected, referee-ready versions, pushed paper by paper.

---

## Overarching Goal

Construct a self-adjoint spectral operator whose eigenvalue distribution mirrors the non-trivial zeros of the Riemann zeta function (Hilbert–Pólya programme). The core object is the PSWF concentration operator and its Mellin/Fourier transform.

**Series arc:**
Coercivity → scaling limits → spectral phase → bandwidth decay → rigorous peak-width bounds → crossover asymptotics → lower bounds + spectral-zeta connection → domain & self-adjointness → Mosco form convergence & Friedrichs extension → spectral inclusion & density criterion → localization principle → completeness & coefficient stability → microlocal Lagrangian singularity transport / Airy normal form → uniform CFU stability (Paper XVII).

---

## Current Repository State (as of April 2026)

| File | Paper | Status | Description |
|---|---|---|---|
| `paper1.tex` | I | ✅ pushed | Gram matrix coercivity |
| `paper2.tex` | II | ✅ pushed | Scaling limits & trace formula |
| `paper2_quadrature.tex` | II (ext.) | ✅ pushed | Quadrature extension to Paper II |
| `section5_numerical_evidence.tex` | V (section) | ✅ pushed | Numerical evidence section |
| `context_summary.md` | — | 📋 META | Full series context & open problems |
| `DEPENDENCIES.md` | — | 📋 META | Logical dependency graph |
| `numerics/` | — | 📁 DIR | Numerical scripts & data |

> **Note:** Files currently in the repo are early draft versions (without `_FINAL` suffix).
> Referee-ready `_FINAL` versions will replace them as revision is completed.

---

## Planned Structure (upload in progress)

Papers are pushed in order of logical independence and revision completeness:

### Phase 1 — Papers I–V (most self-contained, near publication-ready)
| File | Paper | Target Status | Description |
|---|---|---|---|
| `paper1_FINAL.tex` | I | 🔶 pending | Gram matrix coercivity |
| `paper2_FINAL.tex` | II | 🔶 pending | Scaling limits & trace formula |
| `paper3_FINAL.tex` | III | 🔶 pending | Spectral phase analysis |
| `paper4_FINAL.tex` | IV | 🔶 pending | No-go theorem (naive constructions) |
| `paper5_FINAL.tex` | V | 🔶 pending | Barrier estimates & numerical evidence |

### Phase 2 — Papers VI–VIII (after VI→VII dependency is explicitly declared)
| File | Paper | Target Status | Description |
|---|---|---|---|
| `paper6_FINAL.tex` | VI | 🔶 pending | Rigorous upper bounds (Airy profile) |
| `paper7_FINAL.tex` | VII | 🔶 pending | Composite asymptotics in crossover zone |
| `paper8_FINAL.tex` | VIII | 🔶 pending | Non-cancellation & sharp lower bound |

### Phase 3 — Papers IX–XIII (conditional framework, ongoing revision)
| File | Paper | Target Status | Description |
|---|---|---|---|
| `paper9_DRAFT.tex` | IX | 🔶 pending | Conditional framework: domain & closability |
| `paper10_DRAFT.tex` | X | 🔶 pending | Mosco form convergence & Friedrichs extension |
| `paper11_DRAFT.tex` | XI | 🔶 pending | Spectral structure & density criterion |
| `paper12_DRAFT.tex` | XII | 🔶 pending | Localization principle for spectral projections |
| `paper13_DRAFT.tex` | XIII | 🔶 pending | Completeness barrier (no-reduction theorem) |

### Phase 4 — Papers XIV–XVII + fold_model (microlocal layer, after Closing Moves A+B)
| File | Paper | Target Status | Description |
|---|---|---|---|
| `paper14_DRAFT.tex` | XIV | 🔶 pending | HS-norm estimates & regime decomposition |
| `paper15_DRAFT.tex` | XV | 🔶 pending | Intermediate-regime kernel estimates |
| `fold_model.tex` | — | 🔶 pending | Universal CFU fold-amplitude normal form |
| `paper_xvi_draft.tex` | XVI | 🔶 pending | Lagrangian singularity transport / Airy normal form |
| `paper_xvii.tex` | XVII | 🔶 pending | Uniform CFU stability for PSWF fold geometry |

---

## Critical Open Problems (as of April 2026)

| Problem | Front | Status |
|---|---|---|
| `H_SOT = closure(H_spec)` (Bridge Theorem) | Operator identification | 🔴 OPEN |
| Uniform CFU Jacobian bounds — Assumption 4.1(vi) for PSWF | Microlocal | 🔴 OPEN |
| Explicit period `T(λ_n)` for `V(x) = x²/(1-x²)` | Classical dynamics | 🔴 OPEN |
| Completeness of `{Φ_n^(∞)}` in L² | Spectral completeness | 🔴 OPEN |
| Subsequence-independence of `λ_n^(∞)`, `Φ_n^(∞)` | Spectral uniqueness | 🔴 OPEN |
| Gap lower bound `\|λ_n^(c) - λ_{n+1}^(c)\| ≥ C c^{-3/4}` | Spectral gap | 🔴 OPEN |
| Lipschitz regularity of PSWF amplitude (Prob. 6.1, Paper XV) | HS programme | 🔴 OPEN |
| Local Weyl law (Prob. 7.1, Paper XV) | HS programme | 🔴 OPEN |

---

## Planned Next Papers

- **Paper XVIII-A:** Explicit computation of `T(λ_n)` + regularity (classical action integral)
- **Paper XVIII-B:** CFU-Jacobian Lemma as isolated elliptic FIO stability result (Hörmander-style)

> After XVIII-A and XVIII-B, Theorem XVII is formally closed.

---

## Key References

- Olver (1974): *Asymptotics and Special Functions*
- Osipov–Rokhlin–Xiao (2013): *Prolate Spheroidal Wave Functions of Order Zero*
- Slepian–Pollak (1961): Original PSWF paper
- Zworski (2012): *Semiclassical Analysis*, AMS
- Hörmander (1983): *Analysis of Linear PDE I* — Ch. 7.7, 18.1–18.2, 25.1
- Kato (1966): *Perturbation Theory for Linear Operators*
- Chester–Friedman–Ursell (1957): CFU steepest descent extension
- Guillemin–Uhlmann (1981): Oscillatory integrals with singular symbols
- CCM2025: Connes–Consani–Moscovici, arXiv:2511.22755
