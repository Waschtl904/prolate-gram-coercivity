"""
uprime_second_diff.py
=====================
Numerical scaling test for condition (U') of Paper VIII.

(U') states:
  |(lambda_l - lambda_{l+1}) - (F_Ai(x_l) - F_Ai(x_{l+1}))| <= C_2 * c^{-2/3}
  uniform in l throughout the transition window.

lambda_l in (0,1): eigenvalues of the concentration operator
  Q_c f(x) = int_{-1}^{1} sin(c(x-y)) / (pi*(x-y)) f(y) dy
via sinc kernel Gram matrix in Legendre basis:
  S[k,m] = int int sin(c(x-y))/(pi(x-y)) phi_k(x) phi_m(y) dx dy
  phi_k = sqrt((2k+1)/2) * P_k

Eigenvalues sorted descending: lambda_0 ~ 1, lambda_{N_Sh} ~ 0.5.
N_Sh = int(2c/pi)  (floor, NOT round).
M = 2*N_Sh + 20   (ensures crossing region is well inside computed spectrum).

Transition window: |l - N_Sh| <= A0 * c^{1/3}, A0 = 2.0 < |a_1| ~ 2.3381
c values: 30, 50, 100, 200, 400
"""

import numpy as np
from scipy.linalg import eigh
from scipy.special import airy, eval_legendre
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import json
import os

os.makedirs('numerics', exist_ok=True)

# ── Constants ──────────────────────────────────────────────────────────────
A0 = 2.0
C_VALUES = [30, 50, 100, 200, 400]
N_GRID = 800


def N_Sh(c):
    """Shannon number: int(2c/pi), floor."""
    return int(2.0 * c / np.pi)


# ── 1. Concentration eigenvalues via sinc kernel Gram matrix ────────────────
def get_concentration_eigenvalues(c, n_grid=N_GRID):
    """
    Eigenvalues of S[k,m] = int int K_c(x,y) phi_k(x) phi_m(y) dx dy
    K_c(x,y) = sin(c(x-y))/(pi*(x-y)), phi_k = sqrt((2k+1)/2)*P_k.
    M = 2*N_Sh + 20 ensures the 0.5-crossing is well inside the spectrum.
    Returns eigenvalues sorted descending.
    """
    nsh = N_Sh(c)
    M = 2 * nsh + 20

    x, w = np.polynomial.legendre.leggauss(n_grid)

    phi = np.zeros((M, n_grid))
    for k in range(M):
        phi[k] = np.sqrt((2*k+1)/2.0) * eval_legendre(k, x)

    xi, xj = np.meshgrid(x, x, indexing='ij')
    diff = xi - xj
    with np.errstate(divide='ignore', invalid='ignore'):
        K = np.where(np.abs(diff) < 1e-14,
                     c / np.pi,
                     np.sin(c * diff) / (np.pi * diff))

    phiw = phi * w[np.newaxis, :]
    S = phiw @ K @ phiw.T

    lam = eigh(S, eigvals_only=True)
    return np.sort(lam)[::-1]


# ── 2. F_Ai ────────────────────────────────────────────────────────────────
def F_Ai(x_arr):
    """F_Ai(x) = (x*Ai(x)^2 - Ai'(x)^2) / 2"""
    x_arr = np.asarray(x_arr, dtype=np.float64)
    Ai_vals, Aip_vals, _, _ = airy(x_arr)
    return (x_arr * Ai_vals**2 - Aip_vals**2) / 2.0


# ── 3. Transition window ───────────────────────────────────────────────────
def transition_window(c):
    nsh = 2.0 * c / np.pi          # exact float N_Sh
    half = A0 * c**(1.0/3.0)
    l_min = int(np.ceil(nsh - half))
    l_max = int(np.floor(nsh + half))
    return np.arange(l_min, l_max + 1)


def rescaled_index(l, c):
    return (l - 2.0 * c / np.pi) * (c / 2.0)**(-1.0/3.0)


# ── 4. Main computation ────────────────────────────────────────────────────
print("Computing concentration eigenvalues lambda_l in (0,1)...")
print("(sinc kernel Gram matrix; M = 2*N_Sh + 20 per c value)")

results = {}
for c in C_VALUES:
    print(f"  c = {c} ...", end=" ", flush=True)
    lam_all = get_concentration_eigenvalues(c)

    nsh = N_Sh(c)
    lam_near = lam_all[nsh-2:nsh+3]
    print(f"N_Sh={nsh}, M={2*nsh+20}, lam[N_Sh-2:N_Sh+3]={np.round(lam_near,3)}", end=" ")

    # verify crossing
    crossing = np.where(np.diff(np.sign(lam_all - 0.5)))[0]
    print(f"| crossing at {crossing}", end=" ")

    idx = transition_window(c)
    idx = idx[(idx + 2 < len(lam_all)) & (idx >= 0)]

    lam_w  = lam_all[idx]
    lam_p1 = lam_all[idx + 1]
    lam_p2 = lam_all[idx + 2]
    Delta_lam = lam_w - 2*lam_p1 + lam_p2

    x_l0 = rescaled_index(idx,     c)
    x_l1 = rescaled_index(idx + 1, c)
    x_l2 = rescaled_index(idx + 2, c)
    Delta_Ai = F_Ai(x_l0) - 2*F_Ai(x_l1) + F_Ai(x_l2)

    scale = c**(2.0/3.0)
    Delta_lam_scaled = scale * Delta_lam
    Delta_Ai_scaled  = scale * Delta_Ai
    max_scaled = np.max(np.abs(Delta_lam_scaled))

    print(f"| window={len(idx)}, max|c^{{2/3}} Delta|={max_scaled:.4f}")

    results[c] = {
        'x_l':              x_l0,
        'lam_window':       lam_w,
        'Delta_lam_scaled': Delta_lam_scaled,
        'Delta_Ai_scaled':  Delta_Ai_scaled,
        'max_scaled':       max_scaled,
        'n_window':         len(idx),
        'N_Sh':             nsh,
        'crossing':         crossing.tolist(),
    }


# ── 5. Plot A: scaled second differences ──────────────────────────────────
print("\nPlot A: scaled second differences...")
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
axes_flat = axes.flatten()

for i, c in enumerate(C_VALUES):
    ax = axes_flat[i]
    r = results[c]
    ax.plot(r['x_l'], r['Delta_lam_scaled'],
            color='#1f77b4', lw=1.8, label=r'$c^{2/3}\Delta_\lambda$')
    ax.plot(r['x_l'], r['Delta_Ai_scaled'],
            color='#ff7f0e', lw=1.8, ls='--', label=r'$c^{2/3}\Delta_{\rm Ai}$')
    ax.axhline(0, color='gray', lw=0.8, ls=':')
    ax.set_title(f'c = {c}  (N_Sh={r["N_Sh"]})', fontsize=11)
    ax.set_xlabel(r'$x_l = (l-N_{\rm Sh})(c/2)^{-1/3}$', fontsize=9)
    ax.set_ylabel(r'$c^{2/3} \cdot \Delta$', fontsize=9)
    if i == 0:
        ax.legend(fontsize=9)

axes_flat[-1].set_visible(False)
fig.suptitle(
    r'Scaled Second Differences $c^{2/3}\Delta_l$ vs $x_l$' + '\n'
    r'Blue: $\lambda_l$ (concentration eigenvalues) $\quad$ Orange: Airy $F_{\rm Ai}$',
    fontsize=12
)
plt.tight_layout(rect=[0, 0, 1, 0.92])
plt.savefig('numerics/uprime_A_scaled_second_diff.png', dpi=150, bbox_inches='tight')
plt.close()
print("  Saved: uprime_A_scaled_second_diff.png")


# ── 6. Plot B: log-log scaling ─────────────────────────────────────────────
print("Plot B: log-log scaling...")
c_arr   = np.array(C_VALUES, dtype=float)
max_arr = np.array([results[c]['max_scaled'] for c in C_VALUES])
log_c   = np.log(c_arr)
log_max = np.log(max_arr)
alpha, const = np.polyfit(log_c, log_max, 1)
fit_line = np.exp(const) * c_arr**alpha

print(f"  Power-law fit: max|c^{{2/3}} Delta| ~ c^{{{alpha:.3f}}}")
print(f"  alpha ~ 0  => (U') holds at scale c^{{-2/3}}")
print(f"  alpha < 0  => Delta decays faster, (U') conservative")
print(f"  alpha > 0  => (U') may fail at this scale")

fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.loglog(c_arr, max_arr, 'o-', color='#1f77b4', lw=2.5, ms=9,
           label=r'$\max|c^{2/3}\Delta_\lambda|$')
ax2.loglog(c_arr, fit_line, '--', color='#d62728', lw=2,
           label=fr'fit $\sim c^{{{alpha:.3f}}}$')
ax2.axhline(1.0, color='green', lw=1.5, ls=':', label='O(1) reference')
ax2.set_xlabel('c (bandwidth)', fontsize=12)
ax2.set_ylabel(r'$\max|c^{2/3} \cdot \Delta_\lambda|$', fontsize=12)
ax2.set_title(
    r'Log-Log Scaling: $\max|c^{2/3}\Delta_\lambda|$ vs $c$' + '\n'
    fr'Fit exponent $\alpha = {alpha:.3f}$ '
    r'($\alpha \approx 0$: (U$^\prime$) plausible; $\alpha > 0$: too weak)',
    fontsize=12
)
ax2.legend(fontsize=11)
ax2.set_xticks(C_VALUES)
ax2.set_xticklabels([str(c) for c in C_VALUES])
plt.tight_layout()
plt.savefig('numerics/uprime_B_loglog_scaling.png', dpi=150, bbox_inches='tight')
plt.close()
print("  Saved: uprime_B_loglog_scaling.png")


# ── 7. Save summary JSON ───────────────────────────────────────────────────
summary = {
    'operator': 'concentration operator Q_c, sinc kernel Gram matrix in Legendre basis',
    'N_Sh_formula': 'int(2c/pi)  [floor]',
    'M_formula': '2*N_Sh + 20',
    'A0': A0,
    'c_values': C_VALUES,
    'power_law_exponent_alpha': float(alpha),
    'interpretation': (
        "alpha~0: (U') plausible at c^{-2/3}; "
        "alpha<0: Delta decays faster; "
        "alpha>0: (U') may fail"
    ),
    'per_c': {
        str(c): {
            'N_Sh': results[c]['N_Sh'],
            'crossing_index': results[c]['crossing'],
            'window_size': int(results[c]['n_window']),
            'max_scaled_second_diff': float(results[c]['max_scaled']),
            'lam_window_min': float(results[c]['lam_window'].min()),
            'lam_window_max': float(results[c]['lam_window'].max()),
        } for c in C_VALUES
    }
}
with open('numerics/uprime_scaling_summary.json', 'w') as f:
    json.dump(summary, f, indent=2)
print("  Saved: uprime_scaling_summary.json")

print("\nDone. Outputs in numerics/:")
print("  uprime_A_scaled_second_diff.png")
print("  uprime_B_loglog_scaling.png")
print("  uprime_scaling_summary.json")
