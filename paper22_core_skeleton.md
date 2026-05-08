# Paper XXII — Core Skeleton
**Minimal operative structure. This is the working document; `paper22_dag.tex` is the archive.**

---

## 1. The Single Question

```
inf σ(D_Edge) > 0
```

where `D_Edge = Π_edge (A_{N,c} − K_c) Π_edge`.

Everything else in XXII is infrastructure or consequence.

---

## 2. Product Structure of the Main Theorem

The Main Theorem is not a single proof chain. It is a product:

```
Main Theorem  =  F_Gram  ×  F_Airy
```

| Factor | Content | Open node | Method |
|---|---|---|---|
| **F_Gram** | Ev\|_Edge is a uniform frame isomorphism | **O4** | Functional analysis, no RHP |
| **F_Airy** | inf σ(D^Airy) > 0 | **O5** | Airy oscillation, no arithmetic |

O4 and O5 are **not mutually reducible**.
Resolving either one in isolation yields a partial result.
Both are required for the full theorem.

---

## 3. The Four Structural Layers

```
┌─────────────────────────────────────────────────────┐
│ LAYER 0: Black boxes (imports, never re-proved)     │
│  BB1: Bulk ≈ (Paper XXI Thm A)                      │
│  BB2: ∃λ > 0 in σ(D_Edge) (Paper XXI Thm B)        │
│  BB3: Gram coercivity → gap ≥ c^{-1/2} (Paper 13b) │
│  BB5: Widom edge phase φ_c                          │
│  BB6: Deift–Zhou steepest descent                   │
└─────────────────────────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────────────┐
│ LAYER 1: IIKS representation (§2)                   │
│  P2 [exact identity]:                               │
│      K_c(x,y) = F_c(x)^T J G_c(y) / (x−y)         │
│  Purpose: coordinate system for the RHP, not proof  │
│  Key fact: cubic term 1/3 u^3 comes from Widom      │
│           phase integration, NOT from Fourier repr. │
└─────────────────────────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────────────┐
│ LAYER 2: Two-level obstruction (§3)                 │
│                                                     │
│  Edge stability = (phase consistency) + (geometry)  │
│                                                     │
│  Assumption A [OPEN = O1]:                          │
│    ∃ g_c with 2 Re(g_c^+) = Re(φ_c)  on (−1,1)    │
│    Nonlinear: φ_c = φ_c[g_c] (implicit coupling)   │
│    → Fixed-point operator T_c, Muskhelishvili route │
│                                                     │
│  Assumption B [conditional on A]:                   │
│    Steepest-descent geometry holds given g_c        │
│    → Standard Deift–Zhou once g_c is known          │
│                                                     │
│  Conjecture 3.3 [conditional on A+B]:               │
│    Y_c → Y_Airy  ⟹  ‖K̃_c − K^Airy‖_{S1} = O(c^{-1/3}) │
│                                                     │
│  !! O1 is NOT on the minimal path to Main Theorem !!│
└─────────────────────────────────────────────────────┘
           │
     ┌─────┴──────┐
     ▼            ▼
┌──────────┐  ┌──────────────────────────────────────┐
│ LAYER 3a │  │ LAYER 3b                             │
│ Gram–Gap │  │ Airy closure                         │
│  (§4)    │  │  (§5)                                │
│          │  │                                      │
│ O4       │  │ D^Airy = Π_Airy (A^arith − K^Airy)  │
│ [OPEN]:  │  │         Π_Airy                       │
│ Ev|_Edge │  │                                      │
│ uniform  │  │ O5 [OPEN]:                           │
│ quasi-   │  │ inf σ(D^Airy) ≥ c2^Airy > 0         │
│ isometry │  │ Method: Ai(t) > 0 for t > 0,         │
│          │  │ prime sampling non-degenerate         │
│    ↓     │  │          ↓                           │
│ Gram     │  │ P12: gap conjecture                  │
│ λ_min ≥  │  └──────────────────────────────────────┘
│ c^{-1/2} │                │
│    ↓     │                │
│ BB3      │                │
│ (import) │                │
└──────────┘                │
     │                      │
     └──────────┬───────────┘
                ▼
┌─────────────────────────────────────────────────────┐
│ LAYER 4: Main Theorem (§5, Thm 5.3)                 │
│                                                     │
│   inf_{f ∈ Edge, ‖f‖=1} ⟨D_Edge f, f⟩              │
│       ≥ c2^Airy / 2  > 0                           │
│                                                     │
│   Conditional on: O4 + O5                          │
│   (O1/O2 not required for this theorem)             │
│   (O1/O2 needed only for c^{-1/3} upgrade)         │
└─────────────────────────────────────────────────────┘
```

---

## 4. The Two Open Nodes (Full Specification)

### O4 — Frame Stability (functional-analytic)

**Statement:**
```
A‖f‖² ≤ ‖Ev f‖² ≤ B‖f‖²    for all f ∈ Edge,
with A > 0 uniform in n ∈ [(1−δ)N, N).
```

**Why it is hard:**
Standard Kadec-1/4 gives frame stability for frequencies in a band.
Here the frequencies are prime-spaced — no periodicity,
no group structure. The edge band is also shrinking as N → ∞.

**Attack route:**
- Schur-test on the edge Gram matrix via prime sum estimates
- Or: transfer uniform BW-Doubling (Paper III pointwise → edge block uniform)
- Or: Kadec-type stability for Paley–Wiener space on prime sampling sets

**Independence from O5:** Yes. No Airy functions appear.

---

### O5 — Airy Gap (spectral-analytic)

**Statement:**
```
inf σ(D^Airy) ≥ c2^Airy > 0
```
where `D^Airy = Π_Airy (A^arith − K^Airy) Π_Airy`.

**Why it is hard:**
`A^arith` is controlled by the prime distribution;
`K^Airy` is universal. Their mismatch must be
uniformly positive — this is a non-cancellation statement.

**Attack route:**
- `Ai(t) > 0` for all `t > 0` → sampling of `|Ai(t)|²`
  by prime-scaled points is non-degenerate
- Quantitative oscillation bounds on Airy functions
- Connection to first Airy zero `a₁ ≈ −2.338` via spectral counting

**Independence from O4:** Yes. No sampling geometry appears.

---

## 5. The Optional Enhancement Layer (O1/O2)

This is the RHP route. It is **not required** for the Main Theorem.
It provides the deeper result:

```
O1 (Assumption A, nonlinear RHP)
    ↓  Muskhelishvili + fixed point T_c
P5: g_c exists
    ↓
O2 (Assumption B, geometry)  ← standard Deift–Zhou
    ↓
P8: Y_c → Y_Airy
    ↓
c^{-1/3} gap scale  (vs. c^{-1/2} from the minimal path)
```

The enhancement is the **exponent**: `c^{-1/3}` instead of `c^{-1/2}`.
Both are non-trivial; the Airy exponent is the sharp one.

---

## 6. Minimal Path Summary

```
For inf σ(D_Edge) > 0 (Main Theorem):
  Resolve O4  AND  O5.  Done.

For gap ≥ c^{-1/3} (Airy-scale upgrade):
  Resolve O1  →  O2  →  P8.  Then combine with above.

For full programme closure:
  O4, O5, O1/O2  are all independent projects.
  Assign separately.
```

---

## 7. What Is Already Closed

| Item | Status |
|---|---|
| Bulk spectral match (A_{N,c} ≈ K_c) | ✓ Paper XXI Thm A |
| Existential edge obstruction (∃λ > 0) | ✓ Paper XXI Thm B |
| Gram → gap lower bound | ✓ Paper 13b (BB3) |
| IIKS representation of sinc kernel | ✓ exact identity |
| A/B obstruction decomposition | ✓ structural theorem |
| DAG with explicit mechanisms | ✓ paper22_dag.tex |
| Two independent open inputs identified | ✓ O4, O5 |
| O1 removed from minimal proof path | ✓ |

---
*Generated from `paper22_dag.tex` and `paper22_outline.tex`, May 2026.*
*This file is the operative working document. For full formal statements see the `.tex` files.*
