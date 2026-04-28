# Logical Dependency Graph — Papers I–XVII + Paper IV

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
| Frame coercivity under Assumption 3.10 | Paper I | Paper II, Paper III | ✅ |
| Implication framework (Conj. 3.1 + XRY → Ass. 3.10) | Paper II | — | ⚠️ conditional |
| `conj:pswf_product_tail`(i) bulk: exponential decay for `m,n ≤ γN` | Paper II | Paper III (target) | ✅ **resolved by Paper IV** |
| `conj:pswf_product_tail`(ii) off-diagonal: algebraic decay `\|m-n\| ≥ δN` | Paper II | Paper III (target) | ⚠️ conditional on Paper III Ass. 3.1 |
| `conj:pswf_product_tail`(iii) global uniform bound over all `m,n ≤ N` | Paper II | — | ❌ **disproved** by Paper III `prop:bwdoubling` |
| Unconditional uniform bound `\|(I-P_N)f_{mn}\| ≤ CT^{1/2}` | Paper III `thm:offdiag` | Paper II `prop:partial_compatibility`(a) | ✅ |
| Mean spectral localization `E_{mn}[χ_k] = μ_{mn} + E_{mn}` | Paper III `prop:mean-loc` | Paper II `rem:bottleneck` | ✅ |
| Exact IBP energy identity for commutator | Paper III `lem:ibp-exact` | Paper II `rem:bottleneck` | ✅ |
| Explicit energy formula for `E_{mn}` | Paper III `cor:emn-explicit` | Paper II `rem:bottleneck` | ✅ |
| Spectral lower bound `E_{mn}[χ_k] ≥ μ_{mn}/2` | Paper III `prop:spectral-lower` | Paper II `rem:bottleneck` | ✅ |
| Edge obstruction `E_out(f_{nn}) ≥ c₀ > 0` for `n ~ N` | Paper III `prop:bwdoubling` | Paper II `conj:pswf_product_tail`(iii) | ✅ **negative dependency** |
| Conditional algebraic decay `C_p(1+\|m-n\|)^{-p}` | Paper III `thm:offdiag-strong` | Paper II `prop:partial_compatibility`(b) | ⚠️ cond. on Paper III Ass. 3.1 |
| **`prob:pswf-weak-limit`: weak convergence of PSWF densities** | **Paper IV `thm:weak-limit`** | **Paper III `lem:bulk-reduction`** | **✅ proved** |
| **Energy equidistribution `A_{mn}+B_{mn} ≈ μ_{mn}/2`** | **Paper IV `cor:bulk-program-closed`** | **Paper III `prob:comm-refined`** | **✅ resolved** |
| Bulk exponential tail bound `\|(I-P_N)f_{mn}\| ≤ C e^{-αN}` for `m,n ≤ γN` | Paper III (via Paper IV) | Paper II bulk conjecture | ✅ cond. on Paper II Ass. 2.4 |

**Key negative dependency (unusual, document explicitly):**
Paper III `prop:bwdoubling` proves that Paper II `conj:pswf_product_tail`(iii)
is false as stated. Paper II has been revised accordingly:
`conj:pswf_product_tail` is now split into a proved bulk/off-diagonal part
and a documented edge obstruction. The conditional implication of Paper II
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
> but not yet a theorem.

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
> High if one wants the full uniform bound of Paper II.

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
| III → II bulk conjecture | Via Paper IV chain | ✅ cond. on Ass. 2.4 | Medium |
| III off-diagonal → II | `thm:offdiag-strong` | ⚠️ cond. on Paper III Ass. 3.1 | Medium-low |
| IV → I (frame coercivity) | Indirect, via II | ⚠️ inherits II conditionals | Low |

**The program is "closed under composition" for the bulk regime.**
For the full program (including off-diagonal and edge), two assumptions
survive as genuine open problems — neither circular, neither trivial.

---

## Layer 1: Asymptotic Analysis (Papers I–VIII)

```
I  → II → III → IV → V
               ↓
              VI  →  VII  →  VIII
               ↑_______↑
         (VI uses VII as companion — must be declared explicitly)
```

| Result exported | Source | Used by | Status |
|---|---|---|---|
| Coercivity constant `~ c^{-1/2}` | I | II, III | ✅ |
| Gram → Id (scaling limit) | II | III, IX | ⚠️ weak-* only |
| Peak location `t_* ~ c^{1/2}` | III | VI, VII, VIII | ✅ |
| Pointwise decay `\|Φ̂\| ≤ C c^{-1/4} t^{-1/4}` | VI | VIII | ⚠️ depends on VII |
| Airy profile `(1+O(c^{-1/3}))` | VI | VII, VIII, XVI | ✅ (after fix) |
| Peak width upper bound `Δ_ε ≤ C c^{-1/2}` | VII | VIII | ✅ |
| Non-cancellation + lower bound `Δ_ε ≳ c^{-1/2}` | VIII | — | ✅ |
| Rate `\|λ_n^(c) - λ_n^(∞)\| ≤ C c^{-1/4}` | VIII Cor 4.3 | IX, X, XI, XII | ✅ |
| `\|κ_n^(c)\| ≥ c_κ > 0` | VIII | XVI | ✅ |

⚠️ **VI→VII dependency:** Paper VI Theorem 1 (pointwise bound) defers full proof to Paper VII.
Paper VII must be declared as a companion preprint whenever Paper VI is submitted.

---

## Layer 2: Functional Analysis (Papers IX–XIII)

```
VIII → IX → X → XI → XII → XIII
```

| Result exported | Source | Used by | Status |
|---|---|---|---|
| PSWF precompactness | IX Lem 3.1 | X, XI | ✅ |
| `\|Φ_n^(∞)\| = 1` | IX Prop 2.2 | XI | ✅ |
| `H_spec` closable & symmetric | IX Thm 3.3 | X | ✅ |
| SOT-limit `H_lim` exists | X Thread A | XI, XII | ✅ |
| Mosco `q_c →^M q_lim` | X Thread B | X Thm Friedrichs | ✅ |
| `T_{q_lim} = H_str` | X Thm Friedrichs | — | ✅ |
| Strong resolvent convergence | X Cor resolvent | XI | ✅ |
| Bridge: `H_str = closure(H_spec)` | X Thm bridge | XII | ⚠️ conditional on Hyp.(IX.b) |
| `H_lim Φ_n^(∞) = λ_n^(∞) Φ_n^(∞)` | XI Lem eigenvalue-eq | XII | ✅ (along c_k) |
| Spectral inclusion `{λ_n^(∞)} ⊂ σ(H_lim)` | XI Thm spectral-inclusion | XII | ✅ (along c_k) |
| Localization principle (abstract) | XII Thm mechanism | — | ✅ |

🔴 **Central open problem:** `H_SOT = closure(H_spec)` — not proved anywhere in series.
🔴 **All XI results hold only along fixed diagonal subsequence c_k** — subsequence-independence open.

---

## Layer 3: Microlocal Analysis (Papers XIV–XVII + fold_model)

```
XV → fold_model → XVI → XVII
 XIV ↗
```

| Result exported | Source | Used by | Status |
|---|---|---|---|
| HS decomposition Σ_near + Σ_int + Σ_far | XIV | XV | ✅ cond. on (C) |
| `Σ_near = O(1/c)` | XIV | XV | ✅ |
| `theta''(0)=0`, `theta'''(0)≠0` (cubic non-deg.) | XV Lem 4.2 | XVI | ✅ |
| `Σ_model(c) = o(1)` | XV Cor 5.3 | — | ✅ (given theta non-deg.) |
| Universal fold bound `\|Φ_α(u)\| = O(\|u\|^{-1/2})` | fold_model | XVI | ✅ |
| CFU phase-diagram (α < 1/2 / α = 1/2 / α > 1/2) | fold_model | XVI | ✅ |
| Airy normal form (microlocal, cond.) | XVI Thm airy-normalform | XVII | ⚠️ cond. on (i)–(vi) |
| Pointwise `\|Φ(u;c)\| ≤ C(1+\|u\|)^{-3/4}` | XVI Cor pointwise | XVII | ⚠️ cond. on (i)–(vi) |
| Cesàro `O(U^{1/4})` | XVI Cor global-bound | XVII | ⚠️ cond. on (i)–(vi) |
| A₂-stability Assumption 4.1(vi) for PSWF | XVII (target) | XVI (closes) | 🔴 OPEN |
| Explicit period `T(λ_n)` for `V(x)=x²/(1-x²)` | XVIII-A (planned) | XVII | 🔴 OPEN |
| CFU-Jacobian ellipticity lemma | XVIII-B (planned) | XVI, XVII | 🔴 OPEN |

🔴 **Remaining open problems in Layer 3:**
- Prob. 6.1 (Paper XV): Lipschitz regularity of PSWF amplitude
- Prob. 7.1 (Paper XV): Local Weyl law (C)
- prob:PSWF-microlocal (Paper XVI): Verify Assumption 4.1(vi) for PSWF uniformly in c

---

## Summary: What is unconditionally proved

- Sharp peak width: `Δ_ε(c,n) ≍ c^{-1/2}` (Papers VI–VIII) ✅
- SOT-limit operator exists: `H_lim` bounded self-adjoint (Paper X) ✅
- Eigenvalue rate: `|λ_n^(c) - λ_n^(∞)| ≤ C c^{-1/4}` (Paper VIII Cor 4.3) ✅
- `Σ_model(c) = o(1)` (Paper XV) ✅
- Endpoint decay `|Φ(u;c)| = O(|u|^{-1/2})` (Paper XVI Thm endpoint) ✅
- Abstract localization principle (Paper XII) ✅
- Uniform off-diagonal bound `\|(I-P_N)f_{mn}\| ≤ CT^{1/2}` (Paper III) ✅
- Mean spectral localization `E_{mn}[χ_k] = μ_{mn} + E_{mn}` (Paper III) ✅
- Spectral lower bound `E_{mn}[χ_k] ≥ μ_{mn}/2` (Paper III) ✅
- Edge obstruction: global uniform tail bound is false for `m,n ~ N` (Paper III) ✅
- **Weak convergence of PSWF densities: ∫f ψ_n² → λ_n ∫f ρ_n^cl, rate O(1/n) (Paper IV) ✅**
- **Energy equidistribution A_{mn}+B_{mn} ≈ μ_{mn}/2 for m,n ≤ γN (Paper IV→III) ✅**
- **Bulk exponential tail bound ‖(I-P_N)f_{mn}‖ ≤ Ce^{-αN}, m,n ≤ γN (Paper III via IV, cond. on II Ass. 2.4) ⚠️**

## Summary: What remains conditional or open

- **Bulk tail bound (unconditional):** needs Paper II Ass. 2.4 (bulk convolution decay) 🔴
- Off-diagonal algebraic decay (conditional on Paper III Ass. 3.1) ⚠️
- Bridge Theorem `H_SOT = closure(H_spec)` 🔴
- Airy normal form uniform in c (conditional on Assumption 4.1) ⚠️
- Uniform CFU Jacobian for PSWF (Paper XVII target) 🔴
- All spectral completeness / uniqueness / gap questions 🔴
- Paper IV P1: C⁰ extension of thm:weak-limit 🔴 (non-critical)
- Paper IV P2: off-diagonal analogue of thm:weak-limit 🔴 (future work)
