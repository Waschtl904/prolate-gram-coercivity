# O5 Route B Attack Plan

> **Target:** `inf sigma(D^Airy) >= c2 > 0` (closes P12, feeds P13).
>
> **Strategy:** Operator dominance decomposition
> ```
> inf sigma(D^Airy)  >=  lambda_min(A^arith|_edge)  -  ||K^Airy|_edge||
> ```
> Route B makes this explicit by bounding both sides with known or accessible tools.
>
> **Reference:** `O5_airy_gap_problem.tex` (problem formulation, all three routes).
> **Numerical anchor:** F_TW(0) ≈ 0.9597 (Bornemann 2010) => ||K^Airy|| <= 1 - F_TW(0) ≈ 0.04.

---

## Lemma Graph

```
[PNT density]         [Langer-Olver / Paper XVIII]     [Tracy-Widom, Bornemann]
      |                          |                              |
      v                          v                              v
  O5-B-2.1               O5-B-2.2                         O5-B-1
(Airy-window           (Lower frame bound             (||K^Airy|| <= 0.04)
  density)              in Airy coords)
      \                    /                                   |
       \                  /                                    |
        v                v                                    |
          O5-B-2.3                                            |
    (lambda_min(A^arith) >= c_PNT)                           |
                   \                                         /
                    v                                       /
                  O5-B-3  <-------------------------------/
          (inf sigma(D^Airy) >= c_PNT - 0.04 > 0)
                    |
                    v
                   P12  -->  P13
```

---

## Lemma-by-Lemma Breakdown

### O5-B-1: Operator norm of K^Airy

**Statement.**
```
||K^Airy_(0)||_{L^2([0,R])}  <=  1 - F_TW(0)  for all R > 0.
```

**Proof.** The eigenvalues {mu_k} of K^Airy satisfy
`prod_k (1 - mu_k) = det(I - K^Airy) = F_TW(0) approx 0.9597`.
Since all mu_k in [0,1): `mu_max <= 1 - prod_k(1-mu_k) = 1 - F_TW(0) approx 0.04`.
(More precisely: `mu_max = 1 - F_TW(0)` iff only one nonzero eigenvalue,
which is false; so `mu_max < 0.04` strictly.)

**DAG requires:** Tracy-Widom 1994 (BB-import), Bornemann 2010 (numerical).
**Status:** COMPLETE (import). No new work needed.
**Difficulty:** ZERO. Direct consequence of TW theory.

---

### O5-B-2.1: Airy-window density transfer

**Statement.**
Let p_j^Airy be the primes rescaled to the Airy window via
```
p_j^Airy = c^{2/3} * (p_j^* - t_N)
```
where t_N = cos(pi*N/(2N)) = 0 is the edge turning point.
Then the empirical measure mu_N^Airy = (1/N) sum_j delta_{p_j^Airy}
converges weakly to an absolutely continuous measure
```
mu_Airy(dt) = rho_Airy(t) dt
```
with density satisfying `0 < rho_0 <= rho_Airy(t) <= rho_1 < infty`
uniformly on compact subsets of [0, infty).

**Proof sketch.**
By PNT: primes near p_N have density 1/log(p_N) ~ 1/log(N) ~ 1/c.
After Airy rescaling (factor c^{2/3}): effective density becomes
`c^{2/3} * (1/c) = c^{-1/3} -> 0` as c -> infty.

**CRITICAL ISSUE:** The naive density `c^{-1/3}` goes to 0,
not to a finite limit. This means the Airy-rescaled prime process
becomes *sparse* in the limit, not dense.

This is the fundamental tension in O5:
- The Airy window has scale c^{-2/3}
- The prime spacing at p_N is ~ log(N) ~ log(c)
- The number of primes in the Airy window is ~ c^{-2/3} * c / log(c) = c^{1/3} / log(c)

For large c, there ARE primes in the Airy window (c^{1/3}/log(c) -> infty),
but the *rescaled* density is c-dependent.

**Resolution:** The statement must be reformulated as:
```
rho_Airy(t) = (c^{1/3} / log(c)) * rho_normalized(t)
```
where rho_normalized is the PNT density profile normalized to [0,1].
The frame bound (O5-B-2.2) will then have a c-dependent constant,
and the final coercivity bound will be:
```
c_PNT = c_0 * c^{1/3} / log(c)  -> infty as c -> infty.
```
This means: for large c, the arithmetic sampling *dominates* K^Airy,
but the proof requires showing c^{1/3}/log(c) >> 0.04 for all c >= c_0.

**DAG requires:** PNT with explicit error (Rosser-Schoenfeld or Dusart).
**Difficulty:** MEDIUM. The density calculation is elementary but the
uniformity in c requires care.

---

### O5-B-2.2: Lower frame bound in Airy coordinates

**Statement.**
For f in Pi_Airy * L^2([0,R]):
```
(1/N) sum_j |f(p_j^Airy)|^2  >=  c_frame(c) * ||f||^2
```
where `c_frame(c) ~ c^{1/3} / log(c)` (from O5-B-2.1).

**Proof sketch.**
Expand f in the Airy eigenfunction basis {phi_k} of K^Airy.
The sampling sum becomes:
```
(1/N) sum_j |f(p_j^Airy)|^2  =  sum_{k,l} a_k conj(a_l) * (1/N) sum_j phi_k(p_j^Airy) phi_l(p_j^Airy)
```
The diagonal terms (k=l) give c_frame * ||f||^2 by O5-B-2.1.
The off-diagonal terms are controlled by the Airy off-diagonal decay
(exactly the structure of O4-B-2, but now in the Airy eigenfunction basis
rather than the PSWF edge basis).

**Key insight:** O4-B-2 and O5-B-2.2 share the same off-diagonal decay structure.
O5-B-2.2 imports the O4-B-2 decay estimate in a different basis.

**DAG requires:** O5-B-2.1, O4-B-2 (off-diagonal Airy decay, already proved).
**Difficulty:** MEDIUM. The basis change from PSWF-edge to Airy eigenfunctions
needs a careful Parseval-type argument.

---

### O5-B-2.3: Spectral coercivity of A^arith

**Statement.**
```
lambda_min(A^arith|_edge)  >=  c_frame(c)  ~  c^{1/3} / log(c).
```

**Proof.** Direct: Rayleigh quotient characterisation of lambda_min
plus O5-B-2.2. No new argument.

**DAG requires:** O5-B-2.2.
**Difficulty:** LOW once B-2.2 is done.

---

### O5-B-3: Final coercivity

**Statement.**
```
inf sigma(D^Airy)  >=  c_frame(c) - ||K^Airy||  >=  c^{1/3}/log(c) - 0.04  > 0
```
for all c >= c_0 (explicit c_0 from PNT).

**Proof.** Min-Max principle:
```
inf sigma(A^arith - K^Airy)  >=  inf sigma(A^arith) + inf sigma(-K^Airy)
                             =   lambda_min(A^arith) - ||K^Airy||
```
Apply O5-B-2.3 and O5-B-1.

**DAG requires:** O5-B-2.3, O5-B-1.
**Difficulty:** LOW. Pure operator algebra.

---

## The Universality Question (sub4)

The constant `c_frame(c) ~ c^{1/3}/log(c)` is *not* universal:
it depends on the prime distribution via log(c).

This means: **c_2^Airy is arithmetic-sensitive**, not universal.

Specifically:
- If we replaced the primes by a generic sequence with the same Beurling density,
  we would get a different constant.
- The *existence* of c_2 > 0 is universal (holds for any sequence with positive density).
- The *value* of c_2 depends on the arithmetic of the sampling sequence.

This is the precise answer to sub4 in O5_airy_gap_problem.tex:
```
The gap exists universally (for any positive-density sequence),
but its value is arithmetic-sensitive.
```

---

## Comparison with O4

| Property | O4 | O5 |
|---|---|---|
| Core lemma | Off-diagonal decay (oscillatory) | Lower frame bound (density) |
| Depth | Collapsed to scaling consistency | Remains operator-level |
| c-dependence | Cancels (c-independent bound) | Does NOT cancel (c^{1/3}/log(c)) |
| Universality | Yes (Airy is coordinate only) | No (arithmetic survives) |
| Bottleneck | T2 (bookkeeping) | O5-B-2.2 (basis change + density) |
| Imports O4-B-2? | N/A | Yes (off-diagonal structure shared) |

---

## DAG Hookup

After proof of O5-B-3, add to `dag_nodes.json`:

```json
{"id": "O5B1", "type": "T", "statement": "||K^Airy|| <= 1 - F_TW(0) approx 0.04",
 "axis": "spectral", "used_in": ["O5B3"], "requires": ["BB_TW"]},
{"id": "O5B21", "type": "T", "statement": "Airy-window prime density: rho_Airy ~ c^{1/3}/log(c)",
 "axis": "spectral", "used_in": ["O5B22"], "requires": []},
{"id": "O5B22", "type": "T", "statement": "Lower frame bound: (1/N) sum |f(p_j^Airy)|^2 >= c_frame ||f||^2",
 "axis": "spectral", "used_in": ["O5B23"], "requires": ["O5B21", "O4B2"]},
{"id": "O5B23", "type": "T", "statement": "lambda_min(A^arith|_edge) >= c_frame(c)",
 "axis": "spectral", "used_in": ["O5B3"], "requires": ["O5B22"]},
{"id": "O5B3", "type": "T", "statement": "inf sigma(D^Airy) >= c^{1/3}/log(c) - 0.04 > 0 for c >= c_0",
 "axis": "spectral", "used_in": ["P12"], "requires": ["O5B1", "O5B23"]}
```

When O5B3 is proved: change O5 node type from `O` to `T` in dag_nodes.json.

---

*Generated May 2026.*
