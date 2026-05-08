# Review Notes: Paper XVIII — Airy Kernel Universality (v20)

**Date:** May 2026  
**File:** `paper18_airy_universality.tex`  
**Current version:** v20 (commit `1bfd8ed`)  
**Status:** Structurally closed at proof-sketch level. One minor open point (see §4).

---

## 1. Verified Argument Map (v20)

The proof of Main Lemma (pointwise `K_{B_c}(ξ,ξ') → K_A(ξ,ξ')`) has four steps:

| Step | Content | Key tool | Status |
|------|---------|----------|--------|
| 1 | Fermi tail control | XVII Lem. 2.1 + Lem. I2b | ✓ |
| 2 | Projector convergence | Cor. spectral (i–iii), norm-resolvent | ✓ |
| 3 | Fixed-K limit (c→∞) | Lem. H2 (C⁰ convergence, Langer) | ✓ |
| 4 | K→∞ limit | Lem. slepianunif + Rem. dct + Rem. iterated | ✓ |

### Core sub-arguments

**L¹ diagonal of K_A** (Prop. 1.3b):  
`K_A(ξ,ξ) = ∫₀^∞ Ai(ξ+s)² ds ≤ C'(1+ξ)^{-1/2}`  
via `|Ai(t)| ≤ C(1+t)^{-1/4} exp(-2/3 t^{3/2})` (Olver Ch. 11).  
→ **Direct Lebesgue integral. No semigroup, no trace of identity.**

**Parseval identification** (Prop. 1.3c):  
`K_A(ξ,ξ) = Σ_k u_k(ξ)²` a.e., convergence in L¹([0,M])  
via Bessel's inequality + DCT with dominant `(1+ξ)^{-1/2}`.  
→ **No ONB assumption on restrictions u_k|_{[0,M]}.**

**DCT Layer 2** (Rem. dct):  
Dominating function `h(ξ,ξ') = [K_A(ξ,ξ)·K_A(ξ',ξ')]^{1/2}`.  
- `h ∈ L¹([0,M]²)` via Tonelli + L¹ diagonal (holds **only on [0,M]², not globally on ℝ₊²** — stated explicitly in v20).  
- Pointwise convergence: Parseval for complete ONS {u_k} in L²(ℝ₊).  
- Conclusion: S_K → K_A in L¹([0,M]²) and a.e. via Lebesgue DCT.  
→ **No tr(Id_{[0,M]}), no HS-norm of full kernel, no Mercer monotonicity.**

**Uniform-in-c spectral tail** (Lem. slepianunif):  
`sup_{c≥c₁} Σ_{j>K₀} λ_{n*+j}^{(c)} < ε`  
via exponential transition-window decay (Slepian 1978 Thm. 1 + ORX §4.2),  
**not** a factorial bound.  
Geometric series with rate `exp(-c₁^{2/3} γ₀)`.

**Iterated limit** (Rem. iterated):  
Order: c→∞ first (fixed K), then K→∞.  
ε-chain: choose K₀=K₀(ε) from slepianunif (uniform in c≥c₁), then c₀=c₀(K₀,M) from Langer.  
→ **No joint uniformity claimed or needed.**

---

## 2. Errors Fixed Across v13–v20

| Version | Error | Fix |
|---------|-------|-----|
| v13–v14 | Pointwise potential comparison (local instability) | Global form comparison via Kato VI.2.21 (v15) |
| v14 | Fragile L¹ embedding for H⁻¹ | H⁻¹ = (H¹₀)* + Morrey n=1 duality (v15) |
| v14 | Missing DCT uniformity | L∞ via H² + Rellich–Kondrachov (v15) |
| v16 | Implicit coercivity/spectral confusion | Explicit separation: Rem. coercep (v16) |
| v16–v17 | Mercer monotonicity (needs kernel positivity) | CS-diagonal bound + Tonelli (v17) |
| v17 | Uniformity chain implicit | Explicit K→C_K→δ₀→c₀ chain (v17) |
| v18 | tr(Id_{[0,M]}) < ∞ (WRONG: identity not trace-class) | Removed entirely; replaced by Airy integral (v20) |
| v18–v19 | Semigroup t↓0 limit (not justified pointwise) | Dropped; direct Airy integral used (v20) |
| v19 | Factorial Slepian bound (not in references) | Exponential window from Slepian 1978 Thm. 1 (v20) |
| v19 | HS-norm convergence claim for full kernel | Replaced by CS + Tonelli on [0,M]² only (v20) |

---

## 3. What Is Structurally Sound in v20

- ✓ Global form comparison (Kato VI.2.21), no local instability  
- ✓ H⁻¹ control via H¹₀–L∞ duality (Morrey, n=1)  
- ✓ Uniform L∞ via H² + Rellich–Kondrachov  
- ✓ Langer approximation on c^{-2/3} window, error O(c^{-1/3}), uniform in j≤K  
- ✓ Uniformity chain K→C_K→δ₀(K)→c₀(K,M) explicit  
- ✓ Spectral convergence ≠ coercivity (two separate layers)  
- ✓ L¹ diagonal direct from Airy integral, no semigroup  
- ✓ DCT with h ∈ L¹([0,M]²), explicit domain restriction  
- ✓ Uniform-in-c tail via exponential Slepian window  
- ✓ Iterated limit with explicit ε-chain  
- ✓ Poset DAG with internal/external split, no directed cycle  

---

## 4. One Genuine Open Point

**Slepian regime assumption in Lem. slepianunif:**

The bound `λ_{n_c+k}^{(c)} ≤ 2 exp(-c γ(k/c^{1/3}))` uses `γ₀ = min_{s∈[1,2]} γ(s)`, which implicitly assumes `k/c^{1/3} ∈ [1,2]` for the relevant summation range.

This is a regime assumption: it requires `c^{1/3} ≤ k ≤ 2c^{1/3}`.  
For `k > 2c^{1/3}` the eigenvalues are already super-exponentially small (deeper in the tail), so the bound only gets stronger — but this should be stated explicitly.

**Minimal fix (one sentence):** Split the sum at `k = 2c^{1/3}`:  
- For `K₀ ≤ k ≤ 2c^{1/3}`: use exponential window with γ₀.  
- For `k > 2c^{1/3}`: eigenvalues satisfy `λ < exp(-Cc^{1/3})` (deep tail, Slepian 1978 §5), which is summable and negligible for large c.

This closes the regime gap and is **not a structural error**, only a missing case split.

---

## 5. Review Loop Warning

Reviewers (human or AI) should verify objections **against the current file**, not against earlier versions.  
Several objections raised against v18/v19 described errors that had already been fixed in v20.  
Baseline for any future review: **v20 = commit `1bfd8ed`**.

The argument structure is: **Airy decay → L¹ diagonal → CS domination → DCT on [0,M]² → iterated limit.**  
All intermediate functional-analytic bridges are explicit and self-contained.
