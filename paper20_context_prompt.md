# Paper XX — Context Prompt
## Turning-Point Truncation Geometry for Sturm–Liouville Spectral Limits

**Programme:** prolate-gram-coercivity  
**Predecessor freeze commits:** XVIII `d7609d2` / `19f5742`, XIX `580016b`  
**Status:** pre-draft — context only, no frozen results yet  
**Date:** May 2026

---

## 1. Position in the Programme

Papers XVIII and XIX form a closed unit:

| Paper | Content | Status |
|---|---|---|
| XVIII | BR3: qualitative Airy universality | FROZEN |
| XIX | BR3: quantitative two-scale rate, polynomial truncation cost | FROZEN |

Paper XX is **not a repair** of XVIII/XIX.  
It is the first step of **universalisation**: asking whether the geometric
structure discovered in XIX is special to the Airy turning point,
or is a consequence of a broader class of one-dimensional
Sturm–Liouville turning-point scalings.

---

## 2. The Central Question

> **Is the $K^{2/3}$-truncation geometry a special feature of
> the Airy turning point, or is it a universal consequence of
> one-dimensional Sturm–Liouville turning-point scalings?**

More precisely: for a Sturm–Liouville operator with eigenvalue
asymptotics $a_K \sim K^\gamma$, the XIX pipeline produces a
truncation constant $C_1(M,K) \sim K^{1+\gamma}$ and an optimal
coupling rate $\|S_K - K_{\mathcal{A}}\| \sim c^{-1/3}(\log c)^{1+\gamma}$.

For Airy: $\gamma = 2/3$, giving $1+\gamma = 5/3$ — exactly the
exponent in XIX Corollary `cor:lograte`.

The conjecture for XX is:

> **Turning-Point Truncation Law.**  
> For one-dimensional Sturm–Liouville operators with simple
> turning-point scaling and $a_K \sim K^\gamma$,
> the optimal two-scale truncation rate is governed by $1+\gamma$.

---

## 3. Inherited Inputs from XVIII/XIX

These results are **taken as black boxes** in XX — no reproof needed.

### From XVIII (FREEZE `d7609d2` + `19f5742`)

| Result | Label | Content |
|---|---|---|
| Norm-resolvent convergence | `prop:normresolvent` | $\|(\mathcal{L}_c-z)^{-1} - (\mathcal{A}-z)^{-1}\| = O(c^{-1/3})$ |
| Airy scaling window | `def:airycoord` | window $c^{-2/3}$; coordinate $\tilde\xi = c^{2/3}(x_{n^*}^* - x)$ |
| Langer approximation | `lem:langer` | $\|\tilde\psi_j - u_j\|_{C^0([0,M])} \leq C'(M,K) c^{-1/3}$ |
| $K$-dependence of $C'$ | `rem:langerkdep` | $C'(M,K) = O(MK^{2/3})$; source: $a_K \sim K^{2/3}$, $\delta_0(K) = 2C_K+2$ |
| Bessel tail | `lem:besseltail` | $\sum_{j>K}\|u_j\|_{L^2([0,M])}^2 \to 0$ as $K\to\infty$ |
| Slepian–ORX tail | `lem:slepianunif` | $\lambda_{n^*+j}^{(c)} \leq e^{-\alpha j}$, uniform in $c$ |

### From XIX (FREEZE `580016b`)

| Result | Label | Content |
|---|---|---|
| Two-scale decomposition | `def:decomp` | $S_K - K_{\mathcal{A}} = A_K - B_K$ |
| Langer-regime rate | `lem:langer_rate` | $\|A_K\|_{L^2([0,M]^2)} \leq C_1(M,K) c^{-1/3}$ |
| Polynomial truncation cost | `eq:C1scale` | $C_1(M,K) = O(M^2 K^{5/3})$ |
| Tail rate | `lem:tail_rate` | $\|B_K\|_{L^2([0,M]^2)} \leq C_2(\alpha)^{1/2} e^{-\alpha K/2}$ |
| Optimal coupling | `cor:lograte` | $K_{\rm opt}(c) \sim (\log c)/(3\alpha)$; rate $O(c^{-1/3}(\log c)^{5/3})$ |

---

## 4. The New Mathematical Variable

The key abstraction in XX is to **replace** the Airy-specific $\gamma = 2/3$
by a free parameter:

$$
a_K \sim C_\gamma K^\gamma, \qquad \gamma \in (0, 1].
$$

| Operator class | $\gamma$ | $1+\gamma$ |
|---|---|---|
| Airy ($-d^2/d\xi^2 + \xi$ on $\mathbb{R}_+$) | $2/3$ | $5/3$ |
| Harmonic oscillator ($-d^2/dx^2 + x^2$) | $1$ | $2$ |
| Power potential ($-d^2/dx^2 + |x|^\nu$, $\nu>0$) | $\frac{2\nu}{\nu+2}$ | $\frac{3\nu+2}{\nu+2}$ |
| Bessel-type | $1$ | $2$ |

The central propagation chain to track in XX:

$$
\gamma
\;\xrightarrow{a_K \sim K^\gamma}\;
C_K = a_K + 1
\;\xrightarrow{\delta_0 = 2C_K+2}\;
\mu(K) = C_K+1
\;\xrightarrow{\text{Lax--Milgram}}\;
C'(M,K) = O(K^\gamma)
\;\xrightarrow{\text{XIX pipeline}}\;
C_1(M,K) = O(K^{1+\gamma}).
$$

Then:

$$
\|S_K - K_{\mathcal{A}}\|_{L^2([0,M]^2)}
\;\Big|_{K = K_{\rm opt}(c)}
= O\!\left(c^{-1/3}(\log c)^{1+\gamma}\right).
$$

This is the **Turning-Point Truncation Law** in quantitative form.

---

## 5. Proposed Structure of Paper XX

### Section 1 — General Setup
- Abstract Sturm–Liouville operator $L = -d^2/dx^2 + V(x)$ on $\mathbb{R}_+$
  with simple turning point at $x_0$
- Eigenvalue asymptotics: $a_K \sim C_\gamma K^\gamma$ as input hypothesis
- Rescaling analogous to XVIII `def:airycoord`; scaling window $c^{-\beta}$ (to be determined)

### Section 2 — Dependency Analysis
- Which steps of the XVIII/XIX pipeline use $\gamma = 2/3$ explicitly?
- Which steps are $\gamma$-independent?
- Expected answer: only `rem:langerkdep` is $\gamma$-sensitive;
  the rest of the DAG is $\gamma$-agnostic

### Section 3 — Universal Truncation Lemma
- **Lemma `lem:trunc_universal`:**  
  $C'(M,K) = O(MK^\gamma)$, with explicit dependence on $\gamma$
- Proof strategy: track $\delta_0(K) = 2C_K + 2 \sim K^\gamma$
  through the Lax–Milgram step in full generality

### Section 4 — Universal Rate Theorem
- **Theorem `thm:universal_rate`:**  
  $\|S_K - K_{\mathcal{A}}\| \leq \tilde C_1(M,K) c^{-\beta} + C_2 e^{-\alpha K/2}$  
  with $\tilde C_1 = O(K^{1+\gamma})$ and $\beta$ depending on the scaling window
- **Corollary `cor:universal_lograte`:**  
  $K_{\rm opt}(c) \sim (\log c)/\alpha$ gives rate $O(c^{-\beta}(\log c)^{1+\gamma})$

### Section 5 — Verification Table
- Airy: $\gamma = 2/3$, $\beta = 1/3$, $1+\gamma = 5/3$ → recovers XIX exactly
- Harmonic oscillator: $\gamma = 1$, $\beta = ?$, $1+\gamma = 2$
- General power $|x|^\nu$: $\gamma = 2\nu/(\nu+2)$, $1+\gamma = (3\nu+2)/(\nu+2)$

---

## 6. Scope Boundaries (What XX Should NOT Do)

To preserve the clean XVIII/XIX geometry, Paper XX is **explicitly restricted** to:

| In scope | Out of scope |
|---|---|
| One-dimensional operators | Multi-dimensional |
| Self-adjoint, semibounded | Non-self-adjoint |
| Simple turning points | Higher-order / degenerate turning points |
| Real-valued potentials | Random or stochastic potentials |
| Compact interval $[0,M]$ restriction | Global $\mathbb{R}_+$ estimates |
| $K$-uniform Langer bound (if achievable) | Non-perturbative regimes |

A $K$-uniform Langer bound (currently open in XIX `rem:logloss`)
would be a natural goal for XX, but should be treated as a
**separate lemma**, not as a prerequisite.

---

## 7. Open Questions Inherited into XX

From XIX `rem:logloss`:
> The $(1+\gamma)$-loss could be removed if $C'(M,K)$ is shown to be
> $K$-independent. This requires a $K$-uniform coercivity estimate —
> a potential XX result.

Specifically: does there exist a potential class $V$ for which
$C'(M,K) = O(M)$ independent of $K$? If yes, the truncation law
$O(c^{-\beta}(\log c)^{1+\gamma})$ sharpens to $O(c^{-\beta} \log c)$.

---

## 8. Relationship to Broader Programme

```
XVI  → XVII → XVIII (BR3, qualitative) → XIX (BR3, quantitative two-scale)
                                                      ↓
                                              XX (universalisation)
                                           truncation geometry for
                                           general SL turning points
```

Paper XX does **not** close BR3 again — that is done.  
Its contribution is the **abstraction layer**: showing that the
$K^{5/3}$ cost in XIX is not a miracle of Airy functions but
an instance of a general $K^{1+\gamma}$ law.

---

*End of context prompt. No results frozen here.*  
*Next action: begin Section 2 (dependency analysis) to identify*  
*which XVIII/XIX steps are $\gamma$-sensitive.*
