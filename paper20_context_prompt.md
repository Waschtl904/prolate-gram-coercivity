# Paper XX — Original Scaffold (ARCHIVIERT)

> **STATUS: ARCHIVIERT — Mai 2026**
> Dieses Dokument war der Planungs-Scaffold für Paper XX vor dessen Fertigstellung.
> Paper XX (`paper20_universality.tex`) ist inzwischen **arXiv-ready**.
>
> Für den aktuellen Zustand:
> - Volltext: `paper20_universality.tex`
> - Offene Probleme und Programm: `RESEARCH_DIRECTIONS.md`
> - Abhängigkeiten und Theoreme: `DEPENDENCIES.md`
> - Session-Kontext: `PROMPT.md`
>
> Der Scaffold-Inhalt unten hat historischen Wert (er dokumentiert die Entstehung
> der S1/S2/S3-Sprache, der Realisierungsabbildung $\mathfrak{R}$ und der
> $\rho$-Klassifikation), ist aber **nicht mehr operativ**.
> Insbesondere: §6 (Open Questions) und §8 (First Action) sind überholt.

---

<!-- ORIGINAL SCAFFOLD BELOW — DO NOT USE FOR ACTIVE WORK -->

# Paper XX — Full Scaffold
## Universality of Turning-Point Truncation Geometry

**Programme:** prolate-gram-coercivity  
**Predecessor freeze commits:** XVIII `d7609d2`/`19f5742`, XIX `580016b`  
**Status (original):** scaffold — no results frozen yet  
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

### 2.1 $\gamma$-Agnostic Nodes

| Node | Content | Why $\gamma$-agnostic |
|---|---|---|
| Tensor decomposition $A_K - B_K$ | XIX `def:decomp` | Pure algebra |
| Tensor norm estimate (per $j$) | XIX `lem:langer_rate` proof | Only $\|\cdot\|_{L^2}$ |
| Bessel tail | XVIII `lem:besseltail` | Bessel inequality; no $V$ |
| Tonelli/DCT argument | XVIII `rem:dct` | $L^1$ domination; no $V$ |
| Slepian-type tail | XVIII `lem:slepianunif` | ORX/Slepian; independent of $\gamma$ |
| HS/Cauchy–Schwarz on $B_K$ | XIX `lem:tail_rate` | Spectral orthogonality only |
| Sequential $(c,K)$-limit | XVIII `rem:iterated` | Two-scale structure; no $V$ |
| Norm-resolvent perturbation | XVIII `prop:normresolvent` | Kato VI; form-boundedness |

### 2.2 $\gamma$-Sensitive Nodes

| Node | Airy ($\gamma=2/3$) | General |
|---|---|---|
| Spectral spacing | $a_K \sim (3\pi K/2)^{2/3}$ | $a_K \sim C_\gamma K^\gamma$ |
| Coercive threshold | $\mu(K) \sim K^{2/3}$ | $\mu(K) \sim K^\gamma$ |
| Exclusion window | $\delta_0(K) \sim K^{2/3}$ | $\delta_0(K) \sim K^\gamma$ |
| Lax–Milgram constant | $C'(M,K) = O(MK^{2/3})$ | $C'(M,K) = O(MK^\gamma)$ |

---

## §3–§7. (Scaffold-Inhalt)

*(Vollständiger Scaffold-Text bleibt aus historischen Gründen erhalten.
Die Theoreme `thm:universal_rate`, `thm:rate_obstruction`, `def:realization_map`,
die S1/S2/S3-Struktur und die $\rho$-Klassifikation wurden im Verlauf der
tatsächlichen Paper-Entwicklung über diesen Scaffold hinaus entwickelt.
Siehe `paper20_universality.tex` für den finalen Stand.)*

---

*Archiviert: Mai 2026. Predecessor freezes: XVIII `d7609d2`/`19f5742`, XIX `580016b`.*
