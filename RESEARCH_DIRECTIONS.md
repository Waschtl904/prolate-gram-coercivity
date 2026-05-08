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

**Why this matters:**
This is the transition from
> "H1 is sufficient"

to
> "H1 is minimal within $\mathcal{M}(\mathrm{S1,S2,S3})$".

That shift has substantially more theoretical weight than further model examples.
It would close the axiom-economy question for the programme.

**Airy evidence:**
Abramowitz–Stegun §10.4 confirms $f(j) \equiv 1$ is tight for Airy.
The general argument requires understanding how $f(j)$ propagates
through the balance FOC — specifically whether
$(K^*(c))^{1+\gamma} f(K^*(c))$ can be made $o((\log c)^{1+\gamma})$.
Since $K^*(c) \sim \frac{2\beta}{\alpha} \log c$,
this becomes a question about $f(\log c)$,
i.e. whether $f$ can decay along the logarithmic diagonal.

**Likely approach:** Reverse FOC analysis;
show the balance condition forces $f(K^*(c)) \to$ const.

---

## Direction 2 — Outside $\mathcal{M}(\mathrm{S1,S2,S3})$: O3a

**Current status:** Open. No lower bound claimed for $\mathcal{M}^c$.

**The question:**
Is the logarithmic loss $(\log c)^{1+\gamma}$ a consequence
of the method class — or a deeper spectral-geometric phenomenon?

**Two sub-questions:**

**(O3a)** Does there exist a method outside $\mathcal{M}(\mathrm{S1,S2,S3})$
that achieves $o(c^{-\beta}(\log c)^{1+\gamma})$?
If yes: the obstruction is method-specific, not operator-intrinsic.
If no: the log-loss is a genuine spectral-geometric invariant.

**(O3b)** Can a uniform lower bound be established
(currently blocked by absence of H3)?

**Why this is the long-term question:**
The current rigidity theorem is a *Tauberian* statement:
given the three structural constraints, the scale is forced.
A genuine spectral lower bound would require a different proof strategy —
likely an information-theoretic or entropy argument on eigenfunction localization.

---

## Direction 3 — Asymptotic Projection Theory

**Current status:** $\mathfrak{R}$ is defined functionally in Paper XX
(Definition `def:realization_map`). Its abstract properties are not yet developed.

**The question:**
Which summation/approximation methods induce $c$-uniformly stable projections
$\mathfrak{R}: \mathcal{B} \to \mathcal{S}/{\sim_{\mathcal{S}}}$?

**Candidate abstract framework:**
A summation method $M$ acting on $\sum_{j=1}^K j^\sigma$
*induces a stable projection* if:
1. **Leading-power extraction:** $M[\sum j^\sigma] = a_\sigma K^{1+\sigma} + R_M(K)$
2. **Uniform remainder:** $|R_M(K)| \leq C_M K^{\sigma-1}$, $C_M$ independent of $K, c$
3. **Scaling invariance:** $C_M$ independent of all external parameters

Euler–Maclaurin is the canonical example.
The question is whether this is a *characterization* or merely a sufficient condition.

**Possible results:**
- Classification theorem: which methods satisfy (1)–(3)
- Stability functor: $\mathfrak{R}_M$ as a functor from summation methods to projection stability classes
- Obstruction: which structural deformations of $M$ destroy $c$-uniform stability

**Why this extends the theory rather than decorating it:**
The four-layer architecture (analytic / projective / asymptotic / ordinal)
is currently instantiated once, for WKB power-sum bounds.
A projection theory would make the framework reusable for other operator classes
where similar two-scale problems arise.

---

## Dependency structure

```
O1 (envelope minimality)
  └── self-contained within M(S1,S2,S3)
  └── requires: reverse FOC analysis on f(log c)

O3a (outside M)
  └── requires: new proof strategy (entropy / localization)
  └── independent of O1

Direction 3 (projection theory)
  └── subsumes O1 (as a special case of stable projections)
  └── gives context for O3a (what it means to leave M)
  └── longest horizon; highest abstraction
```

---

## Priority assessment

| Direction | Horizon | Blocking O? | Standalone paper? |
|---|---|---|---|
| O1 | Medium | Yes (closes XX) | Yes |
| O3a | Long | No | Possibly, with H3 |
| Projection theory | Long | No | Programme paper XXI? |

*O1 is the natural next target: contained, closes an open claim in XX,
and its resolution (either way) has immediate implications for the programme.*
