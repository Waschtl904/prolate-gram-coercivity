# Paper XX — Full Scaffold
## Universality of Turning-Point Truncation Geometry

**Programme:** prolate-gram-coercivity  
**Predecessor freeze commits:** XVIII `d7609d2`/`19f5742`, XIX `580016b`  
**Status:** scaffold — no results frozen yet  
**Date:** May 2026

---

## Position in the Programme

Papers XVIII and XIX form a closed unit:

| Paper | Content | Status |
|---|---|---|
| XVIII | BR3: qualitative Airy universality | FROZEN |
| XIX | BR3: quantitative two-scale rate, truncation cost $O(K^{5/3})$ | FROZEN |

Paper XX is the **universalisation layer**.  
It shows that the exponent $5/3 = 1 + 2/3$ in XIX is not a miracle of Airy
functions but an instance of a general law:

> **The logarithmic exponent of the optimal two-scale truncation rate
> equals $1 + \gamma$, where $\gamma$ is the spectral growth exponent
> $a_K \sim K^\gamma$ of the rescaled Sturm–Liouville operator.**

This makes the truncation rate a **spectral invariant** of the
turning-point model — not just rate bookkeeping.

---

## §1. Abstract Mechanism

### 1.1 Operator Class

Fix a one-dimensional Sturm–Liouville operator on $L^2(\mathbb{R}_+)$:
$$
\mathcal{A}_\gamma = -\partial_\xi^2 + V(\xi),
\qquad \mathcal{D}(\mathcal{A}_\gamma) = H^2 \cap H^1_0(\mathbb{R}_+),
$$
with $V \geq 0$, $V(\xi) \to +\infty$ as $\xi \to +\infty$,
discrete spectrum $0 < a_1 < a_2 < \cdots$, and the single
**spectral growth hypothesis**:
$$
\boxed{a_K \sim C_\gamma K^\gamma \qquad (K \to \infty),
\quad \gamma \in (0,1].}
$$
No further regularity of $V$ beyond what Langer/Olver requires on
compact intervals is assumed.

The Airy operator of XVIII is the model case $\gamma = 2/3$,
$V(\xi) = \xi$, $C_\gamma = (3\pi/2)^{2/3}$.

### 1.2 The Spine

The entire truncation economy is controlled by the following propagation
chain, which is the **structural spine** of Paper XX:

$$
a_K \sim K^\gamma
\;\xrightarrow{\ell_0}\;
C_K = a_K + 1
\;\xrightarrow{\text{Step 2}}\;
\delta_0(K) = 2C_K + 2
\;\xrightarrow{\text{Lax--Milgram}}\;
C'(M,K) = O(K^\gamma)
\;\xrightarrow{\text{XIX pipeline}}\;
C_1(M,K) = O(K^{1+\gamma}).
$$

Everything else in the XVIII/XIX DAG is $\gamma$-agnostic and carries over
unchanged.

### 1.3 Scaling Window

The Airy scaling window $c^{-2/3}$ in XVIII is specific to $V(\xi) = \xi$
(linear turning point). For general $\mathcal{A}_\gamma$, the window
$c^{-\beta}$ depends on the local behaviour of $V$ near the turning point.
**The exponent $\beta$ is a separate input**, independent of $\gamma$;
the universal formula combines both:
$$
\|S_K - K_{\mathcal{A}}\|_{L^2([0,M]^2)}
\Big|_{K = K_{\rm opt}(c)}
= O\!\left(c^{-\beta} (\log c)^{1+\gamma}\right).
$$

---

## §2. Dependency Analysis — the Structural Core

This section is the **central mathematical contribution** of XX.
It identifies which nodes of the XVIII/XIX DAG are $\gamma$-sensitive
and which are $\gamma$-agnostic.

### 2.1 $\gamma$-Agnostic Nodes (unchanged from XVIII/XIX)

These steps use only functional-analytic infrastructure;
they hold for any $\mathcal{A}_\gamma$:

| Node | Content | Why $\gamma$-agnostic |
|---|---|---|
| Tensor decomposition $A_K - B_K$ | XIX `def:decomp` | Pure algebra |
| Tensor norm estimate (per $j$) | XIX `lem:langer_rate` proof | Only $\|\cdot\|_{L^2([0,M]^2)} = \|\cdot\|_{L^2}\|\cdot\|_{L^2}$ |
| Bessel tail $\sum_{j>K}\|u_j\|_{L^2([0,M])}^2 \to 0$ | XVIII `lem:besseltail` | Bessel inequality + $L^1$ diagonal; no $V$ |
| Tonelli/DCT argument | XVIII `rem:dct` | $L^1([0,M]^2)$ domination; no $V$ |
| Slepian-type tail $\lambda_{n^*+j}^{(c)} \leq e^{-\alpha j}$ | XVIII `lem:slepianunif` | ORX/Slepian structure; independent of $\gamma$ |
| HS/Cauchy–Schwarz on $B_K$ | XIX `lem:tail_rate` | Spectral orthogonality only |
| Sequential $(c,K)$-limit | XVIII `rem:iterated`, XIX `rem:nojoint` | Two-scale structure; no $V$ |
| Norm-resolvent perturbation | XVIII `prop:normresolvent` | Kato VI; uses only form-boundedness |

### 2.2 $\gamma$-Sensitive Nodes (require updating in XX)

Exactly **four nodes** depend on $\gamma$, all within the Spine of §1.2:

| Node | Current (Airy, $\gamma=2/3$) | General ($\gamma$ free) |
|---|---|---|
| Spectral spacing | $a_K \sim (3\pi K/2)^{2/3}$ | $a_K \sim C_\gamma K^\gamma$ |
| Coercive threshold | $\mu(K) = C_K+1 \sim K^{2/3}$ | $\mu(K) \sim K^\gamma$ |
| Exclusion window | $\delta_0(K) = 2C_K+2 \sim K^{2/3}$ | $\delta_0(K) \sim K^\gamma$ |
| Lax–Milgram constant | $C'(M,K) = O(MK^{2/3})$ | $C'(M,K) = O(MK^\gamma)$ |

**Key Proposition** (to be proved in XX §3):

> *Under the spectral growth hypothesis $a_K \sim K^\gamma$,
> the Lax–Milgram constant satisfies $C'(M,K) = O(MK^\gamma)$
> and hence $C_1(M,K) = O(M^2 K^{1+\gamma})$.*

This is the **only new lemma** needed; the rest of the XIX pipeline
applies verbatim with $K^{1+\gamma}$ replacing $K^{5/3}$.

### 2.3 DAG Surgery

The modified DAG for XX has exactly one changed subgraph:
```
[a_K ~ K^gamma]  -->  [C_K ~ K^gamma]  -->  [delta_0 ~ K^gamma]
      |
      v
[C'(M,K) = O(K^gamma)]   <-- ONLY NEW LEMMA
      |
      v
[C_1(M,K) = O(K^{1+gamma})]   (XIX lem:langer_rate, re-parameterised)
      |
      v
[Universal rate theorem]   (XIX thm:twoscale, re-parameterised)
```
All other XVIII/XIX nodes are inherited without change.

---

## §3. Universal Truncation Theorem

### Lemma `lem:trunc_universal` (new)

*Let $\mathcal{A}_\gamma$ satisfy the spectral growth hypothesis
$a_K \sim C_\gamma K^\gamma$.  
Then for fixed $M < \infty$ and $K \geq 1$:*
$$
C'(M,K) = O(M K^\gamma),
\qquad C_1(M,K) = O(M^2 K^{1+\gamma}),
$$
*with constants independent of $c$.*

**Proof sketch.**  
Track $\delta_0(K) = 2C_K + 2 \sim 2C_\gamma K^\gamma + 2$
through the coercivity estimate of XVIII `lem:langer` Step 2:
$q_c \geq \mu(K) = C_K + 1 \sim K^\gamma$ on $[\delta_0(K), M]$.
The Lax–Milgram step yields $C'(M,K) = O(M \mu(K)^{-1} \cdot \|R_c\|) = O(MK^\gamma)$
after inserting $a_K \sim K^\gamma$. Substituting into
$C_1 = KM \cdot C'(2C_\infty + C')$ gives $C_1 = O(K \cdot K^\gamma) = O(K^{1+\gamma})$.

### Theorem `thm:universal_rate` (main result of XX)

*Under the spectral growth hypothesis and with $\beta$ the
scaling-window exponent, for fixed $K$ and $c \to \infty$:*
$$
\|S_K - K_{\mathcal{A}}\|_{L^2([0,M]^2)}
\leq C_1(M,K) \cdot c^{-\beta} + C_2(\alpha)^{1/2} \cdot e^{-\alpha K/2}.
$$

### Corollary `cor:universal_lograte`

*With $K_{\rm opt}(c) = \lfloor \beta \log(c) / \alpha \rfloor$:*
$$
\|S_K - K_{\mathcal{A}}\|_{L^2([0,M]^2)}
\Big|_{K = K_{\rm opt}(c)}
= O\!\left(c^{-\beta}(\log c)^{1+\gamma}\right).
$$

*The exponent $1 + \gamma$ is the spectral invariant of the
turning-point model. It cannot be improved without a
$K$-uniform Langer bound.*

---

## §4. Model Table

| Operator $\mathcal{A}_\gamma$ | $V(\xi)$ | $\gamma$ | $\beta$ | $1+\gamma$ | Rate |
|---|---|---|---|---|---|
| **Airy** (XVIII/XIX) | $\xi$ | $2/3$ | $1/3$ | $\mathbf{5/3}$ | $O(c^{-1/3}(\log c)^{5/3})$ |
| Harmonic oscillator | $\xi^2$ | $1$ | $1/2$ | $\mathbf{2}$ | $O(c^{-1/2}(\log c)^{2})$ |
| Power $\|\xi\|^\nu$, $\nu > 0$ | $\xi^\nu$ | $\tfrac{2\nu}{\nu+2}$ | $\tfrac{\nu}{\nu+2}$ | $\tfrac{3\nu+2}{\nu+2}$ | $O(c^{-\nu/(\nu+2)}(\log c)^{(3\nu+2)/(\nu+2)})$ |
| Bessel-type | $\xi + c/\xi^2$ | $1$ | $1/3$ | $\mathbf{2}$ | $O(c^{-1/3}(\log c)^{2})$ |

**Check:** Airy row recovers XIX `cor:lograte` exactly. ✓  
**Limiting cases:**  
- $\nu \to \infty$ (hard wall): $\gamma \to 2$, $1+\gamma \to 3$ — steeper cost.  
- $\nu \to 0$ (flat potential): $\gamma \to 0$, $1+\gamma \to 1$ — logarithmic only, no power.

---

## §5. Conceptual Framing

### What XIX showed
> Logarithmic losses are unavoidable because of spectral geometry.

### What XX shows
> The logarithmic exponent is exactly $1+\gamma$,
> the spectral growth exponent of the turning-point model.

This is conceptually stronger: the truncation rate becomes a
**spectral invariant** — a quantity that depends only on the
asymptotic eigenvalue spacing, not on the specific form of $V$
or the functional-analytic details of the approximation.

The correct title framing for XX is therefore:

> *A universality principle for two-scale truncation in
> turning-point problems.*

Not "further application of XIX" but a genuine structural theorem.

---

## §6. Open Questions Inherited into XX

| Question | Origin | Status |
|---|---|---|
| $K$-uniform Langer bound: $C'(M,K) = O(M)$? | XIX `rem:logloss` | Open; if proved, rate sharpens to $O(c^{-\beta}\log c)$ |
| Is $\beta = \beta(\gamma)$ or independent? | XX §1.3 | To be determined per operator class |
| Does the $K^{1+\gamma}$ exponent saturate? | — | Likely yes; lower bound argument needed |
| Extension to systems (matrix SL)? | — | Out of scope for XX |

---

## §7. Scope Boundaries

| **In scope** | **Out of scope** |
|---|---|
| One-dimensional, self-adjoint | Multi-dimensional |
| Simple turning point | Higher-order / degenerate turning points |
| Real potential, semibounded | Non-self-adjoint, non-semibounded |
| Compact restriction $[0,M]$ | Global $\mathbb{R}_+$ estimates |
| Spectral growth hypothesis $a_K \sim K^\gamma$ | Sub-polynomial or oscillatory spectra |
| $K$-uniform Langer (as optional lemma) | Random, stochastic, nonlinear operators |

---

## §8. First Action

Begin with **§2 (dependency analysis)** as a standalone lemma:

> *Lemma `lem:gamma_agnostic`: Every node in the XVIII/XIX DAG
> except the four $\gamma$-sensitive nodes of §2.2 holds verbatim
> for any $\mathcal{A}_\gamma$ satisfying the spectral growth hypothesis.*

This lemma, once written, makes the universalisation a one-lemma
replacement (`lem:trunc_universal`) rather than a structural rebuild.

---

*End of scaffold. No results frozen here.*  
*Predecessor freezes: XVIII `d7609d2`/`19f5742`, XIX `580016b`.*
