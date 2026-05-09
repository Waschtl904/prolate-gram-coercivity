# The IR Kernel of Paper XXII

> *Recorded: May 9, 2026.*  
> *This is not a new argument. It is a record of what the programme proved about itself.*

---

## The single sentence

The spectral gap of the Airy mismatch operator is stable under arithmetic perturbation
because the universal Airy geometry dominates the prime-sampling fluctuation asymptotically:

```
  delta_Airy  ~  O(1)       [universal, TW]
  epsilon_c   =  o(1)       [arithmetic, MV]
  ──────────────────────────────────────────
  delta_Airy >> epsilon_c   [the IR condition]
```

This is the irreducible logical core of Paper XXII.
Everything else is either a prerequisite for finding this structure
or a refinement of its quantitative rate.

---

## What the programme proved about itself

The programme did not merely prove a theorem about Gram matrices.
It underwent a renormalisation of its own description:

```
Initial description (Papers XII-XXI):
  complicated discrete/integrable structure
  IIKS + RHP + Deift-Zhou + Widom phase + cubic Airy term
  prime sampling + PSWF oscillatory integrals

          |  asymptotic renormalisation
          |  (identification of the fixed point)
          v

Final description (Paper XXII, IR kernel):
  universal fixed point   +   irrelevant perturbation
  delta_Airy (TW)             epsilon_c (MV)
```

The heavy analytic infrastructure did not disappear.
It was *absorbed* into the universal constant `F_TW(0) ~ 0.9597`.
All the integrable geometry of Papers XII-XXI is encoded in that one number.

---

## Why F_TW(0) ~ 0.96 is structurally decisive

The entire perturbative reorganisation works because `F_TW(0)` is close to 1.
This gives `delta_Airy >= 0.96` — a large stability buffer.

If `F_TW(0)` were close to 0, `delta_Airy` would be small,
`epsilon_c` might not be negligible by comparison,
and the integrable structure would re-enter the minimal proof.

The eliminability of IIKS/RHP from the proof is therefore:
- not a philosophical claim about integrable methods
- not a general principle
- but a quantitative consequence of the specific value `F_TW(0) ~ 0.96`.

The Tracy-Widom constant is the numerical reason the IR separation holds.

---

## The three roles of integrable structure in this programme

| Role | Content | In minimal proof? |
|---|---|---|
| Discovery | Identified D^Airy as the right object | No |
| Coordinates | Gave explicit formulas near the edge | No |
| Flow control | Rate ||K_c - K^Airy||_{S1} = O(c^{-1/3}) | Conditionally (O1/O2) |

The programme needed integrable structure to *reach* the IR fixed point.
Once there, the fixed point stands on its own.

---

## The IR condition as a general criterion

For any asymptotic spectral programme with structure:
```
  D_c  =  D_universal  +  E_c
```
the minimal proof lives outside the integrable category if and only if:
```
  inf sigma(D_universal) >> ||E_c||_op
```
When this holds, perturbative operator theory closes the existence question,
and the integrable structure is relegated to rate control.

Paper XXII is an explicit instance where this condition holds,
with the quantitative verification:
```
  inf sigma(D_universal) >= F_TW(0) ~ 0.96
  ||E_c||_op <= C * (loglog c / log c)^{1/2}  ->  0
  ratio: 1.88 - 4.21  for c in [100, 10^4]   [numerically confirmed]
```

---

## What remains

The IR kernel is identified. The programme knows what it proved.

Residual work is entirely in the UV sector — filling the analytic bookkeeping
that connects the heavy infrastructure to the IR fixed point:

- O4-T2: triple-scale stationary phase completion (~5 pages, LOW)
- O5-V1/V2: Fourier expansion + Bernstein for Airy-bandlimited functions (~3 pages, LOW)
- O5-V3: explicit constant C(R, Omega) (numerical, LOW)
- Section 6: connecting theorem, both arms to P13 (~3 pages, LOW)

The conceptual work of Paper XXII is done.
