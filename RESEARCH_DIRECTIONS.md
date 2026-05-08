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

$$\text{EM remainder control}
\;\Longrightarrow\; \text{scale-stability of } A(K,c)
\;\Longrightarrow\; \mathfrak{R} \circ \mathrm{Res}_\lambda = \mathfrak{R}.$$

**Scale-stability criterion:**
$A(K,c)$ induces a well-defined class under $\mathfrak{R}$
$\iff$
$\sup_{c \geq c_0} A(K, \lambda c)/A(K,c) < \infty$
$\forall \lambda > 0$, uniformly on the diagonal.

### 3.2 Covariant projection and the $\rho$-classification *(2026-05-08)*

The $\rho = 0$ condition (S2, Paper XX) is one point in a continuous family.
Suppose $A(K,\lambda c)/A(K,c) \to L(\lambda)$.
By the Cauchy functional equation, $L(\lambda) = \lambda^\rho$.
Karamata representation: $A(K,c) = c^\rho \ell(c)$, $\ell$ slowly varying.

**The two projection regimes:**

$$\rho = 0:\quad
\mathfrak{R}(b(\cdot,\lambda c)) = \mathfrak{R}(b(\cdot,c))
\qquad\text{(invariant projection, Paper XX)}$$

$$\rho \neq 0:\quad
\mathfrak{R}^\rho(b(\cdot,\lambda c)) = \lambda^\rho\, \mathfrak{R}^\rho(b(\cdot,c))
\qquad\text{(covariant projection)}$$

This is not a weakening of stability but a **classification of the defect**:
the collapse of $c$-uniform stability itself has asymptotic geometry, parametrized by $\rho$.

**Consequence:** The effective exponent shifts:
$c^{-\beta} \mapsto c^{-(\beta-\rho)}$.
The projection map remains structurally present but is no longer invariant
under rescaling — it is *covariant*, transforming by $\lambda^\rho$.

**Conjecture (Twisted rigidity):**
For each $\rho \in \mathbb{R}$, the balance fixed-point under $\mathfrak{R}^\rho$
forces the diagonal rate $O(c^{-(\beta-\rho)}(\log c)^{1+\gamma})$.
Structural rigidity holds within each $\rho$-class;
crossing $\rho$-classes is a genuine change in asymptotic geometry.

**Critical observation:**
S2 is not replaced by something weaker in the $\rho \neq 0$ case.
S2 *fails* — but the failure is structured.
The $\rho$-parameter measures *how* it fails.

### 3.3 S2 as projective invariance *(2026-05-08)*

> **S2 is the statement that the asymptotic geometry possesses
> a stable projection structure under the rescaling group.**
> EM is one mechanism realizing this. The invariance
> $\mathfrak{R} \circ \mathrm{Res}_\lambda = \mathfrak{R}$
> is the actual mathematical content of S2.

| Formulation | Status |
|---|---|
| EM structural property (Paper XX) | Concrete, WKB-specific |
| $A(K,c)$ asymptotically scale-stable | Structural, generalizes |
| $\mathfrak{R} \circ \mathrm{Res}_\lambda = \mathfrak{R}$ | Categorical, fully general |

### 3.4 The five structural questions *(updated 2026-05-08)*

1. **Well-definedness:** $\mathfrak{R}^\rho(b)$ exists $\iff$ $A$ has definite rescaling exponent $\rho$.
2. **Stability axioms:** is $\{$leading-power extraction, uniform remainder, $\rho$-homogeneity$\}$ complete?
3. **Projection fidelity:** when does $\mathfrak{R}^\rho(b_1 + b_2) = \mathfrak{R}^\rho(b_1)$?
4. **Collapse:** deformations breaking $\rho$-homogeneity destroy $\mathfrak{R}^\rho$ while preserving $\succ$.
   (`lem:S2_knockdown` in abstract form.)
5. **Method equivalence:** two methods are *projectively equivalent* if they induce the same $\rho$ and $\mathfrak{R}^\rho$.

### 3.5 Connections

| Theory | Connection |
|---|---|
| Regular variation (BGT) | $\rho = 0$: slowly varying = scale-stable |
| Karamata representation | $A(K,c) = c^\rho \ell(c)$ is the structure theorem |
| Regularly varying functions | $\rho \neq 0$ class |
| Tauberian theorems | Sufficient conditions for $\mathfrak{R}^\rho$ well-defined |
| Renormalization group | Rescaling orbits; $\rho = 0$ = fixed point |
| Asymptotic algebras | Structure of $\bigsqcup_\rho \mathcal{S}^\rho/\!\sim$ |

---

## Asymptotic Mechanics: a programme summary *(2026-05-08)*

The six objects below now interact as a coherent language, not as isolated constructions.

| Object | Role |
|---|---|
| $\mathfrak{R}$ | Projection: analytic bounds $\to$ asymptotic classes |
| S2 | Invariance: $\mathfrak{R}$ commutes with rescaling ($\rho = 0$) |
| $\rho$-classes | Defect classification: structured failure of S2 |
| S3 / diagonal compression | Compression: reduces all degrees of freedom to behavior on $j \sim \frac{2\beta}{\alpha}\log c$ |
| O1 | Residual problem: what survives the S3 projection? |
| Regular variation | Natural functor class for $\rho$-deformations |

**The central principle:**
Every object in the programme is either a projection, an invariance condition,
a defect of that invariance, or a compression that forces the relevant scale.
There are no ad-hoc constructions.

**The $\rho = 0$ spine:**
$$\text{analytic bounds}
\xrightarrow{\mathfrak{R}}
\mathcal{S}/\!\sim_{\mathcal{S}}
\xrightarrow{\succ}
\text{comparison}
\xrightarrow{\text{S3}}
\text{diagonal rate } c^{-\beta}(\log c)^{1+\gamma}$$

**The $\rho \neq 0$ deformation:**
$$\text{analytic bounds}
\xrightarrow{\mathfrak{R}^\rho}
\mathcal{S}^\rho/\!\sim
\xrightarrow{\succ}
\text{comparison}
\xrightarrow{\text{S3}}
\text{diagonal rate } c^{-(\beta-\rho)}(\log c)^{1+\gamma}$$

Paper XX is the complete treatment of the $\rho = 0$ spine.
The twisted theory extends this to the full $\rho$-fibration.

---

## Dependency structure

```
O1 (envelope minimality = information survival under S3 compression)
  └── rho=0, question about projection fidelity under f-perturbation
  └── requires: reverse FOC analysis on f(K*(c))

O3a (outside M)
  └── = leaving the rho=0 class entirely
  └── requires: localization / entropy / semiclassical

Direction 3 (asymptotic projection theory)
  └── rho=0 spine: Paper XX
  └── rho!=0: twisted realization = covariant projection
  └── full theory: rho-fibration over asymptotic geometries
  └── connects to regular variation, Karamata, renormalization
```

---

## Priority assessment

| Direction | Horizon | Closes open claim? | Paper? |
|---|---|---|---|
| O1 | Medium | Yes (necessity in XX) | XXI |
| O3a | Long | No | With H3 |
| Dir. 3 ($\rho=0$) | Medium–Long | No | XXI–XXII |
| Dir. 3 (twisted, $\rho\neq 0$) | Long | No | XXII–XXIII |

*O1 first. Direction 3 at $\rho=0$ is the natural continuation.
The twisted theory is the long horizon giving the full fibration.*
