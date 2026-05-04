# Context Summary — PSWF Galerkin / Prolate–Weil Program

> Internal scaffold for session continuity.
> Last updated: May 2026 (after Paper VIII submission-ready v6).

---

## Current state of the series

**Papers I–VIII are complete.** Paper VIII is submission-ready (v6).
Paper IX (WKB attack on Assumption ass:gap) is the planned next step.

| Paper | Short title | Status |
|---|---|---|
| I | Frame coercivity, DSTP | Complete |
| II | Scaling limit, trace formula | Complete |
| II (quad) | XRY quadrature compatibility | Complete |
| III | PSWF product tail, edge obstruction | Complete |
| IV | Semiclassical equidistribution (Prüfer) | Complete |
| V | Galerkin norm estimates | Complete |
| VI | Prolate phase operator, B-strong framework | Complete |
| VII | Dyadic cancellation, abstract Theorem 2.1 | Complete |
| **VIII** | **Scale-separated Dyadic Separation** | **Submission-ready v6** |
| IX | WKB proof of ass:gap | **Planned** |

---

## Paper VIII: What was proved

**Main result:** Under Assumption ass:gap and B-strong, hypotheses (H1)–(H3)
of Paper VII Theorem 2.1 are verified via the **Dyadic Separation Principle**.

**The operative mechanism:** For `j ∈ B_m(i)`, the ratio
`|λ_j − λ_{j+1}| / |λ_i − λ_j|`
is O(2^{−m}) independent of c, because (c/2)^{−1/3} cancels between
numerator and denominator. The denominator carries the combinatorial
factor 2^m from |i−j| ≥ 2^m.

**Structural novelty:** Lemma F (DSP) requires only
- strict monotonicity of eigenvalues, and
- a uniform gap lower bound at scale (c/2)^{−1/3} (= Assumption ass:gap).

No Airy functions, no erfc, no detailed spectral asymptotics are needed
for Lemma F itself.

**Three-scale architecture:**
1. **Combinatorial (c^{−1/3}):** Lemma F, Corollary C — rigorous under ass:gap
2. **Local Airy ((c/2)^{−1/3}):** Proposition U/U', Lemma A — open
3. **Global Landau–Widom ((log c)^{2/3}):** Conjecture ULW — empirical only

Scale separation: S(c)/(c/2)^{−1/3} ~ c^{1/3}(log c)^{2/3} → ∞.

---

## Key open problems after Paper VIII

### Priority 1 — Target of Paper IX

**Assumption ass:gap:** `λ_l − λ_{l+1} ≥ κ_0 (c/2)^{−1/3}` for all l in transition window.
- Route (i): via Proposition U (would give κ_0 = c_min/2, but Prop U itself is open)
- Route (ii): first-order WKB monotone comparison (no Airy matching needed — preferred route)
- Route (iii): heuristic numerics (not a proof)

This is the **sole gap** between Paper VIII's conditional reduction and a fully
unconditional contraction estimate.

### Priority 2 — Required for full unconditional proof

**Proposition U (and U'):**
- (U): `|λ_l − F_Ai(x_l)| ≤ C₁ c^{−2/3}` pointwise
- (U'): `|(λ_l − λ_{l+1}) − (F_Ai(x_l) − F_Ai(x_{l+1}))| ≤ C₂ c^{−2/3}`
- Proof requires: uniform WKB, Airy matching, stability under discrete differentiation
- (U') is stronger than (U): controls the discrete derivative of the error

**B-strong:** `P_{kl} ≤ C₂ c^{1/2}` in the transition zone (Paper VI context)

### Priority 3 — Earlier in the series, still open

- Bulk convolution decay (Assumption 2.4 of Paper III): Schur test approach recommended
- DSTP for prime sampling (Paper I)
- XRY stability conjecture (Paper II quad)
- Identification of G_∞ as Weil operator (Paper II)

### Empirical (Paper VIII, no analytic route known)

- **Conjecture ULW:** erfc global scaling law with S(c) = (log c/π)^{2/3}
  - Residuals ≈ 2·10^{−2} across c ∈ {50, 100, 200}, decreasing with c
- **β(c):** centering parameter, β(50) ≈ −0.424, β(100) ≈ −0.380, β(200) ≈ −0.359
  - Fitting suggests β(∞) ∈ [−0.30, −0.21]; model sensitivity high
  - No structural identification known

---

## Internal terminology

| Symbol / term | Meaning |
|---|---|
| ass:gap | Assumption ass:gap = Assumption 1 of Paper VIII: uniform gap lower bound |
| Prop U / U' | Proposition 1(U)/(U') of Paper VIII: uniform Airy approximation |
| B-strong | Galerkin norm bound `P_{kl} ≤ C₂ c^{1/2}` (Paper VI) |
| Conj ULW | Conjecture 1 of Paper VIII: Landau–Widom erfc global scaling law |
| DSP / Lemma F | Dyadic Separation Principle: Lemma F of Paper VIII |
| Cor C | Corollary C of Paper VIII: H2 in truncated dyadic sense |
| N_Sh | N_Sh = 2c/π (Landau–Widom counting number) |
| x_l | Rescaled transition index: x_l = (l − N_Sh)(c/2)^{−1/3} |
| F_Ai | Integrated Airy function: F_Ai(x) = ∫_x^∞ Ai(t)² dt |
| S(c) | Landau–Widom width: S(c) = (log c/π)^{2/3} |
| β(c) | Centering parameter in Conjecture ULW |
| B_m(i) | Dyadic annulus: {j : 2^m ≤ |i−j| < 2^{m+1}} |
| DSTP | Discrete Spectral Transfer Property |
| PNT | Prime Number Theorem (appears via trace formula, Paper II) |

---

## Planned Paper IX: WKB route to ass:gap

**Goal:** Prove Assumption ass:gap without Airy matching.

**Strategy:**
1. Write PSWF eigenvalues in terms of the Prüfer phase angle θ_n(c)
2. Use first-order WKB to bound θ_n'(x) from below in the transition window
3. Derive gap lower bound `λ_l − λ_{l+1} ≥ κ_0 (c/2)^{−1/3}` via monotone comparison
4. Explicit κ_0 in terms of WKB data (no Airy constants needed)

**Why this is preferred over route (i) (via Prop U):**
Route (ii) (WKB monotone comparison) requires strictly less:
no uniform Airy approximation, no matching argument, only leading-order
WKB behavior. It would also give a cleaner proof of ass:gap as a standalone result.

**Dependency:** If Paper IX succeeds, the chain
ass:gap + B-strong → Lemma F → Corollary C → Lemma E → Corollary (Paper VIII)
becomes unconditional in the ass:gap component.
B-strong remains the sole surviving open input for the dyadic contraction estimate.

---

## Session notes

- All .md documentation files updated May 2026 to reflect Paper VIII status.
- Paper VIII file: `paper8_scale_separated.tex`, submission-ready v6.
- Proof scaffolds for open problems: see `assumption_2_4_target.md` (for Ass. 2.4 of Paper III).
- Numerical evidence files: see `numerics/` directory.
