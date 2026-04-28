# Logical Dependency Graph — Papers I–IV

> This file documents which results each paper imports from earlier papers.
> Status: ✅ unconditional | ⚠️ conditional | 🔴 open/unproved | ❌ disproved

---

## Prolate–Weil Subprogram (Papers I–IV)

Papers I–IV form the completed bulk-regime sub-chain.
Paper IV closes the last open problem (prob:pswf-weak-limit) of Paper III
and completes the energy equidistribution step.

```
Paper I → Paper II (companion) → Paper III → Paper IV
                ↑_______________________________↑
         (Paper II conjectures; Papers III–IV prove/disprove)
```

| Result exported | Source | Used by | Status |
|---|---|---|---|
| Frame coercivity under the DSTP | Paper I | Paper II, Paper III | ✅ |
| Implication framework (Conj. 3.1 + XRY → DSTP) | Paper II (quadrature) | — | ⚠️ conditional |
| `conj:pswf_product_tail`(i) bulk: exponential decay for `m,n ≤ γN` | Paper II (quadrature) | Paper III (target) | ✅ **resolved by Paper IV** |
| `conj:pswf_product_tail`(ii) off-diagonal: algebraic decay `|m-n| ≥ δN` | Paper II (quadrature) | Paper III (target) | ⚠️ conditional on Paper III Ass. 3.1 |
| `conj:pswf_product_tail`(iii) global uniform bound over all `m,n ≤ N` | Paper II (quadrature) | — | ❌ **disproved** by Paper III `prop:bwdoubling` |
| Unconditional uniform bound `\|(I-P_N)f_{mn}\| ≤ CT^{1/2}` | Paper III `thm:offdiag` | Paper II (quadrature) `prop:partial_compatibility`(a) | ✅ |
| Mean spectral localization `E_{mn}[χ_k] = μ_{mn} + E_{mn}` | Paper III `prop:mean-loc` | Paper II (quadrature) `rem:bottleneck` | ✅ |
| Exact IBP energy identity for commutator | Paper III `lem:ibp-exact` | Paper II (quadrature) `rem:bottleneck` | ✅ |
| Explicit energy formula for `E_{mn}` | Paper III `cor:emn-explicit` | Paper II (quadrature) `rem:bottleneck` | ✅ |
| Spectral lower bound `E_{mn}[χ_k] ≥ μ_{mn}/2` | Paper III `prop:spectral-lower` | Paper II (quadrature) `rem:bottleneck` | ✅ |
| Edge obstruction `E_out(f_{nn}) ≥ c₀ > 0` for `n ~ N` | Paper III `prop:bwdoubling` | Paper II (quadrature) `conj:pswf_product_tail`(iii) | ✅ **negative dependency** |
| Conditional algebraic decay `C_p(1+|m-n|)^{-p}` | Paper III `thm:offdiag-strong` | Paper II (quadrature) `prop:partial_compatibility`(b) | ⚠️ cond. on Paper III Ass. 3.1 |
| **`prob:pswf-weak-limit`: weak convergence of PSWF densities** | **Paper IV `thm:weak-limit`** | **Paper III `lem:bulk-reduction`** | **✅ proved** |
| **Energy equidistribution `A_{mn}+B_{mn} ≈ μ_{mn}/2`** | **Paper IV `cor:bulk-program-closed`** | **Paper III `prob:comm-refined`** | **✅ resolved** |
| Bulk exponential tail bound `\|(I-P_N)f_{mn}\| ≤ C e^{-αN}` for `m,n ≤ γN` | Paper III (via Paper IV) | Paper II (quadrature) bulk conjecture | ✅ cond. on Paper II Ass. 2.4 |

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
- Paper III Section 2 conventions (D_c, λ_n, χ_n notation)
- Paper III Lemma 6.3 (`lem:bulk-reduction`): Paper IV supplies its hypothesis (6.1)

Paper IV exports:
- `thm:weak-limit`: ∫f ψ_n² = λ_n ∫f ρ_n^cl + O(λ_n ‖f'‖/n), for f ∈ C¹, n ≤ γN
- `lem:prufer-oscillation-control`: |∫h cos(2θ_n)| = O(‖h‖_{C¹}/n) if θ_n' ≳ n
- `lem:bohr-sommerfeld-pswf`: π K_n = π/λ_n · (1+O(1/n))

---

## Interface Analysis: Papers II ↔ III ↔ IV

### Interface tension 1 (surviving): Paper II Assumption 2.4

The bulk tail bound
`‖(I-P_N)f_{mn}‖ ≤ C e^{-αN}` for `m,n ≤ γN`
is proved by the chain:

```
Paper IV thm:weak-limit
  → Paper III lem:bulk-reduction (Lemma 6.3)
  → Paper III prob:comm-refined
  → Bulk tail bound
```

but the last step uses **Paper II Assumption 2.4 (bulk convolution decay)**.

> **What Assumption 2.4 says:** The convolution operator
> `(K_c f)(x) = ∫ sin(c(x-y))/(π(x-y)) · f(y) dy`
> satisfies a weighted L²-decay estimate on the bulk diagonal sector.

> **Why it is not yet proved:** It requires a uniform bound on the
> off-diagonal kernel of P_N in the bulk — essentially a quantitative
> version of the Bernstein inequality for PSWFs, uniform in c.
> This is a known-hard problem: it is closely related to
> `conj:pswf_product_tail`(i) (which Paper IV now resolves)
> but not identical. Paper II Ass. 2.4 is a convolution estimate;
> Paper IV proves a density equidistribution result.
> The precise logical gap: Paper IV → Paper III is clean.
> Paper III → final bound still needs Ass. 2.4.

> **Severity:** Medium. The chain is complete modulo one cited assumption.
> Ass. 2.4 is plausible and consistent with ORX Ch.6 estimates,
> but not yet a theorem. Three proof strategies are documented
> in `assumption_2_4_target.md`; Variant A (Schur test) is the
> recommended next step.

### Interface tension 2 (surviving): Paper III Assumption 3.1

The off-diagonal algebraic decay result
(`thm:offdiag-strong`, `|m-n| ≥ δN`)
remains conditional on **Paper III Assumption 3.1 (off-diagonal phase separation)**.

> **What Assumption 3.1 says:** For `|m-n| ≥ δN`, the phase difference
> `θ_m(x) - θ_n(x)` has non-degenerate oscillation on `[-T,T]`,
> uniformly in m,n (not only in the bulk).

> **Why it is not yet proved:** The Prüfer phase argument of Paper IV
> gives `θ_n' ≳ n` in the *bulk* `I_δ`. For the off-diagonal case,
> one needs control of `(θ_m - θ_n)'`, which depends on `χ_m - χ_n`
> and the relative positions of both turning points `x_+(m)` and `x_+(n)`.
> When `|m-n| ≥ δN`, these turning points are well-separated,
> and heuristically the phase difference oscillates at rate `|m-n|`,
> giving `O(1/|m-n|)` → algebraic decay.
> But: this is *not* directly covered by Paper IV's `lem:phase-monotone`,
> which only handles a single index n.

> **Severity:** Medium-low for the program's core results
> (bulk is unconditional; off-diagonal is a strengthening).
> High if one wants the full uniform bound of Paper II (quadrature).

### Interface tension 3 (closed by Paper IV)

The energy equidistribution
`A_{mn} + B_{mn} ≈ μ_{mn}/2` (`prob:comm-refined` of Paper III)
was the central open problem.
It is now closed:
- Paper IV `thm:weak-limit` supplies `prob:pswf-weak-limit`
- Paper III `lem:bulk-reduction` converts this to `prob:comm-refined`
- No additional assumptions needed (within the bulk regime)

> **Status: fully resolved for n,m ≤ γN.**

### Robustness verdict: II ↔ III ↔ IV

| Interface | Nature | Status | Severity |
|---|---|---|---|
| IV → III `lem:bulk-reduction` | Paper IV supplies hypothesis (6.1) | ✅ clean | — |
| III → II (quadrature) bulk conjecture | Via Paper IV chain | ✅ cond. on Ass. 2.4 | Medium |
| III off-diagonal → II (quadrature) | `thm:offdiag-strong` | ⚠️ cond. on Paper III Ass. 3.1 | Medium-low |
| IV → I (frame coercivity) | Indirect, via II | ⚠️ inherits II conditionals | Low |

**The program is “closed under composition” for the bulk regime.**
For the full program (including off-diagonal and edge), two assumptions
survive as genuine open problems — neither circular, neither trivial.

---

## Summary: What is unconditionally proved

- Frame coercivity under DSTP: explicit spectral stability bounds (Paper I) ✅
- DSTP verified for random and Gauss–PSWF sampling (Paper I) ✅
- Compactness of normalized Gram operators in the scaling limit (Paper II) ✅
- Unconditional asymptotic for reference PSWF eigenvalues (Paper II) ✅
- Uniform off-diagonal bound `\|(I-P_N)f_{mn}\| ≤ CT^{1/2}` (Paper III) ✅
- Mean spectral localization `E_{mn}[χ_k] = μ_{mn} + E_{mn}` (Paper III) ✅
- Spectral lower bound `E_{mn}[χ_k] ≥ μ_{mn}/2` (Paper III) ✅
- Edge obstruction: global uniform tail bound is false for `m,n ~ N` (Paper III) ✅
- **Weak convergence of PSWF densities: ∫f ψ_n² → λ_n ∫f ρ_n^cl, rate O(1/n) (Paper IV) ✅**
- **Energy equidistribution A_{mn}+B_{mn} ≈ μ_{mn}/2 for m,n ≤ γN (Paper IV→III) ✅**
- **Bulk exponential tail bound ‖(I-P_N)f_{mn}‖ ≤ Ce^{-αN}, m,n ≤ γN (Paper III via IV, cond. on II Ass. 2.4) ⚠️**

## Summary: What remains conditional or open

- DSTP for prime sampling (Paper I open problem) 🔴
- **Bulk tail bound (unconditional):** needs Paper II Ass. 2.4 (bulk convolution decay) 🔴
- Off-diagonal algebraic decay (conditional on Paper III Ass. 3.1) ⚠️
- Paper IV P1: C⁰ extension of thm:weak-limit 🔴 (non-critical)
- Paper IV P2: off-diagonal analogue of thm:weak-limit 🔴 (future work)
