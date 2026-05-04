# Logical Dependency Graph — Papers I–VIII

> This file documents which results each paper imports from earlier papers.
> Status: ✅ unconditional | ⚠️ conditional | 🔴 open/unproved | ❌ disproved/obstructed
> Last updated: May 2026 (after Paper VIII submission-ready v6)

---

## Overview

Papers I–VIII form the complete series to date.
Paper VIII (Dyadic Separation) is the most recent paper; it establishes a
**conditional reduction theorem** under Assumption ass:gap and B-strong.
Paper IV closes the bulk decorrelation step unconditionally.
Paper IX (WKB attack on ass:gap) is in preparation.

```
Paper I → Paper II (companion) → Paper III → Paper IV
                ↑_______________________________↑
         (Paper II conjectures; Papers III–IV prove/reduce)

Paper V → Paper VI (B-strong framework)
               ↓
Paper VII (abstract dyadic cancellation) ← Paper VIII (scale-separated reduction)
```

---

## Main Dependency Table: Papers I–IV (Prolate–Weil subprogram)

| Result exported | Source | Used by | Status |
|---|---|---|---|
| Frame coercivity under the DSTP | Paper I | Paper II, Paper III | ✅ |
| Implication framework (Conj. 3.1 + XRY → DSTP) | Paper II (quadrature) | — | ⚠️ conditional |
| `conj:pswf_product_tail`(i) bulk: exponential decay for `m,n ≤ γN` | Paper II (quad) | Paper III (target) | ⚠️ bulk decorrelation closed by Paper IV; exponential tail conditional on Ass. 2.4 |
| `conj:pswf_product_tail`(ii) off-diagonal: algebraic decay `|m-n| ≥ δN` | Paper II (quad) | Paper III (target) | ⚠️ conditional on Paper III Ass. 3.1 |
| `conj:pswf_product_tail`(iii) global uniform bound over all `m,n ≤ N` | Paper II (quad) | — | ❌ **disproved** by Paper III `prop:bwdoubling` |
| Unconditional uniform bound `‖(I−P_N)f_{mn}‖ ≤ CT^{1/2}` | Paper III | Paper II (quad) | ✅ |
| Mean spectral localization, exact IBP energy identity, spectral lower bound | Paper III | Paper II (quad) | ✅ |
| Edge obstruction: global uniform tail bound false for `m,n ~ N` | Paper III | Paper II (quad) | ✅ negative dependency |
| **Weak convergence of PSWF densities to ρ^cl, rate O(1/n)** | **Paper IV** | **Paper III Lem 6.3** | **✅ unconditional** |
| **Hypothesis (6.1) of Bulk Decorrelation Reduction (Lemma 6.3)** | **Paper IV** | **Paper III** | **✅ resolved** |
| Bulk exponential tail bound | Paper III (via Paper IV) | Paper II (quad) | ⚠️ conditional on Ass. 2.4 |

---

## Main Dependency Table: Papers V–VIII (Dyadic subprogram)

| Result exported | Source | Used by | Status |
|---|---|---|---|
| Galerkin norm estimates; coercivity structure | Paper V | Papers VI, VII | ✅ |
| B-strong: `P_{kl} ≤ C₂ c^{1/2}` in transition zone | Paper VI | Papers VII, VIII | 🔴 **open — no proof available** |
| Abstract dyadic cancellation Theorem 2.1; reduction to (H1)–(H3) | Paper VII | Paper VIII | ✅ |
| H2 verification in truncated dyadic sense (Corollary C) | Paper VIII | — | ✅ under ass:gap + Prop U |
| **Dyadic Separation Principle (Lemma F)** | **Paper VIII** | **core of series** | **✅ rigorous under ass:gap** |
| Conditional reduction: ass:gap + B-strong → `‖D T_c^{(N)}‖ < 1` | Paper VIII | Paper IX (target) | ⚠️ both inputs open |
| Proposition U: uniform Airy approx `|λ_l − F_Ai(x_l)| ≤ C₁ c^{−2/3}` | Paper VIII (stated) | Papers VIII (Lem A, Term 2) | 🔴 **open** |
| Proposition U': discrete derivative bound `|Δλ_l − ΔF_Ai(x_l)| ≤ C₂ c^{−2/3}` | Paper VIII (stated) | Paper VIII Lem A | 🔴 **open** |
| Assumption ass:gap: `λ_l − λ_{l+1} ≥ κ_0 (c/2)^{−1/3}` | Paper VIII (stated) | Paper VIII Lem F | 🔴 **open — target of Paper IX** |
| Conjecture ULW: global erfc scaling law | Paper VIII (empirical) | — | 📊 numerical only |

---

## Dependency Flow for the Dyadic Separation Principle

```
Assumption ass:gap          Proposition U (U')         B-strong (Paper VI)
       ↓                          ↓                          ↓
  Lemma F (DSP)             Lemma A (Airy incr.)       Paper VII Lem 5.2
       ↓                          ↓                          ↓
 Cor. C part (a)           Cor. C part (b), Term 2    Core sum bound
       └──────────────────────────┴───────────────────────────┘
                                  ↓
                           Lemma E (Core–WKB split)
                                  ↓
                    Corollary: (H1)–(H3) verified
                                  ↓
                    Paper VII Theorem 2.1 applied
                                  ↓
                    ‖D T_c^{(N)}‖ < 1  for large c
```

**Key independence property of Lemma F:**
The Dyadic Separation Principle requires *only* Assumption ass:gap —
no Airy functions, no erfc structure, no specific form of the eigenvalue profile.
Proposition U enters exclusively via parts (b) and Term 2 of Corollary C,
and as one sufficient route to ass:gap. It is not the logical foundation.

---

## Three-Scale Architecture (Paper VIII)

| Scale | Physical layer | Key result | Logical status |
|---|---|---|---|
| Combinatorial `c^{−1/3}` | Dyadic Separation | Lemma F, Corollary C | ✅ rigorous under ass:gap |
| Local Airy `(c/2)^{−1/3}` | Airy/WKB approximation | Proposition U, Lemma A | 🔴 open |
| Global Landau–Widom `(log c)^{2/3}` | erfc eigenvalue profile | Conjecture ULW | 📊 empirical |

Scale separation confirmed: `S(c) / (c/2)^{−1/3} ~ c^{1/3} (log c)^{2/3} → ∞`.

---

## Open Problems (May 2026)

### Tier 1 — Open inputs blocking unconditional proof

| Problem | Where needed | Routes known |
|---|---|---|
| **ass:gap**: `λ_l − λ_{l+1} ≥ κ_0 (c/2)^{−1/3}` | Paper VIII Lem F | (i) via Prop U; (ii) WKB monotone comparison (Paper IX target); (iii) heuristic numerics |
| **Proposition U**: `|λ_l − F_Ai(x_l)| ≤ C₁ c^{−2/3}` | Paper VIII Lem A, Term 2 | Uniform WKB + Airy matching; step (iii) (discrete diff.) is the additional gap |
| **B-strong**: `P_{kl} ≤ C₂ c^{1/2}` | Paper VIII Lem E | Galerkin norm argument |
| **Assumption 2.4** (bulk convolution decay, Paper III) | Paper III tail bound | Schur test on product kernel (see `assumption_2_4_target.md`) |

### Tier 2 — Open problems in the larger program

| Problem | Source | Status |
|---|---|---|
| DSTP for prime sampling | Paper I | 🔴 |
| Off-diagonal algebraic decay (Ass. 3.1) | Paper III | 🔴 |
| XRY stability conjecture | Paper II (quad) | 🔴 |
| Identification of G_∞ as Weil operator | Paper II | 🔴 |
| Uniqueness and tr(G_∞) = 1 | Paper II | 🔴 |
| Edge regime analysis (m,n ~ N; Airy-scale) | Papers II quad, III | 🔴 |
| C⁰ extension of Paper IV main theorem | Paper IV | 🟡 partial |
| Off-diagonal analogue of Paper IV | Paper IV | 🔴 |

### Tier 3 — Empirical (Paper VIII)

| Conjecture | Evidence | Open subproblem |
|---|---|---|
| Conjecture ULW: erfc law with S(c) = (log c/π)^{2/3} | Residuals ≈ 2·10^{−2}, c ∈ {50,100,200} | Analytic derivation |
| β(c) → β(∞) ∈ [−0.30, −0.21] | Numerical fitting, high model sensitivity | Structural identification of β(c) |

---

## Unconditionally Proved Results (May 2026)

### Papers I–IV
- Frame coercivity under DSTP with explicit bounds (Paper I) ✅
- Exact algebraic defect decomposition `E_mn = R_mn^quad` (Paper I) ✅
- DSTP verified for random and Gauss–PSWF sampling (Paper I) ✅
- Compactness of normalized Gram operators in scaling limit (Paper II) ✅
- Trace formula consistent with PNT (Paper II) ✅
- Uniform off-diagonal bound, mean spectral localization, spectral lower bound (Paper III) ✅
- Edge obstruction: global uniform tail bound false for m,n ~ N (Paper III) ✅
- **PSWF equidistribution: `∫f ψ_n² = λ_n ∫f ρ^cl + O(λ_n ‖f‖_{C¹}/n)` (Paper IV) ✅**
- **Bulk decorrelation hypothesis (6.1) supplied unconditionally (Paper IV → III) ✅**

### Papers V–VIII
- Galerkin norm estimates; coercivity structure (Paper V) ✅
- Abstract dyadic cancellation theorem (Paper VII, Theorem 2.1) ✅
- **Dyadic Separation Principle: `|λ_i − λ_j| ≥ κ_0 (c/2)^{−1/3} |i−j|` (Paper VIII, Lemma F, under ass:gap) ✅**
- **Scale independence: (c/2)^{−1/3} cancels in Term 1 of Corollary C (Paper VIII) ✅**
- **Conditional reduction: ass:gap + B-strong → (H1)–(H3) → contraction (Paper VIII) ✅**
- Numerical evidence for Conjecture ULW, β(c) behavior (Paper VIII, empirical) 📊
