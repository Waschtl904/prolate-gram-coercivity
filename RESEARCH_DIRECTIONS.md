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
This is the transition from "H1 is sufficient" to "H1 is minimal within $\mathcal{M}(\mathrm{S1,S2,S3})$".
That shift has substantially more theoretical weight than further model examples.
It would close the axiom-economy question for the programme.

**The diagonal compression observation** *(added 2026-05-08)*

The decisive mechanism is not the global behavior of $f(j) = o(1)$,
but its behavior along the *forced diagonal*
$$j \sim K^*(c) \sim \frac{2\beta}{\alpha} \log c.$$
The FOC compresses the available degrees of freedom:
after substitution $j \mapsto K^*(c)$, any asymptotic improvement in $f$
must survive as $f(K^*(c)) = f\!\left(\frac{2\beta}{\alpha}\log c + O(\log\log c)\right)$.
Since $K^*(c) \to \infty$ only logarithmically,
a globally decaying $f$ may still satisfy $f(K^*(c)) \not\to 0$
at the rate required to improve the leading term.

**Consequence:** O1 is directly coupled to S3.
The same substitution structure that *generates* the rate
(S3: diagonal substitution $K \mapsto K^*(c)$)
also *prevents* its improvement via H1 perturbations.
Global monotonicity of $f$ is insufficient;
what matters is whether the improvement remains asymptotically visible
after projection onto the logarithmic diagonal.

**Likely approach:**
Reverse FOC analysis: assume $f(K^*(c)) \to 0$ and derive a contradiction
with the balance equation, or show $K^*(c)$ shifts in a way that absorbs the gain.

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

**The mode shift** *(added 2026-05-08)*

The current paper is Tauberian in structure:
*given* axioms S1/S2/S3, the scale is forced.
A genuine lower bound outside $\mathcal{M}$ requires a different mathematical mode:
not "every method with these properties produces this rate",
but rather "every approximation must carry this information somewhere".

This suggests the following candidate approaches:
- **Eigenfunction localization:** concentration of $e_j$ near the turning point
  forces a minimum information cost that any approximation must pay.
- **Spectral concentration / Kolmogorov widths:** lower bounds on
  $n$-widths of the eigenfunction class in $L^2([0,M])$ for large $j$.
- **Semiclassical barrier arguments:** the WKB barrier at the turning point
  as an intrinsic obstruction, independent of summation method.
- **Entropy arguments:** the spectral information content at scale $c$
  cannot be compressed below a threshold set by the turning-point geometry.

Each of these is a structurally different mode from the current architecture.

---

## Direction 3 — Asymptotic Projection Theory

**Current status:** $\mathfrak{R}$ is defined functionally in Paper XX
(Definition `def:realization_map`). Its abstract properties are not yet developed.

**The question:**
When does an asymptotic procedure induce a well-defined projection
$\mathfrak{R}: \mathcal{B} \to \mathcal{S}/{\sim_{\mathcal{S}}}$?

**The projection axiomatics** *(added 2026-05-08)*

Once $\mathfrak{R}$ is understood not as a WKB-specific construction
but as a general map from analytic bounds to asymptotic classes,
the following questions become well-posed:

1. **Well-definedness:** when does $b(K,c)$ have a unique image in
   $\mathcal{S}/{\sim_{\mathcal{S}}}$? (Answer for WKB: iff prefactor is $c$-admissible.)
2. **Stability axioms:** which properties of a summation/regularization method
   guarantee that the image is $c$-uniformly stable?
   Candidate axioms: leading-power extraction, uniform remainder control,
   scaling invariance of coefficients. Is this list complete?
3. **Projection fidelity:** when does $\mathfrak{R}(b_1 + b_2) = \mathfrak{R}(b_1)$
   (i.e. when does the dominant term dominate after projection)?
4. **Collapse conditions:** which deformations of the summation method
   destroy $c$-uniform stability while preserving the target order $\succ$?
   (This is exactly `lem:S2_knockdown` in abstract form.)
5. **Equivalence classes of methods:** when do two different methods
   induce the same projection $\mathfrak{R}$?
   This gives an equivalence relation on summation methods,
   coarser than functional equality.

**Why this is not decoration:**
The four-layer architecture (analytic / projective / asymptotic / ordinal)
is currently instantiated once, for WKB power-sum bounds.
A projection theory would:
- make the framework reusable for other operator classes
  where similar two-scale problems arise
- give intrinsic meaning to S2 beyond its WKB instantiation
- connect to existing theory (regular variation, Tauberian theorems,
  asymptotic algebras) from a new angle

This direction begins to leave Spectral Theory proper
and move toward a general *asymptotic structure theory*.

---

## Dependency structure

```
O1 (envelope minimality)
  └── self-contained within M(S1,S2,S3)
  └── directly coupled to S3 (diagonal compression)
  └── requires: reverse FOC analysis on f(log c)

O3a (outside M)
  └── requires: new proof mode (localization / entropy / semiclassical)
  └── independent of O1

Direction 3 (projection theory)
  └── subsumes O1 as special case of stable projections
  └── gives abstract context for O3a (exiting M = losing projection stability)
  └── connects to regular variation, Tauberian theory, asymptotic algebras
  └── longest horizon; highest abstraction
```

---

## Priority assessment

| Direction | Horizon | Closes open claim? | Standalone paper? |
|---|---|---|---|
| O1 | Medium | Yes (necessity in XX) | Yes |
| O3a | Long | No (O3a open by design) | Possibly, with H3 |
| Direction 3 | Long | No | Programme paper XXI? |

*O1 is the natural next target: contained, closes an open claim in XX,
coupled to S3 via diagonal compression,
and its resolution (either way) has immediate implications for the programme.*
