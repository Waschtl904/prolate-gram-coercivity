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
Slowly varying functions are exactly the objects that remain visible under logarithmic compression.

**Likely approach:** Reverse FOC; $f(K^*(c)) \to 0$ either shifts $K^*(c)$ to absorb the gain
or forces $c$-inadmissibility.

---

## Direction 2 — Outside $\mathcal{M}(\mathrm{S1,S2,S3})$: O3a

**Current status:** Open. Tauberian $\to$ information-theoretic mode shift required.
Candidate approaches: eigenfunction localization, Kolmogorov widths,
semiclassical barrier, entropy lower bounds.

---

## Direction 3 — Asymptotic Projection Theory

### 3.1 The three-level structure of S2 *(2026-05-08)*

| Level | Content | Character |
|---|---|---|
| Analytic | EM remainder control | Model-dependent |
| Asymptotic | Scale-stability of $A(K,c)$ | Structural |
| Functional | $\mathfrak{R} \circ \mathrm{Res}_\lambda = \mathfrak{R}$ | Categorical |

**Scale-stability criterion:**
$A(K,c)$ induces a well-defined class under $\mathfrak{R}$
$\iff$
$\sup_{c \geq c_0} A(K, \lambda c)/A(K,c) < \infty$,
$\forall \lambda > 0$, uniformly on the diagonal.

### 3.2 Covariant projection and the $\rho$-classification *(2026-05-08)*

Karamata: $A(K,\lambda c)/A(K,c) \to \lambda^\rho$ $\Rightarrow$ $A(K,c) = c^\rho \ell(c)$, $\ell$ slowly varying.

$$\rho = 0:\quad
\mathfrak{R}(b(\cdot,\lambda c)) = \mathfrak{R}(b(\cdot,c))
\qquad\text{(invariant projection, Paper XX)}$$

$$\rho \neq 0:\quad
\mathfrak{R}^\rho(b(\cdot,\lambda c)) = \lambda^\rho\, \mathfrak{R}^\rho(b(\cdot,c))
\qquad\text{(covariant projection)}$$

The collapse of $c$-uniform stability has asymptotic geometry parametrized by $\rho$:
S2 does not fail randomly; it fails along a definite orbit of the rescaling group.

**Conjecture (Twisted rigidity):**
Under $\mathfrak{R}^\rho$, the balance fixed-point forces rate
$O(c^{-(\beta-\rho)}(\log c)^{1+\gamma})$.
Rigidity holds within each $\rho$-class; crossing classes changes the asymptotic geometry.

### 3.3 S2 as projective invariance

> **S2 is the statement that the asymptotic geometry has a stable projection
> structure under the rescaling group.**
> EM realizes this. The invariance
> $\mathfrak{R} \circ \mathrm{Res}_\lambda = \mathfrak{R}$
> is the actual mathematical content of S2.

---

## Direction 4 — Categorical Sketch *(2026-05-08)*

*This section records a structural observation made during the session of 2026-05-08.
It is a sketch, not a theorem. The purpose is to fix the objects before the intuition dissipates.*

### 4.1 The group action

Let $G = (\mathbb{R}_{>0}, \cdot)$ act on the space of analytic bounds $\mathcal{B}$ by
$$\mathrm{Res}_\lambda(b)(K,c) := b(K, \lambda c), \qquad \lambda \in G.$$
This is a group action: $\mathrm{Res}_\lambda \circ \mathrm{Res}_\mu = \mathrm{Res}_{\lambda\mu}$.

The **orbit** of $b \in \mathcal{B}$ under $G$ is
$\{b(\cdot, \lambda c) : \lambda > 0\} \subseteq \mathcal{B}$.

### 4.2 S2 as functoriality of $\mathfrak{R}$

$\mathfrak{R}$ is $G$-**equivariant** (i.e. functorial with respect to the $G$-action) iff
$$\mathfrak{R}(\mathrm{Res}_\lambda(b)) = \mathfrak{R}(b) \quad \forall \lambda \in G.$$
This is exactly S2: the projection $\mathfrak{R}$ does not distinguish between
bounds in the same $G$-orbit (when $\rho = 0$).

Without S2 ($\rho \neq 0$): $\mathfrak{R}^\rho$ is not equivariant but *$\rho$-covariant*:
$$\mathfrak{R}^\rho(\mathrm{Res}_\lambda(b)) = \lambda^\rho \cdot \mathfrak{R}^\rho(b).$$
This is a *twisted equivariance* or *equivariance with character $\chi_\rho(\lambda) = \lambda^\rho$*.

The characters $\chi_\rho : G \to \mathbb{R}_{>0}$, $\lambda \mapsto \lambda^\rho$
classify the one-dimensional representations of $G = (\mathbb{R}_{>0}, \cdot)$.
The $\rho$-classification is therefore the **representation-theoretic classification**
of how $\mathfrak{R}$ can transform under $G$.

### 4.3 S3 as a section

The diagonal $K^*(c)$ is a **section** of the projection
$\mathcal{B} \to \mathcal{B}/G$ (bounds modulo rescaling):
it selects one representative from each $c$-family of bounds.

More precisely: S3 licenses the map
$$b(K, c) \longmapsto b(K^*(c), c),$$
which is a **section** in the sense that it picks a canonical point
on the diagonal $\{K = K^*(c)\}$ inside the two-dimensional parameter space $(K, c)$.

The diagonal rate $c^{-\beta}(\log c)^{1+\gamma}$ is the **value of $\mathfrak{R}$ on this section**.

### 4.4 The full categorical picture

The programme can now be described as:

> A $G$-space $\mathcal{B}$ of analytic bounds,
> a $G$-equivariant map $\mathfrak{R}: \mathcal{B} \to \mathcal{S}/\!\sim$
> (S2 = equivariance, $\rho = 0$),
> a section $\sigma: \mathcal{B}/G \to \mathcal{B}$ induced by S3 (diagonal $K^*(c)$),
> and a preorder $\succ$ on the target $\mathcal{S}/\!\sim$.
> The rate theorem is: $\mathfrak{R}(\sigma(b)) \asymp \phi_{\beta, 1+\gamma}$.

The **obstruction theorem** (Thm. `thm:rate_obstruction`) states:
no element of $\mathcal{B}$ satisfying S1--S3 maps under $\mathfrak{R} \circ \sigma$
to a class $\prec \phi_{\beta, 1+\gamma}$.

**The twisted theory** replaces $G$-equivariance by $\chi_\rho$-covariance;
the rate shifts by the character exponent $\rho$.

### 4.5 What this is not (yet)

- This is not a formal category-theoretic argument. The objects are not equipped
  with morphisms beyond what is needed for the above.
- The section $\sigma$ is not unique; S3 licenses *a* section, not a canonical one.
- The $\rho$-classification assumes the Karamata limit exists;
  the case of non-regularly-varying prefactors is not covered.

These are the boundaries of the sketch. The sketch is included
because it identifies the *type* of each object in the programme
without which the connections to external theory (regular variation,
representation theory of $\mathbb{R}_{>0}$) would remain informal.

---

## Asymptotic Mechanics: programme summary *(2026-05-08)*

| Object | Role | Categorical type |
|---|---|---|
| $\mathfrak{R}$ | Projection: bounds $\to$ classes | $G$-equivariant map |
| S2 | Invariance: $\mathfrak{R} \circ \mathrm{Res}_\lambda = \mathfrak{R}$ | Equivariance condition ($\rho=0$) |
| $\rho$-classes | Defect classification | Characters of $G = (\mathbb{R}_{>0},\cdot)$ |
| S3 / diagonal | Compression + section | Section of $\mathcal{B} \to \mathcal{B}/G$ |
| O1 | Residual: what survives the section? | Fidelity of $\mathfrak{R}$ on $\mathrm{Im}(\sigma)$ |
| Regular variation | Functor class for $\rho$-deformations | Rep theory of $G$ |

**Central principle:**
Every object is a projection, an equivariance condition, a character of the
rescaling group, or a section. There are no ad-hoc constructions.

**The $\rho = 0$ spine:**
$$\mathcal{B}
\xrightarrow{\mathfrak{R}}
\mathcal{S}/\!\sim
\xrightarrow{\succ}
\text{comparison}
\xrightarrow{\sigma}
c^{-\beta}(\log c)^{1+\gamma}$$

**The $\rho \neq 0$ deformation:**
$$\mathcal{B}
\xrightarrow{\mathfrak{R}^\rho}
\mathcal{S}^\rho/\!\sim
\xrightarrow{\succ}
\text{comparison}
\xrightarrow{\sigma}
c^{-(\beta-\rho)}(\log c)^{1+\gamma}$$

Paper XX is the complete treatment of the $\rho = 0$ spine.
The twisted theory extends this to the full $\rho$-fibration over characters of $G$.

---

## Dependency structure

```
O1 = projection fidelity on Im(sigma), rho=0
  -> requires: reverse FOC on f(K*(c))

O3a = leaving rho=0 class, information-theoretic proof mode

Direction 3 / twisted theory
  -> rho=0: Paper XX (equivariant projection)
  -> rho!=0: covariant projection, character rho
  -> full: rho-fibration = rep theory of (R_{>0}, *)

Categorical sketch (Direction 4)
  -> gives type of each object
  -> prerequisite for connecting to external theory
  -> not yet: formal morphisms, non-Karamata cases, canonical section
```

---

## Priority assessment

| Direction | Horizon | Closes claim? | Paper? |
|---|---|---|---|
| O1 | Medium | Yes | XXI |
| O3a | Long | No | With H3 |
| Dir. 3 ($\rho=0$) | Medium–Long | No | XXI–XXII |
| Dir. 3 (twisted) | Long | No | XXII–XXIII |
| Dir. 4 (categorical) | Very long | No | XXIII+ |

*O1 first. The categorical sketch (Direction 4) is recorded here as a foundation,
not as a target. Its role is to fix the types so that future work
can build on named objects rather than rediscover the connections.*
