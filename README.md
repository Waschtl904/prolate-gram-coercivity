# Prolate Sampling and Frame Stability

This repository contains a sequence of research papers on
sampling, frame stability, and spectral structure in
Paley–Wiener spaces using prolate spheroidal wave functions (PSWFs).

---

## Core Idea

A central concept developed in this series is the
**Discrete Spectral Transfer Property (DSTP)**:

> Discrete sampling preserves the spectral decay structure
> of PSWF interactions, leading to Schur-summable defect matrices
> and stable frame operators.

The main result of Paper I is a reduction principle:
frame stability holds — with explicit bounds — provided the DSTP is satisfied.
Papers II and II(quadrature) develop the operator-theoretic and analytic
consequences of this principle.

---

## Current Contents

The repository currently contains the following working papers:

| File | Description |
|---|---|
| `paper1.tex` | Frame coercivity and defect decomposition; introduction of DSTP |
| `paper2.tex` | Scaling limits, trace formula, and conditional coercivity under DSTP |
| `paper2_quadrature.tex` | XRY quadrature compatibility and conditional DSTP verification |
| `paper3.tex` | PSWF product spectral tail estimates; edge obstruction (bandwidth doubling) |
| `paper4_semiclassical.tex` | Semiclassical / WKB analysis; weak convergence of PSWF densities |
| `section5_numerical_evidence.tex` | Numerical experiments supporting the analytic results |

Additional files:

| File | Description |
|---|---|
| `numerics/` | Computational experiments and scripts |
| `DEPENDENCIES.md` | Logical dependency graph between papers |
| `context_summary.md` | Internal working summary (AI-session context scaffold) |
| `assumption_2_4_target.md` | Analysis of proof strategies for the remaining open assumption |
| `PROMPT.md` | Internal prompt scaffolding |

---

## Relationship Between the Papers

- **Paper I** establishes the core reduction: frame stability of the prolate
  sampling operator is equivalent to a spectral defect condition (DSTP).
  Unconditional coercivity is proved; DSTP is verified for random and
  Gauss–PSWF sampling. Prime sampling is left open.

- **Paper II** develops operator-theoretic consequences: scaling limits
  of Gram operators, unconditional compactness, and a trace formula
  connecting weighted Gram matrices to the prime number theorem.
  Strong coercivity in the scaling limit is conditional on DSTP
  holding along prime sampling sequences.

- **Paper II (quadrature)** organises the problem of verifying DSTP
  for XRY PSWF-Gauss quadrature into two explicit conjectural inputs
  (a PSWF product spectral tail conjecture and an XRY stability conjecture).
  The edge regime is identified as a proved obstruction (bandwidth doubling).

- **Paper III** proves the edge obstruction unconditionally,
  establishes a uniform off-diagonal bound, and provides mean spectral
  localization results. The bulk exponential tail bound is conditional
  on Assumption 2.4 (bulk convolution decay).

- **Paper IV** provides the semiclassical input: weak convergence of
  PSWF densities and energy equidistribution in the bulk regime,
  closing the central open problem of Paper III in the bulk.

---

## Open Problems (as of April 2026)

| Problem | Source | Status |
|---|---|---|
| DSTP for prime sampling | Paper I | 🔴 open |
| Bulk convolution decay (Assumption 2.4) | Paper II / III | 🔴 open |
| Off-diagonal phase separation (Paper III, Ass. 3.1) | Paper III | ⚠️ conditional |
| C⁰ extension of PSWF density convergence | Paper IV | 🔴 open |
| Off-diagonal analogue of Paper IV main theorem | Paper IV | 🔴 open |

A full dependency and status graph is in [`DEPENDENCIES.md`](DEPENDENCIES.md).

---

## Series Vision (Work in Progress)

This project is part of a larger planned series investigating:

- semiclassical structure of PSWFs and WKB phase analysis
- oscillation-compatible quadrature rules
- arithmetic sampling regimes (prime sets, random sampling)
- potential extensions toward number-theoretic spectral questions

These components are under active development and
are **not yet fully represented in this repository**.

---

## Key References

- Osipov–Rokhlin–Xiao (2013): *Prolate Spheroidal Wave Functions of Order Zero*, Springer
- Slepian–Pollak (1961): Original PSWF concentration paper
- Xiao–Rokhlin–Yarvin (2001): PSWF-Gauss quadrature
- Connes–Consani–Moscovici (2025): arXiv:2511.22755
- Kato (1966): *Perturbation Theory for Linear Operators*
- Reed–Simon (1975): *Methods of Modern Mathematical Physics, Vol. I–II*
