# Context Summary — Prolate–Weil Program (Papers I–IV)

> **Purpose:** Paste this at the top of any new AI chat before working on this project.
> Provides the full logical chain without needing Papers I–IV in full.
> **Repo:** `Waschtl904/prolate-gram-coercivity`
> **Last updated:** April 30, 2026 — after full read-through and review of all four papers,
> and after update of `README.md`, `DEPENDENCIES.md`, `assumption_2_4_target.md`.

---

## Overarching Goal

The **Prolate–Weil Program** seeks a spectral realization of the **Weil positivity criterion**
via the PSWF concentration operator and its associated Gram forms.
The four papers build an explicit implication chain toward this goal,
with full rigor about what is proved, what is conditional, and what remains open.

**No claim about zeros of ζ(s) is made in any of the four papers.**

---

## The Four Papers

| File | Title (short) | Status |
|---|---|---|
| `paper1.tex` | Gram Form Coercivity + DSTP | Near publication-ready |
| `paper2.tex` | Scaling Limits, Trace Formula, Weil Connection | Near publication-ready |
| `paper2_quadrature.tex` | XRY Quadrature Implication Framework | Implication framework (conditional) |
| `paper3.tex` | PSWF Product Spectral Tail Estimates | Core analytic paper |
| `paper4_semiclassical.tex` | Semiclassical Equidistribution of PSWF Densities | Complete — fully proved |

---

## Overarching Logic Chain

```
Paper I (Gram coercivity, DSTP axiom)
  ↓
Paper II (Scaling limits, trace formula, Weil connection)
  ↓
Paper II_quadrature (Implication: Conj.(i)+(ii) → DSTP for XRY)
  ↓
Paper III (PSWF product tail bounds: bulk, off-diagonal, edge obstruction)
  ↓
Paper IV (Semiclassical equidistribution of ψ_n², rate O(1/n))
  ↑
  └── Paper IV closes prob:pswf-weak-limit from Paper III unconditionally
      Remaining gap: Assumption 2.4 (Fourier-side, see assumption_2_4_target.md)
```

---

## Central Notation

| Symbol | Meaning |
|---|---|
| `ψ_n^(c)` | PSWF on [-T,T] with bandwidth ω, time-bandwidth c = ωT |
| `λ_n(c)` | Slepian concentration eigenvalue: `‖ψ_n‖²_{L²([-T,T])}` |
| `χ_n(c)` | Sturm–Liouville eigenvalue of D_c: `χ_n ~ n(n+1) + c²/2` |
| `K_c` | Prolate concentration operator: `R_T ∘ B_ω ∘ R_T` |
| `K_N(x,y)` | Christoffel-Darboux kernel: `∑_{n=0}^{N-1} ψ_n(x) ψ_n(y)` |
| `G^(N)_{p,c}` | Gram matrix of PSWF-sampled form |
| `P_N` | Orthogonal projector onto `span{ψ_0,...,ψ_{N-1}}` in L²([-T,T]) |
| `DSTP` | Discrete Spectral Transfer Property — central axiom of Paper I |
| `f_{mn}` | Product function: `ψ_m^(c) · ψ_n^(c)` |
| `μ_{mn}` | Sum of SL eigenvalues: `χ_m(c) + χ_n(c)` |
| `E_{mn}[χ_k]` | Spectral mean of D_c in state f_{mn} |
| `ρ_n^cl(x)` | Classical equilibrium density for index n |
| `θ_n(x)` | Prüfer phase of ψ_n (Paper IV) |
| `r_n(x)` | Prüfer amplitude of ψ_n (Paper IV) |
| `r_n^WKB(x)` | WKB reference amplitude (Paper IV) |
| `Δ_n(x)` | Amplitude deviation: `r_n² - r_n^WKB²` (Paper IV) |
| `N_Sh = 2c/π` | Shannon number (approximate number of well-concentrated PSWFs) |

---

## Paper I — Gram Form Coercivity and DSTP

**Main result:** The prolate Gram form is coercive (explicit lower bounds) provided the
**Discrete Spectral Transfer Property (DSTP)** holds for the sampling set.

- Defect decomposition: `E_{mn} = R_{mn}^quad` — the defect is purely a quadrature error.
  The PSWF orthogonality term is **exactly zero** (not small — exactly zero).
- First-order quadrature bound: `|E_{mn}| ≤ C · h · c`, where h is mesh width.
- DSTP verified: for random sampling and Gauss–PSWF sampling.
- DSTP open: for prime sampling.

---

## Paper II — Scaling Limits, Trace Formula, Weil Connection

**Main results (all unconditional):**
- Normalized Gram operators `G̃_k` lie in the unit ball of the trace-class space.
  Banach–Alaoglu gives weak-* accumulation points `G_∞ ≥ 0` with `tr(G_∞) ≤ 1`.
- Trace formula: weighted trace of `G̃_k^w` converges to 1, consistent with PNT.
- `ω_k → 0` (bandwidth to zero) is a forced consequence of scaling with primes.

**Conditional:**
- Strong coercivity `λ_min(G̃_k) → 1` requires DSTP for prime sampling (open).
- Identification of `G_∞` as the Weil operator (the RH-relevant step) remains open.

---

## Paper II_quadrature — Implication Framework for XRY

This paper is explicitly an **implication framework**, not a theorem paper.

It shows:
- **Conjecture (i)** [PSWF product tail, bulk + off-diagonal]
  + **Conjecture (ii)** [XRY stability]
  ⟹ DSTP for bulk/off-diagonal XRY quadrature.

- The **edge regime** (m,n ~ N) is a **proved obstruction** (bandwidth doubling,
  from Paper III `prop:bwdoubling`): global uniform tail bound is FALSE.
  Conjecture (i) is therefore split: proved for bulk/off-diagonal, false globally.

---

## Paper III — PSWF Product Spectral Tail Estimates

The central analytic paper. All results are for `f_{mn} = ψ_m · ψ_n`.

| Result | Status |
|---|---|
| Uniform off-diagonal bound: `‖(I-P_N)f_{mn}‖ ≤ C T^{1/2}`, all m,n | ✅ unconditional |
| Mean spectral localization: `E_{mn}[χ_k] = μ_{mn} + E_{mn}` | ✅ unconditional |
| IBP energy identity for commutator | ✅ unconditional |
| Exact energy formula for `E_{mn}` (explicit positive functional) | ✅ unconditional |
| Spectral lower bound: `E_{mn}[χ_k] ≥ μ_{mn}/2` | ✅ unconditional |
| Edge obstruction: `E_out(f_{nn}) ≥ c₀ > 0` for n ~ N | ✅ unconditional (negative) |
| Bulk Decorrelation Reduction (Lemma 6.3): hypothesis supplied by Paper IV | ✅ unconditional |
| Bulk exponential tail bound: `‖(I-P_N)f_{mn}‖ ≤ C e^{-αN}` for m,n ≤ γN | ⚠️ cond. on Assumption 2.4 |
| Off-diagonal algebraic decay: `≤ C_p(1+\|m-n\|)^{-p}` | ⚠️ cond. on Assumption 3.1 |

**Key tool:** Slepian energy identity reduces the spectral tail bound to the
out-of-band Fourier energy of f_{mn}. Bandwidth doubling: `f_{mn} ∈ PW_{2ω}`.

**Assumption 2.4 (Paper III):** Uniform L²-bound on the out-of-band Fourier energy
of the Christoffel-Darboux kernel in the bulk sector. This is a Fourier-side statement;
Paper IV's equidistribution is time-domain. Three proof strategies in `assumption_2_4_target.md`.

---

## Paper IV — Semiclassical Equidistribution of PSWF Densities

**The most complete paper. Fully proved, no external assumptions.**

**Main theorem (`thm:weak-limit`):** For n ≤ γN and f ∈ C¹([-T,T]):
```
∫f ψ_n² dx = λ_n(c) ∫f ρ_n^cl dx + R_n(f)
|R_n(f)| ≤ (C_{δ,γ} λ_n / n) · (‖f‖_{L∞} + T‖f'‖_{L∞})
```
Uniform in n ≤ γN and f ∈ C¹. No microlocal machinery.

**Key lemmas exported (available as inputs for future work):**
- `lem:prufer-oscillation-control`: `|∫h cos(2θ_n)| ≤ C‖h‖_{C¹}/n` if `θ_n' ≳ n`
- `lem:amplitude-drift`: `r_n²/r_n^{WKB,2} = 1 + O(1/n)` uniformly in n ≤ γN
- `lem:normalization`: `r_n^{WKB,2}/2 = λ_n ρ^cl · (1+O(1/n))` — links ψ_n² to ρ^cl
- `lem:bohr-sommerfeld-pswf`: `π K_n = π/λ_n · (1+O(1/n))`

**Note:** `lem:amplitude-drift` + `lem:normalization` together imply the Diagonal-Bound
`K_N(x,x) ≤ CNc/(πT)` needed for Variante A (Schur test) in `assumption_2_4_target.md`.

**Proof structure (strict DAG, no circular dependencies):**
1. Prüfer transform: ψ_n = r_n sin θ_n, p ψ_n' = r_n ω_n^cl cos θ_n
2. Oscillation control (`lem:prufer-oscillation-control`): via IBP,
   using phase monotonicity `θ_n' ≥ c_{δ,γ} n` on I_δ.
   The **sup-form** (not just the full integral) is essential for step 3.
3. Drift cancellation identity (Step 1 of `lem:amplitude-drift`):
   `d/dx log(r_n/r_n^WKB) = G(x)(1 + cos(2θ_n))`.
   The D = p'/(4p) terms cancel **exactly algebraically**.
4. Gronwall bootstrap: the self-referential term `2Δ_n G cos(2θ_n)` is O(1/n²),
   strictly smaller than the O(1/n) main term.
5. Normalization matching via Bohr–Sommerfeld (`lem:bohr-sommerfeld-pswf`).

**Corollary (`cor:bulk-program-closed`):** Paper IV supplies hypothesis (6.1) of
Paper III Lemma 6.3 (Bulk Decorrelation Reduction) with ω_n = C_{δ,γ}/n.
This closes the bulk program up to Assumption 2.4:
```
Paper IV thm:weak-limit
  → Paper III lem:bulk-reduction          [unconditional]
  → Paper III prob:comm-refined            [unconditional]
  → Bulk tail bound                        [conditional on Assumption 2.4]
```

---

## What Is Unconditionally Proved (April 30, 2026)

- Frame coercivity under DSTP, with explicit bounds (Paper I) ✅
- Exact defect decomposition E_{mn} = R_{mn}^quad (Paper I) ✅
- DSTP verified for random and Gauss–PSWF sampling (Paper I) ✅
- Compactness of normalized Gram operators in scaling limit (Paper II) ✅
- Trace formula with PNT consistency (Paper II) ✅
- Uniform off-diagonal bound ‖(I-P_N)f_{mn}‖ ≤ CT^{1/2} (Paper III) ✅
- Mean spectral localization E_{mn}[χ_k] = μ_{mn} + E_{mn} (Paper III) ✅
- Exact energy formula for E_{mn} (Paper III) ✅
- Spectral lower bound E_{mn}[χ_k] ≥ μ_{mn}/2 (Paper III) ✅
- Edge obstruction: global uniform tail bound FALSE for m,n ~ N (Paper III) ✅
- Weak convergence of PSWF densities ψ_n² → λ_n ρ_n^cl, rate O(1/n) (Paper IV) ✅
- Drift cancellation identity and amplitude control, r_n²/r_n^WKB² = 1+O(1/n) (Paper IV) ✅
- Bulk Decorrelation Reduction hypothesis supplied (Paper IV → Paper III) ✅

---

## What Remains Open (April 30, 2026)

| Problem | Source | Severity |
|---|---|---|
| Bulk convolution decay (Assumption 2.4 of Paper III) | Paper III | **Medium — next target** |
| DSTP for prime sampling | Paper I | High |
| Off-diagonal algebraic decay (Assumption 3.1 of Paper III) | Paper III | Medium-low |
| Identification of G_∞ as Weil operator | Paper II | High (long-term) |
| XRY stability conjecture (Conjecture (ii) of Paper II_quad) | Paper II_quad | Open |
| Off-diagonal analogue of Paper IV main theorem | Paper IV P2 | Future work |
| Paper IV extension to C⁰ test functions | Paper IV P1 | Non-critical |
| Edge regime analysis m,n ~ N (Airy-scale methods) | Papers II_quad, III | Future work |

**The single most actionable next step:** prove Assumption 2.4 via the Schur test
(Variante A in `assumption_2_4_target.md`). All inputs are now explicitly available:
- Diagonal-Bound from `lem:amplitude-drift` + `lem:normalization` (Paper IV)
- Sinc off-diagonal structure from Slepian (1964)
- Schur test: Reed–Simon I, Thm. VI.23

This would make the bulk tail bound `‖(I-P_N)f_{mn}‖ ≤ Ce^{-αN}` unconditional
and close the entire bulk program without any remaining external assumptions.

---

## Key References

- Osipov–Rokhlin–Xiao (2013): *Prolate Spheroidal Wave Functions of Order Zero*, Springer
- Slepian (1978): Bell Syst. Tech. J. 57, 1371–1430
- Slepian (1964): Bell Syst. Tech. J. — explicit Sinc formula for K_N(x,y) [Eq. 3.6]
- Levitan–Sargsjan (1991): *Sturm–Liouville and Dirac Operators*, Kluwer
- Weil (1952): positivity criterion
- Connes–Consani–Moscovici (2025): arXiv:2511.22755
- Widom (1964): asymptotic concentration eigenvalue bounds
- Reed–Simon (1975): *Methods of Modern Mathematical Physics, Vol. I–II*
  (Schur test: Vol. I, Thm. VI.23)
