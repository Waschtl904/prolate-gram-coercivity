# Program Map: Linear Stack → Modular System

> This document is the translation layer between the old sequential paper numbering
> (Papers I–XXII) and the new modular architecture (DAG nodes, black boxes, problem clusters).
>
> **Key principle:** In the new system, "Paper" has three distinct meanings:
> - **Archive** — complete theory, for external readers (`*_outline.tex`)
> - **Proof machine** — dependency logic (`*_dag.tex`)
> - **Research interface** — isolated open problems (`*_problem.tex`)

---

## The Three Axes of the New System

```
Axis 1: Discrete Geometry     (Sampling / Kadec / Primes)   → O4
Axis 2: Spectral Universality (Airy / Tracy–Widom / IIKS)   → O5
Axis 3: RHP Enhancement       (Muskhelishvili / Deift–Zhou)  → O1/O2  [optional]
```

The Main Theorem of XXII = Axis 1 ∩ Axis 2.
Axis 3 improves the exponent (c^{-1/2} → c^{-1/3}) but is not on the minimal path.

---

## Full Mapping Table: Papers I–XXII

| Paper | Old role | New role | DAG nodes / files | Open problems |
|---|---|---|---|---|
| **I** | Gram coercivity, DSTP | **Black Box (BB3)** | BB3 in `paper22_dag.tex` Layer 0 | DSTP for primes still open |
| **II** | Scaling limits, trace formula, Weil | **Background infrastructure** | Not in XXII DAG directly | Weil-operator still open |
| **II_quad** | XRY quadrature, conditional framework | **Conditional sub-module** | Not in XXII DAG | XRY stability open |
| **III** | Bulk tail, off-diagonal, edge obstruction | **Existential seed (BB2)** | BB2 in `paper22_dag.tex` Layer 0 | Uniform BW-Doubling → O4 Route A |
| **IV** | Semiclassical equidistribution | **Tool for O4 Route B** | Used in Langer–Olver entry for Gram matrix entries | No new open problem |
| **V** | WKB Cover, Bridge Lemma, Schur control | **Closed module** ✅ | Feeds BB1 (bulk match) indirectly | ass:bulkconv closed for γ < 1/2 |
| **VI** | Galerkin norm, No-Go theorem, Layers 0–2 | **Obstruction certificate** | Motivates Layer 2 / A-B splitting in XXII | B-strong still open |
| **VII** | Dyadic cancellation, reduction | **Contraction engine** | Feeds early contraction strand; not in XXII DAG | H3 / B-strong open |
| **VIII** | Scale-separated cancellation | **Three-scale closed module** ✅ | ass:gap, Prop.U/U' closed | Global LW scale open |
| **IX–XVII** | Refined coercivity, resolvent, quasimode, bridge, cliff | **Technical backbone** | Input to BB5 (Widom edge phase), BB6 (Deift–Zhou) in XXII | Internal; no new O-nodes |
| **XVIII** | Qualitative Airy universality | **Black Box (BB5+BB6 seed)** | BB5, BB6 in `paper22_dag.tex` Layer 0; A5 in `trilogy_dag.tex` | O4 Route B uses Langer–Olver from here |
| **XIX** | Quantitative Airy rate | **Rate calibration** | A6–A8 in `trilogy_dag.tex`; not directly in XXII | |
| **XX** | Universality and structural rigidity | **Universal envelope** | U1–U7 in `trilogy_dag.tex`; structural boundary for XXII | ρ-classification open |
| **XXI** | Commutativity failure, bulk–edge split | **Black Box (BB1+BB2)** | BB1, BB2 in `paper22_dag.tex` Layer 0 | |
| **XXII** | Edge coercivity, Main Theorem | **Program interface** | `paper22_outline.tex` + `paper22_dag.tex` + `paper22_core_skeleton.md` | O1–O6 (see below) |
| **13b** | Gram → spectral gap | **Black Box (BB3 = R1)** | R1 in `paper22_dag.tex` Layer 3 | |
| **13cc** | IIKS structure, RHP reduction | **Coordinate system (P2)** | P2 in `paper22_dag.tex` Layer 1 | O1/O2 (enhancement) |

---

## Dissolution of "Paper XXII" into Three Roles

```
What was once "Paper 4" (= XXII) is now:

  paper22_outline.tex       →  Archive
                                Complete theory, all sections, bibliography.
                                For external readers and submission.

  paper22_dag.tex           →  Proof machine
                                Every theorem as node, every dependency explicit.
                                Import/black-box cleanly separated.
                                For internal consistency checking.

  paper22_core_skeleton.md  →  Research interface
                                Reduced to: F_Gram × F_Airy = Main Theorem.
                                Two open nodes only.
                                For daily working.
```

---

## Open Problems: Old Assumptions → New O-Nodes

| Old ID | Old description | New ID | New file | Method axis |
|---|---|---|---|---|
| H3 / B-strong | P_{kl} ≤ C₂ c^{1/2} | — | Early contraction strand (Paper VII); not in XXII DAG | Axis 1 (discrete) |
| ass:gap (closed ✅) | Uniform gap κ₀ c^{-1/3} | Closed by `airy_discrete_stability_lemma.tex` | — | — |
| Ass. A (Paper VII contraction) | Nonlinear self-consistency | **O1** | `paper22_dag.tex` §5, `O5_airy_gap_problem.tex` §3 Route C | Axis 3 (RHP) |
| Off-diagonal decay (Paper III) | Assumption 3.1 | **O4 sub-problem** | `O4_frame_stability_problem.tex` §4 Route B | Axis 1 (discrete) |
| BW-Doubling uniform | Uniform over edge block | **O4 Route A** | `O4_frame_stability_problem.tex` §4 Route A | Axis 1 (discrete) |
| DSTP for primes | DSTP with prime sampling | **O4 core** | `O4_frame_stability_problem.tex` §2 | Axis 1 (discrete) |
| RHP convergence Y_c → Y_Ai | Conj. 3.3 in XXII | **O1 + O2** | `paper22_dag.tex` P5, P7, P8 | Axis 3 (RHP) |
| inf σ(D^Airy) > 0 | new in XXII | **O5** | `O5_airy_gap_problem.tex` | Axis 2 (spectral) |
| Weil operator G_∞ | Paper II | — | Not in XXII program | — |
| XRY stability | Paper II_quad | — | Not in XXII program | — |
| ρ-classification | Paper XX | — | `RESEARCH_DIRECTIONS.md` | — |

---

## The Three Strands That Survive into XXII

### Strand 1: Discrete geometry (Axis 1)
```
Paper I (Gram coercivity)
  → Paper III (edge obstruction / BW-Doubling)
    → O4_frame_stability_problem.tex
      → O4: uniform quasi-isometry of Ev|_Edge
        → P9 in paper22_dag.tex
          → R1 (BB3 = Paper 13b)
            → gap ≥ c^{-1/2}
```

### Strand 2: Spectral universality (Axis 2)
```
Papers XVIII–XX (Airy universality, quantitative rate)
  → Paper 13cc (IIKS structure)
    → P2 in paper22_dag.tex (IIKS = coordinate system)
      → O5_airy_gap_problem.tex
        → O5: inf σ(D^Airy) > 0
          → P12 in paper22_dag.tex
            → P13: Main Theorem
```

### Strand 3: RHP enhancement (Axis 3, optional)
```
Paper 13cc (RHP reduction)
  → P5: Assumption A (O1)
    → P7: Assumption B (O2)
      → P8: Y_c → Y_Airy
        → P10: c^{-1/3} gap scale (upgrade only)
```

---

## What Is Fully Closed (No Further Work Needed)

| Item | Closed by | Status |
|---|---|---|
| ass:gap | `airy_discrete_stability_lemma.tex` | ✅ |
| Prop. U / U' | `airy_discrete_stability_lemma.tex` | ✅ |
| H1 (Paper VII) | `phase_nondeg_lemma.tex` | ✅ |
| H2 (Paper VII) | `airy_discrete_stability_lemma.tex` | ✅ |
| ass:bulkconv (γ < 1/2) | Paper V / `bridge_lemma.tex` | ✅ |
| DSTP ⊥ AX1–AX4 | `ax5_independence_remark.tex` | ✅ |
| Conj. 6.1 (phase) | `phase_nondeg_lemma.tex` | ✅ |
| Gram → gap (for use in XXII) | Paper 13b as BB3 | ✅ (imported) |
| IIKS representation of sinc kernel | Paper 13cc as P2 | ✅ (exact identity) |
| Universal rate O(c^{-β}(log c)^{1+γ}) | Paper XX | ✅ |

---

## What Remains Open (Prioritized)

| Priority | ID | Description | File | Method |
|---|---|---|---|---|
| 🔴 Critical (minimal path) | **O4** | Uniform frame stability of Ev\|_Edge | `O4_frame_stability_problem.tex` | Kadec / Jaffard / BW-Doubling |
| 🔴 Critical (minimal path) | **O5** | inf σ(D^Airy) > 0 | `O5_airy_gap_problem.tex` | Airy oscillation / Tracy–Widom |
| 🟡 Important (exponent) | **O1** | Assumption A: nonlinear RHP fixed point | `paper22_dag.tex` §5 | Muskhelishvili |
| 🟡 Important (exponent) | **O2** | Assumption B: geometry given A | `paper22_dag.tex` §5 | Deift–Zhou |
| 🟠 Early strand | **H3 / B-strong** | P_{kl} ≤ C₂ c^{1/2} | Paper VII | WKB / Airy |
| 🟠 Structural | **ρ-classification** | Deformation classes via Karamata | `RESEARCH_DIRECTIONS.md` | Karamata / reg. variation |
| ⚪ Long-range | **O6** | RH collapse of coercivity gap | `paper22_dag.tex` §5 | Zeta zeros |

---

*Generated May 2026. Reflects state after Papers I–XXII and all companion notes.*
*This file is the master translation layer. Update whenever a new paper or open node is added.*
