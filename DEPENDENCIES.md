# Logical Dependency Graph — Papers I–IV

> This file documents which results each paper imports from earlier papers.
> Status: ✅ unconditional | ⚠️ conditional | 🔴 open/unproved | ❌ disproved/obstructed

---

## Overview

Papers I–IV form the Prolate–Weil subprogram.
Paper IV closes the bulk decorrelation step (`prob:pswf-weak-limit` of Paper III)
unconditionally. The bulk exponential tail bound itself remains conditional
on Assumption 2.4 (bulk convolution decay, Paper III). See Interface Analysis below.

```
Paper I → Paper II (companion) → Paper III → Paper IV
                ↑_______________________________↑
         (Paper II conjectures; Papers III–IV prove/disprove/reduce)
```

---

## Main Dependency Table

| Result exported | Source | Used by | Status |
|---|---|---|---|
| Frame coercivity under the DSTP | Paper I | Paper II, Paper III | ✅ |
| Implication framework (Conj. 3.1 + XRY → DSTP) | Paper II (quadrature) | — | ⚠️ conditional |
| `conj:pswf_product_tail`(i) bulk: exponential decay for `m,n ≤ γN` | Paper II (quadrature) | Paper III (target) | ⚠️ **bulk decorrelation closed by Paper IV; exponential tail bound conditional on Ass. 2.4** |
| `conj:pswf_product_tail`(ii) off-diagonal: algebraic decay `\|m-n\| ≥ δN` | Paper II (quadrature) | Paper III (target) | ⚠️ conditional on Paper III Ass. 3.1 |
| `conj:pswf_product_tail`(iii) global uniform bound over all `m,n ≤ N` | Paper II (quadrature) | — | ❌ **disproved** by Paper III `prop:bwdoubling` |
| Unconditional uniform bound `‖(I−P_N)f_{mn}‖ ≤ CT^{1/2}` | Paper III `thm:offdiag` | Paper II (quadrature) `prop:partial_compatibility`(a) | ✅ |
| Mean spectral localization `E_{mn}[χ_k] = μ_{mn} + E_{mn}` | Paper III `prop:mean-loc` | Paper II (quadrature) `rem:bottleneck` | ✅ |
| Exact IBP energy identity for commutator | Paper III `lem:ibp-exact` | Paper II (quadrature) `rem:bottleneck` | ✅ |
| Explicit energy formula for `E_{mn}` | Paper III `cor:emn-explicit` | Paper II (quadrature) `rem:bottleneck` | ✅ |
| Spectral lower bound `E_{mn}[χ_k] ≥ μ_{mn}/2` | Paper III `prop:spectral-lower` | Paper II (quadrature) `rem:bottleneck` | ✅ |
| Edge obstruction `E_out(f_{nn}) ≥ c₀ > 0` for `n ~ N` | Paper III `prop:bwdoubling` | Paper II (quadrature) `conj:pswf_product_tail`(iii) | ✅ **negative dependency** |
| Conditional algebraic decay `C_p(1+\|m-n\|)^{-p}` | Paper III `thm:offdiag-strong` | Paper II (quadrature) `prop:partial_compatibility`(b) | ⚠️ cond. on Paper III Ass. 3.1 |
| **`prob:pswf-weak-limit`: weak convergence of PSWF densities to ρ^cl, rate O(1/n)** | **Paper IV `thm:weak-limit`** | **Paper III `lem:bulk-reduction`** | **✅ proved unconditionally** |
| **Hypothesis (6.1) of Lemma 6.3 (Bulk Decorrelation Reduction)** | **Paper IV `cor:bulk-program-closed`** | **Paper III `lem:bulk-reduction`** | **✅ resolved** |
| Bulk exponential tail bound `‖(I−P_N)f_{mn}‖ ≤ C e^{−αN}` for `m,n ≤ γN` | Paper III (via Paper IV) | Paper II (quadrature) bulk conjecture | ⚠️ **conditional on Ass. 2.4 of Paper III** |

**Key negative dependency (unusual, document explicitly):**
Paper III `prop:bwdoubling` proves that Paper II (quadrature)
`conj:pswf_product_tail`(iii) is false as stated.
Paper II (quadrature) has been revised accordingly:
`conj:pswf_product_tail` is now split into a proved bulk/off-diagonal part
and a documented edge obstruction. The conditional implication
is now restricted to the bulk regime `m,n ≤ γN`.

**Paper IV dependency summary:**

Paper IV imports:
- ORX Ch.4 Prop.4.2 (exponential concentration): used in `lem:turning-point-cutoff`
- Slepian 1978 Eq.(4.3) (integral formula for λ_n): used in `lem:bohr-sommerfeld-pswf`
- Levitan–Sargsjan (Prüfer theory): used in `lem:prufer-ode`
- Paper III Section 2 conventions (D_c, λ_n, χ_n notation)
- Paper III Lemma 6.3 (`lem:bulk-reduction`): Paper IV *supplies* its hypothesis (6.1)

Paper IV exports:
- `thm:weak-limit`: `∫f ψ_n² = λ_n ∫f ρ_n^cl + O(λ_n ‖f‖_{C¹}/n)`, for `f ∈ C¹`, `n ≤ γN`
- `lem:prufer-oscillation-control`: `|∫h cos(2θ_n)| = O(‖h‖_{C¹}/n)` if `θ_n' ≳ n`
- `lem:amplitude-drift`: `r_n²/r_n^{WKB,2} = 1 + O(1/n)` (drift cancellation identity)
- `lem:normalization`: `r_n^{WKB,2}/2 = λ_n ρ^cl · (1+O(1/n))`

---

## Interface Analysis: Papers II ↔ III ↔ IV

### Interface tension 1 (surviving): Paper III Assumption 2.4

The bulk tail bound
`‖(I−P_N)f_{mn}‖ ≤ C e^{−αN}` for `m,n ≤ γN`
is proved by the chain:

```
Paper IV thm:weak-limit
  → Paper III lem:bulk-reduction (Lemma 6.3)    [closed unconditionally by Paper IV]
  → Paper III prob:comm-refined
  → Bulk tail bound                             [still needs Assumption 2.4]
```

**What Assumption 2.4 says:** For the product functions `f_{mn} = ψ_m ψ_n`
with `m,n ≤ γN`, the out-of-band Fourier energy satisfies
`E_out(f_{mn}) ≤ C e^{−α c}` (exponential convolution decay).

**Why it is not yet proved:** It requires a uniform bound on the Fourier
convolution `ψ̂_m * ψ̂_n` outside `[−ω, ω]` — essentially quantitative
control of the tail of the product's Fourier transform, uniform in `m,n ≤ γN`.
This is a Fourier-side statement; Paper IV's equidistribution is a
time-domain statement. They are related but not identical.
Evidence: ORX Ch.6 gives pointwise Fourier decay for individual PSWFs
near the band edge; the convolution stability for products is the gap.

**What Paper IV closes (precisely):** The weak-convergence step
`prob:pswf-weak-limit` — i.e., the *time-domain* energy equidistribution
needed for the decorrelation lemma. This is now unconditional.
Assumption 2.4 is a *Fourier-side* statement and is not touched by Paper IV.

**Severity:** Medium. The chain `IV → III lem:bulk-reduction → decorrelation`
is clean and unconditional. The single remaining gap is Ass. 2.4.
Three proof strategies are documented in `assumption_2_4_target.md`;
Variant A (Schur test on the product kernel) is the recommended next step.

### Interface tension 2 (surviving): Paper III Assumption 3.1

The off-diagonal algebraic decay result
(`thm:offdiag-strong`, `|m-n| ≥ δN`)
remains conditional on **Paper III Assumption 3.1 (pointwise spectral localization)**:

`|a_k^{mn}| ≤ C_p / (1 + |χ_k(c) − μ_{mn}|)^p` for `k ≥ N`.

**Why it is not yet proved:** Paper IV's Prüfer analysis gives `θ_n' ≳ n`
for a single index `n` in the bulk. For the off-diagonal case one needs
control of `(θ_m − θ_n)'`, which depends on `χ_m − χ_n` and the relative
positions of both turning points `x_+(m)` and `x_+(n)`. When `|m-n| ≥ δN`,
these turning points are well-separated, and heuristically the phase
difference oscillates at rate `|m-n|`, giving algebraic decay `O(1/|m-n|)`.
But this is *not* directly covered by Paper IV's single-index analysis.

**Severity:** Medium-low for the core program (bulk is fully unconditional
modulo Ass. 2.4; off-diagonal is a strengthening). Higher if one wants
the full uniform bound of Paper II (quadrature).

### Interface tension 3 (closed by Paper IV)

The energy equidistribution
`A_{mn} + B_{mn} ≈ μ_{mn}/2` (`prob:comm-refined` of Paper III)
was the central open problem of Paper III.
It is now closed:
- Paper IV `thm:weak-limit` supplies `prob:pswf-weak-limit` with rate O(1/n)
- Paper III `lem:bulk-reduction` converts this to `prob:comm-refined`
- No additional assumptions are needed (within the bulk regime `m,n ≤ γN`)

> **Status: fully resolved for m,n ≤ γN.**

### Robustness verdict: I ↔ II ↔ III ↔ IV

| Interface | Nature | Status | Severity |
|---|---|---|---|
| IV → III `lem:bulk-reduction` | Paper IV supplies hypothesis (6.1) | ✅ clean | — |
| III → II (quadrature) bulk conjecture | Via Paper IV chain; cond. on Ass. 2.4 | ⚠️ one gap remains | Medium |
| III off-diagonal → II (quadrature) | `thm:offdiag-strong` cond. on Ass. 3.1 | ⚠️ conditional | Medium-low |
| II → I (frame coercivity) | Scaling limit; conditional on prime DSTP | ⚠️ inherits open problem | Low (program level) |

**The program is "closed under composition" for the bulk regime modulo Ass. 2.4.**
For the full program (off-diagonal and edge), two assumptions survive as
genuine open problems — neither circular, neither trivial.

---

## Summary: What is unconditionally proved (April 2026)

- Frame coercivity under DSTP: explicit spectral stability bounds (Paper I) ✅
- Exact algebraic defect decomposition `E_mn = R_mn^quad` (Paper I) ✅
- DSTP verified for random and Gauss–PSWF sampling (Paper I) ✅
- Compactness of normalized Gram operators in the scaling limit (Paper II) ✅
- Trace formula: weighted Gram matrix asymptotics consistent with PNT (Paper II) ✅
- Uniform off-diagonal bound `‖(I−P_N)f_{mn}‖ ≤ CT^{1/2}` (Paper III) ✅
- Mean spectral localization `E_{mn}[χ_k] = μ_{mn} + E_{mn}` (Paper III) ✅
- Exact energy decomposition: explicit positive functional for `E_{mn}` (Paper III) ✅
- Spectral lower bound `E_{mn}[χ_k] ≥ μ_{mn}/2` (Paper III) ✅
- Edge obstruction: global uniform tail bound is false for `m,n ~ N` (Paper III) ✅
- **Weak convergence of PSWF densities: `∫f ψ_n² = λ_n ∫f ρ^cl + O(λ_n ‖f‖_{C¹}/n)` (Paper IV) ✅**
- **Drift cancellation identity: `log(r_n/r_n^{WKB}) = ∫ G cos(2θ_n)` (Paper IV) ✅**
- **Amplitude drift control: `r_n²/r_n^{WKB,2} = 1 + O(1/n)` uniformly (Paper IV) ✅**
- **Bulk decorrelation reduction fully supplied: hypothesis (6.1) of Lemma 6.3 (Paper IV → III) ✅**

## Summary: What remains conditional or open (April 2026)

- DSTP for prime sampling (Paper I open problem) 🔴
- **Bulk tail bound (unconditional):** needs Paper III Ass. 2.4 (bulk convolution decay) 🔴
- Off-diagonal algebraic decay: conditional on Paper III Ass. 3.1 ⚠️
- XRY stability conjecture (Paper II quadrature) 🔴
- Identification of `G_∞` as Weil operator (Paper II) 🔴
- Uniqueness and `tr(G_∞) = 1` (Paper II) 🔴
- Edge regime analysis `m,n ~ N`: requires Airy-scale methods (Papers II quad, III) 🔴
- Paper IV P1: `C⁰` extension of `thm:weak-limit` 🟡 (partial: rate-free via density)
- Paper IV P2: off-diagonal analogue of `thm:weak-limit` for `ψ_m ψ_n`, `m ≠ n` 🔴
- Paper IV P5: near-critical regime `n ~ γN` (Airy-scale needed) 🔴
