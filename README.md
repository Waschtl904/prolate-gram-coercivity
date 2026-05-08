# Prolate–Weil Program: Sampling, Frame Stability, and Spectral Structure

This repository contains a sequence of research papers on discrete sampling,
frame stability, and spectral structure in Paley–Wiener spaces using prolate
spheroidal wave functions (PSWFs), with connections to operator-theoretic
approaches to Weil positivity.

**Current state: Papers I–VIII complete. Hypotheses H1 and H2 of Paper VII are now unconditional.
The sole remaining gap in the original programme is B-strong.
Airy Edge Programme (Papers XIII–XVI): unconditional lower bound (Q5-lower) proved;
bridge to trace-norm control in progress.**

---

## Core Idea

The central concept developed in this series is the
**Discrete Spectral Transfer Property (DSTP)**:

> Discrete sampling preserves the spectral decay structure of PSWF
> interactions, leading to Schur-summable defect matrices and stable
> frame operators.

The main result of Paper I is a **reduction principle**: frame stability holds —
with explicit bounds — provided the DSTP is satisfied. Papers II–VIII develop the
operator-theoretic, arithmetic, semiclassical, and dyadic consequences of this
principle. **Paper VIII** establishes the three-scale architecture (combinatorial,
Airy/WKB, Landau–Widom) and completes the reduction to B-strong as the unique
remaining gap.

---

## Papers in This Repository

| File | Title | Status |
|---|---|---|
| `paper1.tex` | Frame coercivity and defect decomposition; introduction of DSTP | Complete |
| `paper2.tex` | Scaling limits, trace formula, conditional coercivity; Weil connection | Complete |
| `paper2_quadrature.tex` | XRY quadrature compatibility; conditional DSTP verification framework | Complete |
| `paper3.tex` | PSWF product spectral tail estimates; edge obstruction (bandwidth doubling) | Complete |
| `paper4_semiclassical.tex` | Semiclassical equidistribution of PSWF densities via Prüfer analysis | Complete |
| `paper5.tex` | WKB cover, Bridge Lemma, Schur control; ass:bulkconv proved for γ < 1/2 | Complete |
| `paper6.tex` | Galerkin norm estimates; No-Go theorem; B-strong framework | Complete |
| `paper7_skeleton.tex` | Dyadic cancellation for PSWF Galerkin operators; H1 unconditional | Complete |
| `paper8_scale_separated.tex` | Scale-separated dyadic cancellation; H2 unconditional; three-scale architecture | **Submission-ready** |
| `paper13_gap_s.tex` | Gap-S obstruction; reduction of frame stability to (Q5) | Complete |
| `paper14_airy_resolvent.tex` | Airy resolvent asymptotics; Framework paper: open problems map | Framework |
| `paper15_quasimode.tex` | Quasimode construction; unconditional (Q5-lower): $N_\varphi \geq 2$ | **Proved ✅** |
| `paper16_bridge.tex` | Bridge Reduction Lemma; quasimode stability ⇒ quadratic form convergence | **BR1-finite ✅** |

Companion notes (proved results, ready to insert into papers):

| File | Content | Status |
|---|---|---|
| `phase_nondeg_lemma.tex` | Phase Non-Degeneracy: α^(c) = π/2 + O(c^{−1/3}); H1 unconditional | **Proved** ✅ |
| `airy_discrete_stability_lemma.tex` | Proposition U(U') + ass:gap unconditional | **Proved** ✅ |
| `bridge_lemma.tex` | Bridge Lemma fully written out (to insert in paper5.tex) | **Proved** ✅ |
| `ax5_independence_remark.tex` | DSTP logically independent of AX1–AX4 (Riemann-rule witness) | **Proved** ✅ |
| `section5_numerical_evidence.tex` | Numerical evidence for spectral tail separation (for paper2_quadrature.tex) | Supplementary |

Internal documentation:

| File | Description |
|---|---|
| `numerics/` | Computational experiments and scripts |
| `DEPENDENCIES.md` | Full logical dependency graph between all papers and companion notes |
| `context_summary.md` | Internal working summary (session context scaffold) |
| `PROMPT.md` | Internal prompt scaffolding for AI-assisted sessions |
| `PHASE_NONDEG_NOTE.md` | **Superseded** — Phase Non-Degeneracy gap now closed; see `phase_nondeg_lemma.tex` |
| `assumption_2_4_target.md` | **Archived** — proof strategies for ass:bulkconv, superseded by Paper V |

---

## Airy Edge Programme (Papers XIII–XVI)

This sub-programme addresses **condition (Q5)**:
how many eigenvalues of $\mathcal{K}_c$ lie in a $c^{-1/3}$-window
near the transition point $z_{n^*}$?
The answer drives Gap-S (Paper XIII, Theorem B) and hence the full
frame stability theory.

### Three-Layer Architecture

| Layer | Paper | Content | Status |
|---|---|---|---|
| **I. Local / Existential** | XV | Airy quasimodes → $N_\varphi \geq 2$ unconditionally | ✅ **Proved** |
| **II. Form Stability** | XVI | Quasimode stability ⇒ quadratic form convergence (BR1-finite) | ✅ **Proved** |
| **II. Form Stability** | XVI | $L^2$ kernel rate ⇒ strong resolvent conv.\ (BR1-global) | ⚠️ Conditional |
| **III. Global / Trace** | XIV | Weighted kernel conv.\ ⇒ trace-norm conv.\ (BR3) | 🔴 Open (hardest) |
| **III. Global / Trace** | XIV | $N_\varphi \leq 2$ (upper count) | 🔴 Open (needs BR3) |

### Logical Chain (Papers XIII–XVI → Gap-S)

```
Paper XV (unconditional)
  Spectral ID Principle + Airy quasimodes
      ↓ [Paper XVI, Thm 2.1, unconditional]
  BR1-finite: form convergence on Airy subspaces
      ↓ [Paper XVI, Thm 3.2, + L² kernel rate assumption]
  BR1-global: strong resolvent convergence
      ↓ [Paper XIV, + BR3: weighted kernel convergence]
  Trace-norm resolvent convergence
      ↓ [Paper XIV, Helffer–Sjöstrand]
  (Q5): N_φ(c) = 2 + O(c^{-1/3})
      ↓ [Paper XIII, Theorem B]
  Gap-S
```

### What Is Unconditional After Papers XV–XVI

- **Spectral Identification Principle** (XVI, Prop. 1.1):
  the PSWE→$\mathcal{K}_c$ transfer is rigorous via shared eigenbasis. ✅
- **Spectral concentration** (XVI, Cor. 1.3):
  Airy quasimodes concentrate on $\psi_{n^*+k}^{(c)}$ with error $O(c^{-1/3})$. ✅
- **Form convergence on finite subspaces** (XVI, Thm. 2.1):
  $\mathfrak{q}[B_c](u,v) \to \mathfrak{q}[\mathcal{A}](u,v)$ on Airy-generated subspaces,
  rate $O(c^{-1/6})$. ✅
- **(Q5-lower)** (XV, Thm. 1.1):
  $N_\varphi(c) \geq 2$ for all large $c$. ✅

### Open Problems (Airy Edge Programme)

| Problem | Location | Difficulty |
|---|---|---|
| $L^2$ kernel rate (Ass. 3.1, XVI) | XVI §3 | Medium — Olver-type PSWE asymptotics |
| Bulk–edge microlocal separation | XIV, Prob. 4 | Hard |
| BR3: weighted kernel convergence | XIV, Prob. 4.1; XVI, Prob. 4.1 | **Hardest** |
| Index matching: sub-leading Weyl | XIV, Prob. 4.4 | Medium–hard (new) |
| (Q5-upper): $N_\varphi \leq 2$ | XIV | Needs BR3 |

---

## What is Now Unconditional (Full Programme)

The following results hold **without any remaining assumptions**:

- **ass:bulkconv** (Assumption 2.4, Paper III): proved for γ < 1/2 via Bridge Lemma (Paper V) ✅
- **Phase Non-Degeneracy**: α^(c) = π/2 + O(c^{−1/3}), dist(α^(c), {0,π}) ≥ π/4 for all large c ✅
- **Proposition U and U'** (Paper VIII): Airy discrete stability bounds unconditional ✅
- **ass:gap** (Paper VIII): uniform spectral gap unconditional ✅
- **H1, H2** (Paper VII/VIII): unconditional ✅
- **Lemma F, Corollary C** (Paper VIII): unconditional ✅
- **(Q5-lower)**: $N_\varphi(c) \geq 2$ for all large $c$ (Paper XV) ✅
- **BR1-finite**: form convergence on Airy subspaces (Paper XVI) ✅

---

## Paper VIII: Three-Scale Architecture

**Paper VIII** (`paper8_scale_separated.tex`) establishes the three-scale structure
of the dyadic cancellation mechanism:

| Scale | Layer | Content | Status |
|---|---|---|---|
| Combinatorial `c^{−1/3}` | Dyadic Separation | Lemma F (DSP), Corollary C | ✅ Unconditional |
| Local Airy `(c/2)^{−1/3}` | Airy / WKB | Proposition U(U'), Lemma A | ✅ Unconditional |
| Global Landau–Widom `(log c)^{2/3}` | erfc profile | Conjecture ULW | 📊 Empirical only |

---

## Open Problems (May 2026)

### Gap in Original Programme

| Problem | Location | Status |
|---|---|---|
| **B-strong**: `P_{kl} ≤ C₂ c^{1/2}` in transition zone | Paper VI/VII H3 | 🔴 Open |

### Airy Edge Programme

See table in § Airy Edge Programme above.

### Secondary

| Problem | Evidence / Status |
|---|---|
| **Conjecture ULW**: erfc global scaling law | Numerical residuals ≈ 2·10^{−2} |
| Limit of β(c) as c → ∞ | Fitting suggests β(∞) ∈ [−0.30, −0.21] |
| Bridge Lemma extension to γ ≥ 1/2 | Geometry breaks; stationary phase open |
| Weil operator identification G_∞ (Paper II) | Structural; medium term |

---

## Logical Dependency Chain

```
phase_nondeg_lemma.tex
    ↓ proves H1 (Paper VII) unconditionally
airy_discrete_stability_lemma.tex
    ↓ proves ass:gap + Prop. U(U') unconditionally
    ↓ proves H2 (Paper VII/VIII) unconditionally

B-strong (open)
    ↓ will prove H3 (Paper VII)

H1 ✅ + H2 ✅ + H3 (⚠️ B-strong)
    ↓
Paper VII Theorem 2.1 (abstract dyadic cancellation)
    ↓
Contraction estimate: ‖DT_c^{(N)}‖ < 1 for large c
    ↓
Assumption A → complete frame stability theory

───────────────────────────────────────────────

Paper XV (unconditional)
    ↓ Airy quasimodes + Spectral ID Principle
Paper XVI, Thm 2.1 (unconditional)
    ↓ BR1-finite: form convergence on Airy subspaces
Paper XVI, Thm 3.2 (+ L² kernel rate, open)
    ↓ BR1-global: strong resolvent convergence
Paper XIV (+ BR3: weighted kernel conv., open)
    ↓ Trace-norm resolvent convergence
    ↓ (Q5): N_φ(c) = 2 + O(c^{-1/3})
Paper XIII, Theorem B
    ↓
  Gap-S
```

---

## Key References

- Osipov–Rokhlin–Xiao (2013): *Prolate Spheroidal Wave Functions of Order Zero*, Springer
- Slepian (1978): *Prolate spheroidal wave functions, Fourier analysis, and uncertainty V*, Bell Syst. Tech. J.
- Xiao–Rokhlin–Yarvin (2001): *Prolate spheroidal wave functions, quadrature, and interpolation*, Inverse Problems
- Kato (1966): *Perturbation Theory for Linear Operators*, Springer
- Simon (2005): *Trace Ideals and Their Applications*, 2nd ed., AMS
- Olver (1997): *Asymptotics and Special Functions*, AK Peters
- Tracy–Widom (1994): Level-spacing distributions and the Airy kernel, Comm. Math. Phys. **159**
- Connes–Consani–Moscovici (2022, 2025): UV prolate spectrum and zeros of zeta, PNAS; arXiv:2511.22755
- Levitan–Sargsjan (1991): *Sturm–Liouville and Dirac Operators*, Kluwer
- Weil (1952): *Sur les formules explicites de la théorie des nombres*
- Reed–Simon (1980): *Methods of Modern Mathematical Physics I*, Academic Press
- NIST DLMF (2023): Digital Library of Mathematical Functions, https://dlmf.nist.gov/
