# Research Directions after Paper XX

*Status: May 2026. Paper XX internally complete; arXiv submission pending.*

---

## Direction 1 — O1: H1 Envelope Minimality

**Current status:** Sufficiency is a theorem (Thm. `thm:universal_rate`).
Necessity is open. Airy case confirmed.

**The question:**
Does there exist a hypothesis
$$\|e_j\|_{C^0} \leq C_0 \, j^\gamma f(j) \, c^{-\beta}, \qquad f(j) = o(1) \text{ monotone},$$
that still yields $\Phi_1(K^*(c), c) = O(c^{-\beta}(\log c)^{1+\gamma})$
with $c$-admissible constants?

**The diagonal compression observation** *(2026-05-08)*

After substitution $j \mapsto K^*(c) \sim \frac{2\beta}{\alpha} \log c$,
improvements survive only as $f(K^*(c))$. Trichotomy:

- **Algebraic:** $f(j) = j^{-\epsilon}$ $\Rightarrow$ $f(K^*(c)) = (\log c)^{-\epsilon} \to 0$. Survives.
- **Slowly varying:** $f(j) = (\log j)^{-\delta}$ $\Rightarrow$ $f(K^*(c)) = (\log\log c)^{-\delta}$. Partially survives.
- **Sub-slowly-varying:** $f(j) = (\log\log j)^{-\delta}$ $\Rightarrow$ frozen under projection.

**S3 compression principle:** S3 is simultaneously a transfer mechanism
*and* a compression mechanism. O1 is the question:
> *Which information survives the S3 diagonal projection?*

**Likely approach:** Reverse FOC; show $f(K^*(c)) \to 0$ either shifts $K^*(c)$
to absorb the gain, or forces $c$-inadmissibility of the shifted prefactor.

---

## Direction 2 — Outside $\mathcal{M}(\mathrm{S1,S2,S3})$: O3a

**Current status:** Open. No lower bound claimed for $\mathcal{M}^c$.

**Mode shift** *(2026-05-08):* Tauberian $\to$ information-theoretic.
Candidate approaches: eigenfunction localization, Kolmogorov widths,
semiclassical barrier, entropy lower bounds.

---

## Direction 3 — Asymptotic Projection Theory

### 3.1 The three-level structure of S2

*(2026-05-08)*

| Level | Content | Character |
|---|---|---|
| Analytic | Concrete summation formula (EM) | Model-dependent |
| Asymptotic | Scale-stability of $A(K,c)$ | Structural |
| Functional | $\mathfrak{R}$ commutes with rescaling | Categorical |

The implication chain is:
$$\text{EM remainder control} \;\Longrightarrow\; \text{scale-stability of } A(K,c)
\;\Longrightarrow\; \mathfrak{R} \circ \mathrm{Res}_\lambda = \mathfrak{R}.$$
Only the last two levels generalize beyond WKB.
EM is one realization; the invariance $\mathfrak{R} \circ \mathrm{Res}_\lambda = \mathfrak{R}$
is the actual mathematical content of S2.

**Scale-stability criterion:**
$$A(K,c) \text{ induces a well-defined class under } \mathfrak{R}
\iff
\sup_{c \geq c_0} \frac{A(K, \lambda c)}{A(K,c)} < \infty
\quad \forall \lambda > 0, \text{ uniformly on the diagonal.}$$

### 3.2 Twisted realization theory

*(2026-05-08)*

**The degenerate case $\mathfrak{R} \circ \mathrm{Res}_\lambda = \mathfrak{R}$
is not the only interesting case.**

Suppose instead:
$$\frac{A(K, \lambda c)}{A(K,c)} \xrightarrow{c \to \infty} L(\lambda)$$
for some function $L: (0,\infty) \to (0,\infty)$.
By the standard argument, $L$ must satisfy the Cauchy functional equation
$L(\lambda\mu) = L(\lambda)L(\mu)$, so $L(\lambda) = \lambda^\rho$ for some $\rho \in \mathbb{R}$.

This gives a one-parameter family of *rescaling cocycles*:
$$\frac{A(K, \lambda c)}{A(K,c)} \sim \lambda^\rho, \qquad \rho \in \mathbb{R}.$$

- $\rho = 0$: scale-stable; $\mathfrak{R}$ well-defined. *Current Paper XX setting.*
- $\rho \neq 0$: $A(K,c)$ transforms as $c^\rho$ under rescaling;
  the image under $\mathfrak{R}$ shifts by $\phi_{s,t} \mapsto \phi_{s-\rho, t}$.
  The preorder $\succ$ is preserved (it is defined on index pairs),
  but the equivalence class assigned to the bound shifts with $\lambda$:
  $\mathfrak{R}$ is no longer a map to a single class, but to a *cocycle orbit*.

**Definition (Twisted realization map):**
For prefactor $A$ with rescaling exponent $\rho$, define
$$\mathfrak{R}^\rho(b) := [\phi_{s-\rho, t}]
\quad \text{if} \quad b(K^*(c), c) \sim_{\mathcal{S}} c^\rho \phi_{s,t}(c).$$
For $\rho = 0$ this recovers $\mathfrak{R}$ from Paper XX.

**Conjecture (Twisted rigidity):**
*For each $\rho \in \mathbb{R}$, the balance fixed-point equation
under $\mathfrak{R}^\rho$ forces the diagonal rate*
$$O\!\left(c^{-(\beta - \rho)}(\log c)^{1+\gamma}\right),$$
*with the effective exponent shifted by $\rho$.
Structural rigidity holds within each $\rho$-class;
the class itself is determined by the rescaling behavior of $A$.*

**Consequence:** the obstruction theorem generalizes: rate improvement
within a fixed $\rho$-class is impossible by the same balance argument;
crossing $\rho$-classes corresponds to a genuine change in
the asymptotic geometry of the bound.

### 3.3 S2 as projective invariance

The reformulation is now complete:

> **S2 is not the statement that EM gives good constants.**
> **S2 is the statement that the asymptotic geometry possesses
> a stable projection structure under the rescaling group.**

In this language:
- Paper XX establishes the $\rho = 0$ case.
- Twisted realization theory covers $\rho \neq 0$.
- The full theory classifies which asymptotic geometries
  arise from which rescaling-cocycle structure of the analytic bounds.

### 3.4 The five structural questions (updated)

1. **Well-definedness:** $\mathfrak{R}^\rho(b)$ exists $\iff$ $A$ has a definite rescaling exponent $\rho$.
2. **Stability axioms:** is $\{$leading-power extraction, uniform remainder, $\rho$-homogeneity$\}$ complete?
3. **Projection fidelity:** when does $\mathfrak{R}^\rho(b_1 + b_2) = \mathfrak{R}^\rho(b_1)$?
4. **Collapse:** deformations that break $\rho$-homogeneity destroy $\mathfrak{R}^\rho$
   while preserving $\succ$. (`lem:S2_knockdown` in abstract form.)
5. **Method equivalence:** two methods are *projectively equivalent* if
   they induce the same $\rho$ and the same $\mathfrak{R}^\rho$.

### 3.5 Connections to existing theory

| Existing theory | Connection |
|---|---|
| Regular variation (BGT) | Slowly varying = boundary case $\rho = 0$, $L(\lambda) \equiv 1$ |
| Regularly varying functions | $\rho \neq 0$ class: $A(K,\lambda c) \sim \lambda^\rho A(K,c)$ |
| Karamata representation | Structure theorem for $\rho$-homogeneous prefactors |
| Tauberian theorems | Sufficient conditions for $\mathfrak{R}^\rho$ to be well-defined |
| Renormalization group | Rescaling action on asymptotic classes; fixed points = $\rho = 0$ |
| Asymptotic algebras | Algebraic structure of $\bigsqcup_\rho \mathcal{S}^\rho/\!\sim$ |

---

## Dependency structure

```
O1 (envelope minimality = information survival under S3 compression)
  └── coupled to S3 via diagonal compression
  └── coupled to S2 via c-admissibility = rho=0 condition
  └── requires: reverse FOC analysis

O3a (outside M)
  └── requires: localization / entropy / semiclassical
  └── independent of O1

Direction 3 (asymptotic projection theory)
  └── rho=0: Paper XX (scale-stable, R well-defined)
  └── rho!=0: twisted realization theory (new)
  └── S2 = projective invariance under rescaling group
  └── connects to regular variation, Karamata, renormalization
  └── O1 = special case rho=0, question about fidelity under f-perturbation
  └── O3a = leaving rho=0 class entirely
```

---

## Priority assessment

| Direction | Horizon | Closes open claim? | Standalone paper? |
|---|---|---|---|
| O1 | Medium | Yes (necessity in XX) | Yes |
| O3a | Long | No | Possibly, with H3 |
| Dir. 3 ($\rho=0$ theory) | Medium–Long | No | Programme paper XXI |
| Dir. 3 (twisted, $\rho\neq 0$) | Long | No | Programme paper XXII? |

*O1 is the natural next target.
 Direction 3 at $\rho=0$ is the natural continuation of the programme language.
 The twisted theory is the long horizon that gives the full geometric picture.*
