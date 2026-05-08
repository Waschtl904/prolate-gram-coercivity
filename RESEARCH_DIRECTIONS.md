# Research Directions after Paper XX

*Status: May 2026. Paper XX internally complete; arXiv submission pending.*

---

## Direction 1 — O1: H1 Envelope Minimality

**Current status:** Sufficiency is a theorem (Thm. `thm:universal_rate`).
Necessity is open. Airy case confirmed.

**The diagonal compression observation** *(2026-05-08)*

After substitution $j \mapsto K^*(c) \sim \frac{2\beta}{\alpha} \log c$,
improvements survive only as $f(K^*(c))$. Trichotomy:

- **Algebraic:** $f(j) = j^{-\epsilon}$ $\Rightarrow$ $f(K^*(c)) = (\log c)^{-\epsilon}$. Survives.
- **Slowly varying:** $f(j) = (\log j)^{-\delta}$ $\Rightarrow$ $f(K^*(c)) = (\log\log c)^{-\delta}$. Partially survives.
- **Sub-slowly-varying:** $f(j) = (\log\log j)^{-\delta}$ $\Rightarrow$ frozen.

**S3 compression principle:** O1 = *which information survives the S3 diagonal projection?*

**Likely approach:** Reverse FOC; $f(K^*(c)) \to 0$ either shifts $K^*(c)$ to absorb the gain
or forces $c$-inadmissibility.

---

## Direction 2 — Outside $\mathcal{M}(\mathrm{S1,S2,S3})$: O3a

**Current status:** Open. Tauberian $\to$ information-theoretic mode shift required.
Candidate approaches: eigenfunction localization, Kolmogorov widths,
semiclassical barrier, entropy lower bounds.

---

## Direction 3 — Asymptotic Projection Theory

### 3.1 Three-level structure of S2 *(2026-05-08)*

| Level | Content | Character |
|---|---|---|
| Analytic | EM remainder control | Model-dependent |
| Asymptotic | Scale-stability of $A(K,c)$ | Structural |
| Functional | $\mathfrak{R} \circ \mathrm{Res}_\lambda = \mathfrak{R}$ | Categorical |

**Scale-stability criterion:**
$A(K,c)$ induces a well-defined class under $\mathfrak{R}$
$\iff$
$\sup_{c} A(K,\lambda c)/A(K,c) < \infty$, $\forall \lambda > 0$, uniformly on the diagonal.

### 3.2 Covariant projection and $\rho$-classification *(2026-05-08)*

Karamata: $A(K,\lambda c)/A(K,c) \to \lambda^\rho$ $\Rightarrow$ $A(K,c) = c^\rho \ell(c)$.

$$\rho = 0:\; \mathfrak{R}(b(\cdot,\lambda c)) = \mathfrak{R}(b(\cdot,c)) \qquad \text{(invariant, Paper XX)}$$
$$\rho \neq 0:\; \mathfrak{R}^\rho(b(\cdot,\lambda c)) = \lambda^\rho \mathfrak{R}^\rho(b(\cdot,c)) \qquad \text{(covariant)}$$

**Conjecture (Twisted rigidity):**
Under $\mathfrak{R}^\rho$, balance fixed-point forces rate $O(c^{-(\beta-\rho)}(\log c)^{1+\gamma})$.

### 3.3 S2 as projective invariance

> **S2** = stable projection structure under the rescaling group.
> $\mathfrak{R} \circ \mathrm{Res}_\lambda = \mathfrak{R}$ is the actual content of S2.

---

## Direction 4 — Categorical Sketch *(2026-05-08)*

### 4.1 Group action

$G = (\mathbb{R}_{>0}, \cdot)$ acts on $\mathcal{B}$ by $\mathrm{Res}_\lambda(b)(K,c) := b(K,\lambda c)$.

### 4.2 S2 as equivariance / covariance

$\rho = 0$: $\mathfrak{R}$ is $G$-equivariant. S2 = equivariance condition.

$\rho \neq 0$: $\mathfrak{R}^\rho$ is $\chi_\rho$-covariant, $\chi_\rho(\lambda) = \lambda^\rho$.
The characters $\chi_\rho$ classify the 1-dimensional representations of $G$.
The $\rho$-classification = **representation-theoretic classification** of $\mathfrak{R}$-behavior under $G$.

### 4.3 S3 as section

$K^*(c)$ is a **section** of $\mathcal{B} \to \mathcal{B}/G$:
it selects a canonical representative on the diagonal $\{K = K^*(c)\}$.
The diagonal rate = value of $\mathfrak{R}$ on this section.

### 4.4 Full picture

> $G$-space $\mathcal{B}$,
> $G$-equivariant $\mathfrak{R}: \mathcal{B} \to \mathcal{S}/\!\sim$ (S2),
> section $\sigma$ induced by S3,
> preorder $\succ$ on target.
> Rate theorem: $\mathfrak{R}(\sigma(b)) \asymp \phi_{\beta,1+\gamma}$.
> Obstruction: nothing in $\mathrm{Im}(\sigma)$ maps $\prec \phi_{\beta,1+\gamma}$.

### 4.5 What this is not (yet)

- No formal morphisms beyond what is needed above.
- $\sigma$ is not canonical: S3 licenses *a* section, not a unique one.
- $\rho$-classification requires existence of the Karamata limit;
  non-regularly-varying prefactors are not covered.

---

## Direction 5 — The Two Next Mathematical Problems *(2026-05-08)*

*Within the established language, exactly two directions remain open at the level of*
*new mathematical content (as opposed to new notation or new examples).*

### 5.1 Realization problem: which operator classes carry $\rho \neq 0$?

**Question:** Does there exist an operator class $\mathfrak{T}^\rho_\gamma$
(some modification of $\mathfrak{T}_\gamma$ or a genuinely different class)
for which the natural analytic bounds satisfy
$A(K,c) = c^\rho \ell(c)$ with $\rho \neq 0$?

**What would this require:**
A bound of the form $\|e_j\|_{C^0} \leq C_0 j^\gamma c^{\rho - \beta}$ with $\rho \neq 0$,
i.e. a *sub-optimal* pointwise control that grows polynomially in $c$.
This could arise from:
- operators with $c$-dependent potential: $V = V_c(\xi)$
- multi-parameter families where $c$ enters the operator definition
- perturbation of $\mathfrak{T}_\gamma$ operators by $c$-dependent terms

**Why this matters:**
If $\rho \neq 0$ classes are vacuous (no natural operator carries them),
the twisted theory is formally complete but physically empty.
If they are non-vacuous, the $\rho$-fibration becomes a genuine
classification of operator-analytic complexity.

**First candidate:** Operators with $c$-dependent turning point $\xi_0(c)$.
The Langer transformation introduces $c$-dependence into the eigenfunction bounds;
the resulting prefactor may carry $\rho \neq 0$.

### 5.2 Stability problem: which deformations preserve S2 in weak form?

**Question:** Is there a condition *weaker* than $\rho = 0$ (full equivariance)
that still allows the balance fixed-point argument to produce a *controlled* rate?

**Precise formulation:**
Let S2$^\epsilon$ denote the condition:
$$\frac{A(K, \lambda c)}{A(K,c)} \leq C \lambda^\epsilon \qquad \forall \lambda \geq 1,$$
for some $\epsilon > 0$ small. This is *near-equivariance*: the prefactor grows
at most polynomially in $\lambda$, but with a controlled exponent.

**Conjecture (S2$^\epsilon$ rigidity):**
Under S2$^\epsilon$, the balance fixed-point produces rate
$O(c^{-(\beta - \epsilon)}(\log c)^{1+\gamma})$,
where the effective exponent shift is exactly $\epsilon$.
For $\epsilon \to 0$: recovers the Paper XX result.
For $\epsilon = \rho$: recovers the twisted theory.

**Why this is the stability problem:**
It asks whether the Paper XX result is *stable* under small violations of S2,
or whether the rate jumps discontinuously.
If the rate degrades continuously with $\epsilon$,
the rigidity theorem is *stable* in the analytical sense.
If it jumps, S2 is a *sharp threshold* and not merely a convenient sufficient condition.

**Connection to O1:**
For the realization problem (5.1) and the stability problem (5.2)
to have consistent answers, the $\rho$-parameter should behave
like a continuous deformation parameter of the asymptotic geometry.
O1 would then be the $\epsilon = 0$ boundary case:
the threshold at which the geometry transitions from the $\rho = 0$ class
to the $\rho > 0$ class via slowly-varying corrections.

---

## Session closure: 2026-05-08

### What stabilized today

| Phase | Function |
|---|---|
| Paper XX (commits I–IV) | Fixpoint identification: $\rho = 0$ spine |
| Directions v1 | Problem space segmentation: O1, O3a, Dir. 3 |
| Directions v2 | Rescaling group made visible: scale-stability criterion |
| Directions v3 | Orbit structure introduced: covariant projection |
| Directions v4 | Categorical representation + boundary conditions |
| Directions v5 | Two next problems: realization and stability |

### What the theory now knows about itself

- Its own coordinates: $\mathfrak{R}$, $\rho$, S1/S2/S3, $K^*(c)$
- Its own forbidden moves: non-canonical sections, non-Karamata prefactors,
  category-theory beyond types
- Its own deformation space: the $\rho$-fibration over $\mathrm{Hom}(G, \mathbb{R}_{>0})$
- Its own next problems: realization ($\rho \neq 0$ instances)
  and stability (near-equivariance threshold)

### The theory's status

This is no longer a paper programme in the classical sense.
It is a small asymptotic theory with controlled syntax,
classified deformations, and two open problems
that are *internal* to its own language.

The next paper (Paper XXI) will either:
- close O1 (necessity of H1), or
- establish the first $\rho \neq 0$ realization,

depending on which problem yields first.

---

## Priority

| Direction | Horizon | Paper? |
|---|---|---|
| O1 | Medium | XXI |
| Realization ($\rho \neq 0$) | Medium | XXI–XXII |
| Stability (S2$^\epsilon$) | Medium | XXII |
| O3a | Long | With H3 |
| Categorical (Dir. 4) | Very long | XXIII+ |
