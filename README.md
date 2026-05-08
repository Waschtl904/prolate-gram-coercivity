# prolate-gram-coercivity

A programme of eight (now twenty) papers establishing coercivity, spectral
properties, and universality of the prolate spheroidal wave function (PSWF)
Gram matrix, culminating in a quantitative two-scale convergence rate for
Airy kernel universality and its universal generalisation.

---

## Layer-Survival Selection Principle

> **The leading logarithmic exponent is selected not by maximal $K$-growth,
> but by the highest interaction layer surviving the $c$-scaling hierarchy.**

This is the central result of Papers XVIII–XX and the mathematical leitmotif
of the programme. It explains:

- **Why** the rate exponent is $1+\gamma$ (linear interaction layer)
  and not $1+2\gamma$ (quadratic interaction layer), even though
  $1+2\gamma > 1+\gamma$ algebraically.
- **How** logarithmic truncation losses arise: they trace the Airy zero
  spacing $a_K \sim K^\gamma$ propagating through the coercivity spine
  into $C_{\rm lin} = O(K^{1+\gamma})$.
- **What** the asymptotic hierarchy is: the quadratic layer $O(K^{1+2\gamma})
  c^{-2\beta}$ is suppressed by one extra factor $c^{-\beta}$ relative to the
  linear layer $O(K^{1+\gamma}) c^{-\beta}$, placing it below the $c$-horizon
  at the optimal coupling $K_{\rm opt} \sim (2\beta/\alpha) \log c$.

---

## Programme Structure

| Paper | File | Content | Status |
|-------|------|---------|--------|
| I | `paper1.tex` | Gram matrix basics | frozen |
| II | `paper2.tex` | Coercivity lower bound | frozen |
| II-Q | `paper2_quadrature.tex` | Quadrature estimates | frozen |
| III | `paper3.tex` | Spectral gap | frozen |
| IV | `paper4_semiclassical.tex` | Semiclassical analysis | frozen |
| V | `paper5.tex` | Scale separation | frozen |
| VI | `paper6.tex` | Fredholm theory | frozen |
| VII | `paper7_skeleton.tex` | Skeleton lemmas | frozen |
| VIII | `paper8_scale_separated.tex` | Scale-separated regime | frozen |
| IX | `paper9_superconcentration.tex` | Superconcentration | frozen |
| X | `paper10_coercivity_gap.tex` | Coercivity gap | frozen |
| XI | `paper11_fredholm_microlocal.tex` | Fredholm–microlocal | frozen |
| XII | `paper12_direct_coercivity.tex` | Direct coercivity | frozen |
| XIII | `paper13_gap_s.tex` | Gap-s lemma | frozen |
| XIV | `paper14_airy_resolvent.tex` | Airy resolvent | frozen |
| XV | `paper15_quasimode.tex` | Quasimode construction | frozen |
| XVI | `paper16_bridge.tex` | Bridge lemma | frozen |
| XVII | `paper17_cliff.tex` | Cliff estimates | frozen |
| XVIII | `paper18_airy_universality.tex` | BR3: qualitative Airy universality | **FROZEN d7609d2** |
| XIX | `paper19_quantitative_rate.tex` | Two-scale rate; $C_{\rm lin}$/$C_{\rm quad}$ split; $O(c^{-1/3}(\log c)^{5/3})$ | **FROZEN** |
| XX | `paper20_universality.tex` | Universality and Structural Rigidity of Turning-Point Truncation Geometry | **arXiv-ready** |

---

## The Trilogy (XVIII–XX): Core Mathematical Content

### XVIII — Qualitative universality
Establishes $\|K_{B_c} - K_{\mathcal{A}}\|_{L^2(w\otimes w)} \to 0$ (BR3)
via two-scale decomposition $S_K - K_{\mathcal{A}} = A_K - B_K$.
No rate; iterated limit structure $(c\to\infty$, then $K\to\infty)$.

### XIX — Quantitative two-scale rate
The Langer term $A_K$ splits into two interaction layers:
$$
A_K = A_K^{\rm lin} + A_K^{\rm quad},
$$
$$
\|A_K^{\rm lin}\| \leq C_{\rm lin}\cdot c^{-1/3}, \quad
\|A_K^{\rm quad}\| \leq C_{\rm quad}\cdot c^{-2/3},
$$
with $C_{\rm lin} = O(K^{5/3})$, $C_{\rm quad} = O(K^{7/3})$.
At $K_{\rm opt} \sim (\log c)/(3\alpha)$: rate $O(c^{-1/3}(\log c)^{5/3})$.
The quadratic layer is subleading by $c^{-1/3}$.

### XX — Universal layer-survival mechanism
For any $\mathcal{A}_\gamma \in \mathfrak{T}_\gamma$
(spectral growth $a_K \sim K^\gamma$, turning-point window $c^{-\beta}$):
$$
C_{\rm lin} = O(K^{1+\gamma}), \quad C_{\rm quad} = O(K^{1+2\gamma}).
$$
At $K_{\rm opt} \sim (2\beta/\alpha)\log c$:
$$
\|K_{B_c} - K_{\mathcal{A}_\gamma}\| = O\!\left(c^{-\beta}(\log c)^{1+\gamma}\right).
$$
The Layer-Survival Selection Principle explains the selection
mechanism: $1+2\gamma > 1+\gamma$ algebraically, but the quadratic
layer pays $c^{-2\beta}$ (two Langer errors) and falls below the
$c$-horizon at $K_{\rm opt}$.

Paper XX additionally introduces the method class $\mathcal{M}(\mathrm{S1,S2,S3})$,
the realization map $\mathfrak{R}: \mathcal{B} \to \mathcal{S}/\!\sim_{\mathcal{S}}$,
and establishes a structural rigidity theorem: no method in
$\mathcal{M}(\mathrm{S1,S2,S3})$ achieves a rate $o(c^{-\beta}(\log c)^{1+\gamma})$.

---

## Propagation Spine

```
a_K ~ K^gamma  -->  mu(K) ~ K^gamma  -->  C_hat ~ K^gamma
                                              |
                          x K * C_inf (lin)  |   x K * C_hat (quad)
                                    v                  v
              C_lin ~ K^{1+gamma}          C_quad ~ K^{1+2*gamma}
                      c^{-beta}                    c^{-2*beta}
                   [SURVIVES K_opt]         [BELOW c-HORIZON at K_opt]
```

---

## Key Parameters

| Symbol | Meaning | Airy value |
|--------|---------|------------|
| $\gamma$ | Spectral growth exponent ($a_K \sim K^\gamma$) | $2/3$ |
| $\beta$ | Turning-point window ($c^{-\beta}$ per Langer error) | $1/3$ |
| $\alpha$ | Slepian tail decay rate | $>0$ (XVIII) |
| $1+\gamma$ | Leading log-exponent (linear layer) | $5/3$ |
| $1+2\gamma$ | Subleading log-exponent (quadratic layer) | $7/3$ |
| $K_{\rm opt}$ | Optimal truncation | $\sim (2\beta/\alpha)\log c$ |

---

## Model Family $V = |\xi|^\nu$

| $\nu$ | $\gamma$ | $\beta$ | $1+\gamma$ (leading) | $1+2\gamma$ (subleading) |
|-------|---------|---------|----------------------|-------------------------|
| $1$ (Airy) | $2/3$ | $1/3$ | $5/3$ | $7/3$ |
| $2$ (harmonic) | $1$ | $1/2$ | $2$ | $3$ |
| $\nu$ | $2\nu/(\nu+2)$ | $\nu/(\nu+2)$ | $(3\nu+2)/(\nu+2)$ | $(5\nu+2)/(\nu+2)$ |
| $\nu\to\infty$ | $\to 2$ | $\to 1$ | $\to 3$ | $\to 5$ |

---

## Open Problems

Open problems are classified and maintained in [`RESEARCH_DIRECTIONS.md`](RESEARCH_DIRECTIONS.md).
The two primary open directions after Paper XX are:

- **O1** — Necessity of H1 (envelope minimality within $\mathcal{M}(\mathrm{S1,S2,S3})$):
  does $f(j) = o(1)$ in the eigenfunction bound improve the rate?
  Reduces to the question of which information survives the S3 diagonal
  projection $j \mapsto K^*(c) \sim (2\beta/\alpha)\log c$.

- **O3a** — Rate optimality outside $\mathcal{M}(\mathrm{S1,S2,S3})$:
  does there exist a method outside the class achieving
  $o(c^{-\beta}(\log c)^{1+\gamma})$? Requires an information-theoretic
  or semiclassical lower bound, beyond the Tauberian argument of Paper XX.

Additional directions (realization problem for $\rho \neq 0$ classes,
S2$^\epsilon$ stability) are documented in `RESEARCH_DIRECTIONS.md`.

---

*Programme: prolate-gram-coercivity. Author: Sebastian Schmalnauer, Vienna. May 2026.*
