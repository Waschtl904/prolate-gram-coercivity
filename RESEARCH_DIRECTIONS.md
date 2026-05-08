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

The decisive mechanism is not the global behavior of $f(j) = o(1)$,
but its behavior along the *forced diagonal*
$$j \sim K^*(c) \sim \frac{2\beta}{\alpha} \log c.$$
After substitution $j \mapsto K^*(c)$, any asymptotic improvement survives only as
$f(K^*(c)) = f\!\left(\frac{2\beta}{\alpha}\log c + O(\log\log c)\right).$
Since $K^*(c) \to \infty$ only logarithmically,
a globally decaying $f$ may still satisfy $f(K^*(c)) \not\to 0$
at the rate required to improve the leading term.

**The S3 compression principle** *(2026-05-08)*

S3 is not merely a transfer mechanism for asymptotic information.
It is simultaneously a *compression mechanism* for possible improvements:

- **Algebraic improvements** in $j$ (e.g. $f(j) = j^{-\epsilon}$)
  survive the diagonal projection, since
  $f(K^*(c)) = (\log c)^{-\epsilon} \to 0$.
  These *would* improve the rate and are excluded by O1 (open).
- **Slowly varying improvements** (e.g. $f(j) = (\log j)^{-\delta}$)
  become $f(K^*(c)) = (\log\log c)^{-\delta} \to 0$ very slowly,
  and generate a rate $O(c^{-\beta}(\log c)^{1+\gamma}(\log\log c)^{-\delta})$:
  a genuine improvement, but only by a secondary logarithm.
  Whether this is excludable within $\mathcal{M}(\mathrm{S1,S2,S3})$
  is precisely the content of O1.
- **Sub-slowly-varying improvements** (e.g. $f(j) = (\log\log j)^{-\delta}$)
  become frozen: $f(K^*(c)) \sim (\log\log\log c)^{-\delta}$,
  asymptotically invisible after projection.

**Reformulation of O1:**
O1 is not an envelope-minimality question in the classical sense.
The deeper question is:
> *Which information survives the S3 diagonal projection?*

This makes O1 a problem about information loss under diagonal compression,
not about the global shape of the eigenfunction envelope.

**Likely approach:**
Reverse FOC analysis: show that any $f$ with $f(K^*(c)) \to 0$
either forces a shift in $K^*(c)$ that absorbs the gain,
or requires the prefactor to become $c$-inadmissible (violating S2).

---

## Direction 2 — Outside $\mathcal{M}(\mathrm{S1,S2,S3})$: O3a

**Current status:** Open. No lower bound claimed for $\mathcal{M}^c$.

**The question:**
Is the logarithmic loss $(\log c)^{1+\gamma}$ a consequence
of the method class — or a deeper spectral-geometric phenomenon?

**Two sub-questions:**

**(O3a)** Does there exist a method outside $\mathcal{M}(\mathrm{S1,S2,S3})$
that achieves $o(c^{-\beta}(\log c)^{1+\gamma})$?

**(O3b)** Can a uniform lower bound be established
(currently blocked by absence of H3)?

**The mode shift** *(2026-05-08)*

The current paper is Tauberian: *given* axioms, the scale is forced.
A genuine lower bound outside $\mathcal{M}$ requires a different mode:
not "every method with these properties produces this rate",
but "every approximation must carry this information somewhere".

Candidate approaches:
- **Eigenfunction localization** near the turning point as intrinsic information cost
- **Kolmogorov widths** of the eigenfunction class in $L^2([0,M])$
- **Semiclassical barrier arguments** at the turning point
- **Entropy / information-theoretic** lower bounds on spectral approximation at scale $c$

Each requires a structurally different proof mode from the current architecture.

---

## Direction 3 — Asymptotic Projection Theory

**Current status:** $\mathfrak{R}$ defined functionally in Paper XX.
Abstract theory not yet developed.

**The abstract core** *(2026-05-08)*

The structure underlying $\mathfrak{R}$ is more general than its WKB instantiation:
- a *source space* of analytic representatives (bounds, expansions)
- a *target order* of asymptotic equivalence classes
- a *stability condition* ensuring that projection and rescaling commute

The content of S2 is then precisely:

> **Scale-stability criterion:**
> $A(K,c)$ *induces a well-defined class under* $\mathfrak{R}$
> $\iff$ $A$ *is asymptotically scale-stable*,

where *asymptotically scale-stable* means:
$$\sup_{c \geq c_0}\, \frac{A(K, \lambda c)}{A(K, c)} < \infty
\quad \forall \lambda > 0, \text{ uniformly in } K \text{ on the diagonal}.$$

This is entirely independent of Euler–Maclaurin.
EM is one concrete mechanism that *realizes* scale-stability in the WKB power-sum class.
The criterion itself is a general asymptotic stability axiom.

**Transformation of S2:**
The scale-stability criterion would transform S2 from a
WKB-technical property (EM structural property)
into a general asymptotic stability axiom:

| Stage | Formulation of S2 |
|---|---|
| Paper XX | EM structural property: $C_\sigma$ explicit and $c$-independent |
| Abstract criterion | $A(K,c)$ is asymptotically scale-stable |
| Functional form | $\mathfrak{R}$ commutes with $c$-rescaling |

All three are equivalent in the WKB setting;
only the last two generalize.

**The five structural questions:**
1. **Well-definedness:** when does $b(K,c)$ have a unique image in $\mathcal{S}/{\sim}$?
2. **Stability axioms:** is {leading-power extraction, uniform remainder, scaling invariance} complete?
3. **Projection fidelity:** when does $\mathfrak{R}(b_1 + b_2) = \mathfrak{R}(b_1)$?
4. **Collapse conditions:** which deformations destroy $c$-uniform stability
   while preserving the target order $\succ$?
   *(This is `lem:S2_knockdown` in abstract form.)*
5. **Method equivalence:** when do two summation methods induce the same $\mathfrak{R}$?

**Connection to existing theory:**
- Regular variation (Bingham–Goldie–Teugels): slowly varying functions
  as the boundary case of scale-stability
- Tauberian theorems: sufficient conditions for $\mathfrak{R}$ to be well-defined
- Asymptotic algebras: algebraic structure of $\mathcal{S}/{\sim}$ as a ring

---

## Dependency structure

```
O1 (envelope minimality = information survival under S3 compression)
  └── coupled to S3 via diagonal compression principle
  └── coupled to S2 via c-admissibility of shifted prefactors
  └── requires: reverse FOC analysis on f(K*(c))

O3a (outside M)
  └── requires: new proof mode (localization / entropy / semiclassical)
  └── independent of O1

Direction 3 (asymptotic projection theory)
  └── scale-stability criterion generalizes S2
  └── subsumes O1 as instance of projection fidelity
  └── subsumes O3a context: leaving M = losing scale-stability
  └── connects to regular variation, Tauberian theory, asymptotic algebras
```

---

## Priority assessment

| Direction | Horizon | Closes open claim? | Standalone paper? |
|---|---|---|---|
| O1 | Medium | Yes (necessity in XX) | Yes |
| O3a | Long | No | Possibly, with H3 |
| Direction 3 | Long | No | Programme paper XXI? |

*O1 is the natural next target. Its resolution requires understanding
which information survives the S3 diagonal projection —
a question that is simultaneously the key to Direction 3.*
