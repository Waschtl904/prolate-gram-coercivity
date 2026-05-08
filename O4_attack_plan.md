# O4 Attack Plan: Concrete Lemma Chains

> This document gives the precise lemma-level decomposition of O4
> (Uniform Frame Stability of Ev|_Edge) into DAG-hookable steps.
>
> **Reference:** `O4_frame_stability_problem.tex` (problem formulation, tools, routes A–C).
> **DAG target:** O4 closes P9 (`lambda_min(G_{N,c}) >= alpha(c)`).
>
> Each lemma is labeled `O4-A-k`, `O4-B-k`, `O4-C-k` and can be added to
> `dag_nodes.json` as a new `T` node on axis `discrete`, requiring the
> existing nodes listed under **DAG requires**.

---

## Route A — Uniform BW-Doubling

**Core idea:** The existential BW-Doubling of Paper III
(`exists n*: E_out(|psi_{n*}|^2) >= c3`) becomes uniform over the edge block
by exploiting spectral monotonicity of K_c eigenvalues.

**Key insight:** `1 - lambda_n(c)` is *increasing* in `n` (eigenvalues decrease).
So the worst case in the edge block is `n = (1-delta)N`, and the bound there
is controlled by the Widom formula — which is already in BB5.

### Lemma O4-A-1: Spectral monotonicity transfer

**Statement.**
For all `n in [(1-delta)N, N):`
```
E_out(|psi_n|^2) = 1 - lambda_n(c) >= 1 - lambda_{(1-delta)N}(c) >= c_W(delta) > 0
```
where `c_W(delta) = 1 - erfc_approx((2alpha/pi - 1 + delta) * sqrt(c))` from Widom.

**Proof sketch.** Direct: eigenvalue monotonicity (standard) + Widom lower
boundary formula (BB5) applied at `n = (1-delta)N`.

**DAG requires:** BB5, BB3 (Widom gives the erfc boundary scale).
**DAG feeds:** O4-A-2.
**Difficulty:** LOW. This is essentially bookkeeping.

---

### Lemma O4-A-2: Energy-outside to sampling lower bound

**Statement.**
For `f = sum_{n in Edge} a_n psi_n` and sampling set `Lambda = {p_j*}`:
```
(1/N) sum_j |f(p_j*)|^2  >=  c_W(delta) * (1/N) sum_j sum_n |a_n|^2 |psi_n(p_j*)|^2
                          -   (cross-term error)
```
where the cross-term error is controlled by `|G_{mn}|` for `m != n`.

**Proof sketch.** Expand `|f(p_j*)|^2`, separate diagonal and off-diagonal.
Diagonal gives `c_W * ||f||^2` by O4-A-1. Off-diagonal needs separate control
(this is the hard part — it's exactly the Jaffard route, Route B).

**DAG requires:** O4-A-1.
**DAG feeds:** O4-A-3 (if cross terms controlled) or O4-B-1 (cross-term reduction).
**Difficulty:** MEDIUM. The cross-term estimate is the bottleneck.

---

### Lemma O4-A-3: Off-diagonal cancellation via PNT gap control

**Statement.**
The cross-term satisfies:
```
|sum_{m!=n} a_m conj(a_n) G_{mn}|  <=  C(delta) * (log N / N) * ||f||^2
```
for all `f in Edge`, where the `log N / N` factor comes from prime gap statistics.

**Proof sketch.**
`|G_{mn}| = (1/N)|sum_j psi_m(p_j*) psi_n(p_j*)|`.
Use Cauchy-Schwarz: `|G_{mn}| <= sqrt(G_{mm} G_{nn})`. Then use that off-diagonal
terms for |m-n| >= 1 contribute a sum bounded by the Schur row-sum of `|G - I|`,
which is controlled by prime gap statistics (inter-prime gaps ~ log N).

**DAG requires:** O4-A-1, PNT (standard, BB-level).
**DAG closes:** O4 (combined with O4-A-1, O4-A-2).
**Difficulty:** MEDIUM-HIGH. The Schur row-sum bound needs a clean prime gap argument.

**Critical question:** Does `(log N / N) * N = log N -> infty` break the bound?
Answer: No — the Schur test gives `||G - I|| <= C * (log N / N) * N^(epsilon)`
for any `epsilon > 0` by partial summation. For `N` large, this goes to 0
if the prime gaps are `O(log N)` uniformly (Cramer conjecture).
Under RH only: prime gaps are `O(sqrt(N) log N)` — too large.
**→ Route A requires a sub-RH prime gap input or a weaker uniform estimate.**

---

## Route B — Jaffard Gram Matrix Inversion

**Core idea:** Show `G = I + E` with `||E||_{ell^1 -> ell^1} < 1`.
Then `lambda_min(G) >= 1 - ||E|| > 0` by Neumann series.

**Key tool:** Langer–Olver approximation for `psi_n` in the edge window
(Paper XVIII, available as infrastructure). The off-diagonal decay of `G_{mn}`
follows from Airy function oscillation.

### Lemma O4-B-1: Airy approximation of edge PSWFs

**Statement.**
For `n in [(1-delta)N, N)` and `x in [-1,1]` in the transition window:
```
|psi_n(x) - c^(1/6) Ai(c^(2/3) zeta_n(x))| <= C c^(-1/2)
```
uniformly in `n` and `x`.

**Proof sketch.** Langer–Olver theorem (Paper XVIII, Theorem A). Already available.

**DAG requires:** BB5 (Widom), Paper XVIII infrastructure (available as BB from trilogy).
**DAG feeds:** O4-B-2.
**Difficulty:** LOW. This is already done in Paper XVIII.

---

### Lemma O4-B-2: Off-diagonal Gram decay via Airy oscillation

**Statement.**
For `m, n in [(1-delta)N, N)` with `|m - n| >= 1`:
```
|G_{mn}|  <=  C / (|m - n| + 1)^(3/2)
```
uniformly in `N` and in the prime sampling set `{p_j*}`.

**Proof sketch.**
Substitute Langer–Olver into `G_{mn} = (1/N) sum_j psi_m(p_j*) psi_n(p_j*)`.
The Airy functions satisfy:
```
Ai(t - s) Ai(t)  ~  (1/pi) cos(phi(t,s)) / (1 + |s|)^(1/2)   for s = c^(2/3)(zeta_m - zeta_n)
```
The sum over `j` (prime points) contributes an oscillatory integral over `[-1,1]`;
stationary phase gives decay `|m-n|^(-3/2)` from the separation of Airy zeros.

**DAG requires:** O4-B-1.
**DAG feeds:** O4-B-3.
**Difficulty:** MEDIUM. Airy product oscillation integrals are classical but need care.

---

### Lemma O4-B-3: Jaffard ell^1 bound and matrix invertibility

**Statement.**
The edge Gram matrix satisfies:
```
sum_{n} |G_{mn}|  <=  1 + C_J  for all m,
sum_{m} |G_{mn}|  <=  1 + C_J  for all n,
```
where `C_J = sum_{k>=1} C / k^(3/2) < infty`.
Therefore `||G - I||_{ell^1 -> ell^1} <= C_J < 1` for `c` large enough,
and `lambda_min(G) >= 1 - C_J > 0`.

**Proof sketch.** Schur test: row sums bounded by O4-B-2 via `sum_k k^(-3/2) < infty`.
Jaffard's theorem then gives invertibility in the Banach algebra sense.

**DAG requires:** O4-B-2.
**DAG closes:** O4.
**Difficulty:** LOW once O4-B-2 is established. Pure functional analysis.

**Status of Route B:**
The bottleneck is **O4-B-2** (Airy oscillation integral over primes).
This is the most precisely formulated attack point — and it does NOT depend on O5.

---

## Route C — Beurling–Kadec for Edge-Restricted PW

**Core idea:** The edge modes `psi_n` with `n in [(1-delta)N, N)` have effective
bandwidth `(1-delta)c`. The primes are `(1-delta)c`-dense by PNT.
Apply Beurling–Kadec stability directly.

### Lemma O4-C-1: Effective bandwidth of edge modes

**Statement.**
For `f in Edge`, the Fourier transform satisfies:
```
supp(hat{f})  ⊂  [-(1-delta/2)c, (1-delta/2)c]
```
up to an error `O(c^(-1/2))` in `L^2` norm.

**Proof sketch.**
Each `psi_n` with `n < N` concentrates its Fourier energy on `[-c, c]`;
for `n < (1-delta)N`, the concentration shifts inward by the Slepian eigenvalue
gap. Quantitative: `||psi_n||_{L^2(|xi|>(1-delta/2)c)} <= C e^{-alpha delta c}`
by the super-exponential tail of PSWF eigenvalues.

**DAG requires:** BB3 (Gram-gap gives PSWF tail control), BB5.
**DAG feeds:** O4-C-2.
**Difficulty:** MEDIUM. Needs quantitative PSWF Fourier concentration.

---

### Lemma O4-C-2: Prime Nyquist density for effective bandwidth

**Statement.**
The prime set `{p_j*}` in `[-1,1]` satisfies Beurling lower density:
```
D^-({p_j*})  >=  (1-delta/2) c / pi  +  c_PNT
```
for `c` large, where `c_PNT > 0` follows from PNT with explicit error.

**Proof sketch.**
Beurling density = `lim_{r->infty} inf_x #{p_j*: |p_j*-x|<r} / (2r)`.
By PNT: primes up to `x` have density `1/log x`; normalised to `[-1,1]`,
the density of `{p_j*}` is `alpha = N / (p_N * 2) ~ 1/(2 log N)`.
But the relevant comparison is with `(1-delta/2)c/pi`; for the rescaled problem
(bandwidth `(1-delta/2)c`), the Nyquist threshold is `(1-delta/2)c/pi`.
Check: `alpha * pi >= (1-delta/2)c` requires `c` to be small relative to `N`;
for fixed `alpha = N/c`, this holds for `alpha > (1-delta/2)/pi`.

**DAG requires:** PNT (standard, BB-level).
**DAG feeds:** O4-C-3.
**Difficulty:** LOW. Standard density calculation.
**Risk:** The effective bandwidth argument needs `alpha > (1-delta/2)/pi` which
may not hold for all `alpha in (0, 2/pi)`. Need to check the regime.

---

### Lemma O4-C-3: Beurling–Kadec frame stability

**Statement.**
Under O4-C-1 and O4-C-2: the set `{p_j*}` is a frame for `Edge` with
frame constants `A, B > 0` depending only on `delta` and `alpha`, uniform in `N`.

**Proof sketch.**
Apply Beurling–Kadec theorem: if `Lambda` has Beurling density `> c_eff/pi`
and `f` is bandlimited with bandwidth `c_eff`, then `Lambda` is a stable sampling set.
Here `c_eff = (1-delta/2)c` from O4-C-1, and density condition from O4-C-2.

**DAG requires:** O4-C-1, O4-C-2.
**DAG closes:** O4.
**Difficulty:** LOW once O4-C-1 and O4-C-2 are established. Classical result.

---

## Comparison of Routes

| Route | Bottleneck lemma | Difficulty | Requires RH/Cramer | Depends on O5 |
|---|---|---|---|---|
| A | O4-A-3 (prime gap Schur bound) | HIGH | Partially (sub-RH gap) | No |
| B | O4-B-2 (Airy oscillation over primes) | MEDIUM | No | No |
| C | O4-C-1 (effective bandwidth) | MEDIUM | No | No |

**Recommended starting point: Route B, Lemma O4-B-2.**

Reason: the Airy product oscillation integral is a classical object in
integrable systems (it appears in Tracy–Widom kernel estimates);
the decay rate `|m-n|^(-3/2)` is sharp and the stationary phase argument
is well-scoped. Route C is parallel but requires controlling the bandwidth
regime carefully. Route A has an arithmetic obstruction.

---

## DAG Hookup: New Nodes to Add

After proving the bottleneck lemma for chosen route, add to `dag_nodes.json`:

```json
{
  "id": "O4B2",
  "type": "T",
  "statement": "Off-diagonal Gram decay: |G_{mn}| <= C / |m-n|^(3/2) uniformly in N",
  "source": "O4_frame_stability_problem.tex Route B + O4_attack_plan.md",
  "axis": "discrete",
  "used_in": ["O4B3"],
  "requires": ["O4B1"],
  "on_minimal_path": false
},
{
  "id": "O4B3",
  "type": "T",
  "statement": "Jaffard bound: ||G - I||_{ell^1} <= C_J < 1 => lambda_min(G) >= 1 - C_J",
  "source": "O4_attack_plan.md",
  "axis": "discrete",
  "used_in": ["P9"],
  "requires": ["O4B2"],
  "on_minimal_path": false
}
```

Once O4B3 is proved, update `O4.used_in` to `["P9", "O4B3"]` and
change `O4.type` from `O` to `T` (open problem resolved).

---

*Generated May 2026. Update after each lemma is resolved.*
