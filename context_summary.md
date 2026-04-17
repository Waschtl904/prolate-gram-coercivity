# Series Context Summary — Papers I–XVII

> **Purpose:** Paste this at the top of any new AI chat before working on Paper XVII or later.
> Provides the full logical chain without needing Papers I–XVI in full.
> **Current working file:** `paper_xvii.tex`
> **Repo:** `Waschtl904/prolate-gram-coercivity`
> **Last updated:** April 2026, after full GPT-referee review of all papers.

---

## Overarching Goal

The series constructs a spectral operator whose eigenvalue distribution
mirrors the non-trivial zeros of the Riemann zeta function (Hilbert–Pólya conjecture).
The core object is the PSWF concentration operator and its Mellin/Fourier transform.
Series arc: coercivity → scaling limits → spectral phase →
bandwidth decay → rigorous peak-width upper bounds → crossover asymptotics
→ lower bounds + spectral-zeta connection → domain & self-adjointness (conditional framework)
→ Mosco form convergence & Friedrichs extension → spectral inclusion & density criterion
→ localization principle for spectral projection stability
→ completeness barrier (Paper XIII) → coefficient stability / HS-norm estimates (Papers XIV–XV)
→ microlocal Lagrangian singularity transport / Airy normal form (Paper XVI)
→ **uniform CFU stability for PSWF fold geometry (Paper XVII)**.

---

## Central Notation

- `Phi_n^(c)`: rescaled PSWF, `Phi_n^(c)(u) = psi_n^(c)(e^u) e^{u/2}`, `u in (-inf,0)`
- `Phi_hat_n^(c)(t)`: Fourier–Mellin transform of `Phi_n^(c)`
- `t_*(c,n) ~ c^{1/2}`: Fourier peak location (saddle frequency)
- `Delta_eps(c,n)`: peak width — smallest Delta s.t. L2-mass outside `[t_*-Delta, t_*+Delta]` <= eps * total
- `lambda_n^(c)`: Slepian concentration eigenvalue, `lambda_n^(c) in (0,1)`
- `lambda_n^(inf)`: limit eigenvalue, `lambda_n^(inf) := lim_{c->inf} lambda_n^(c)` (Paper IX, inherited from VIII Cor 4.3)
- `Phi_n^(inf)`: strong limit of `Phi_n^(c_k)` along fixed diagonal subsequence `c_k`; ONS property holds (Paper XI)
- `Z_cross = {t : c^{-2/3} <= |t-t_*| <= c^{-1/3}}`: crossover zone
- `H_c`: finite-c PSWF concentration operator, bounded self-adjoint, `||H_c|| <= 1`
- `H_SOT` / `H_lim`: SOT-limit of H_c along `c_k`; bounded self-adjoint, `||H_SOT|| <= 1`
- `H_spec`: spectral operator `sum_n lambda_n^(inf) <f, Phi_n^(inf)> Phi_n^(inf)`; closable, symmetric
- `q_c`, `q_lim`: associated quadratic forms (Paper X)
- `kappa_n^(c)`: Airy normalisation coefficient, `|kappa_n^(c)| >= c_kappa > 0` (Paper VIII)
- `A_N^(c,(M))`, `D^(M)`: PSWF compression and diagonal reference operator (Papers XIV–XV)
- `Sigma_model(c)`: key intermediate-regime sum (Paper XV)
- `theta(xi)`: WKB phase; `theta'''(0) != 0` (Paper XV Lem. 4.2)
- `Phi(u;c)`: fold amplitude with cubic WKB phase (Paper XVI)
- `c_3(c)`: cubic WKB coefficient, `c_3(c) >= delta_0 > 0` (target of Paper XVII)
- `C`: canonical relation, locally `{(beta, Theta'(beta;c)+u; u, beta)}` (Paper XVI)

### ⚠️ Critical distinction

`H_SOT` and `H_spec` are **two separate objects**:
- `H_SOT` = SOT-limit, bounded, self-adjoint — **unconditional**
- `H_spec` = formal spectral series — **closable and symmetric, unconditional**
- `H_SOT = closure(H_spec)` is **Open Problem IX.7 / Paper X Bridge Theorem (conditional)** — **not proved**

---

## Papers I–VIII: Asymptotic Layer (FINAL)

- **I:** Gram matrix coercivity, constant `~ c^{-1/2}`
- **II:** Scaling limits, trace formula linking eigenvalues to primes
- **III:** Spectral phase analysis, evidence for `c^{-1/2}` peak-width scaling
- **IV:** No-go theorem — rules out naive bandlimited constructions
- **V:** Barrier estimate for `t >> t_*`; numerical evidence for `Delta_eps ~ c^{-1/2}`
- **VI:** Pointwise/L2/Airy bounds — Theorem 1 defers to Paper VII (companion preprint)
- **VII:** Peak width upper bound `Delta_eps <= C c^{-1/2}`; composite Airy–WKB
- **VIII:** Lower bound `Delta_eps >= c_1 c^{-1/2}`; sharp two-sided; Cor 4.3 exports `|lambda_n^(c)-lambda_n^(inf)| <= C c^{-1/4}`

## Papers IX–XIII: Functional-Analytic Layer (DRAFT)

- **IX:** Conditional framework; closability of H_spec; Open Problem 7 (Bridge)
- **X:** Mosco convergence; Friedrichs extension; Bridge conditional on Hyp.(IX.b)
- **XI:** Spectral inclusion; eigenvalue equation (along c_k only)
- **XII:** Localization principle (abstract, fully proved); Gap-S and SOT-Faster open
- **XIII:** Completeness barrier — no-reduction theorem; Route C incompatibility

## Papers XIV–XVII + fold_model: Microlocal Layer (DRAFT)

- **XIV:** HS decomposition Sigma_near + Sigma_int + Sigma_far
- **XV:** `Sigma_model = o(1)` (Cor. 5.3); cubic non-degeneracy confirmed (Lem. 4.2)
- **fold_model:** Universal CFU fold-amplitude normal form; phase diagram alpha < / = / > 1/2
- **XVI:** Lagrangian singularity transport; Airy normal form conditional on Assumption 4.1(i)–(vi); Open Problem prob:PSWF-microlocal
- **XVII:** Proof architecture for uniform CFU stability; two missing lemmas (see below)

---

## Two Remaining Closing Moves for Paper XVII

### Closing Move A — Paper XVIII-A
Explicit computation of classical period:
`T(lambda_n) = ∮_{E=lambda_n} dx / sqrt(lambda_n - V(x))`
for `V(x) = x^2/(1-x^2)`. Show `T(lambda_n) > 0` and control `partial_E T(lambda_n)`.
This is pure elliptic integral computation — no new ideas needed.

### Closing Move B — Paper XVIII-B
CFU-Jacobian Lemma: show
`J_total = J_can * J_Airy * J_symbol = |phi'| * (1 + O(h))`
uniform in `K_eps`, with explicit ellipticity lower bound of the symbolic factor in `S^{-1/2}_{1,0}`.
Standard CFU / Hörmander 3.2–3.3 + Zworski Ch.12 — no new ideas needed.

---

## Central Open Problems (as of April 2026)

| Problem | Front | Source |
|---|---|---|
| `H_SOT = closure(H_spec)` | Operator identification | Paper IX OP.7 |
| Uniform CFU Jacobian — Assumption 4.1(vi) | Microlocal | Paper XVI |
| `T(lambda_n)` explicit for `V(x)=x²/(1-x²)` | Classical dynamics | Paper XVII |
| Completeness of `{Phi_n^(inf)}` | Spectral completeness | Paper XI |
| Subsequence-independence | Spectral uniqueness | Paper XI |
| Gap lower bound | Spectral gap | Paper XII |
| Lipschitz regularity of PSWF amplitude | HS programme | Paper XV Prob.6.1 |
| Local Weyl law | HS programme | Paper XV Prob.7.1 |

---

## Key References

- Olver (1974): *Asymptotics and Special Functions*
- Osipov–Rokhlin–Xiao (2013): *Prolate Spheroidal Wave Functions of Order Zero*
- Slepian–Pollak (1961): Original PSWF paper
- CCM2025: Connes–Consani–Moscovici, arXiv:2511.22755
- Kato (1966): *Perturbation Theory for Linear Operators*
- Zworski (2012): *Semiclassical Analysis*, AMS
- Hörmander (1983): *Analysis of Linear PDE I* — Ch. 7.7, 18.1–18.2, 25.1
- Chester–Friedman–Ursell (1957): CFU steepest descent extension
- Guillemin–Uhlmann (1981): Oscillatory integrals with singular symbols
- Arnold (1972): Normal forms near degenerate critical points
- Reed–Simon (1975): *Methods of Modern Mathematical Physics, Vol. II*
- Mosco (1969): Convergence of convex sets
