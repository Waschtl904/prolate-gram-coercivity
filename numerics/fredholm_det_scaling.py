"""
Fredholm Determinant Scaling Experiment
========================================
Paper XI (prolate-gram-coercivity programme)

Goal: distinguish Scenario (A) vs (B) of Paper XI, Section 4.

  Compute  log|D_c(1)| = log|det(I - T_c)|
  where T_c is the prolate operator on [-1,1] with bandwidth c,
  using the Bornemann (2010) discretisation:

    [T_c]_{ij} = w_j * K_c(x_i, x_j),
    K_c(x,y)  = sin(c*(x-y)) / (pi*(x-y)),  K_c(x,x) = c/pi.

  Then log|D_c(1)| = log|det(I - K_c^{(m)})|
  approximated to high accuracy with m-point Gauss-Legendre nodes.

Scaling models (Paper XI, §4):
  Scenario (B):  log|D_c(1)| ~ -alpha * c^{2/3}   (exponential dominance)
  Scenario (A):  log|D_c(1)| ~ -beta * log(c)      (polynomial gap possible)
  Intermediate:  log|D_c(1)| ~ -gamma * c           (bulk dominance)

Output:
  - Table of log|D_c(1)| for c in C_VALUES, m in M_VALUES
  - Convergence check in m for each c
  - Fit of log|D_c(1)| vs c^{2/3}, log(c), c
  - Plot: log|D_c(1)| vs c with fitted curves
  - Saves: numerics/fredholm_det_results.csv
            numerics/fredholm_det_scaling.png
"""

import numpy as np
from numpy.linalg import slogdet
from numpy.polynomial.legendre import leggauss
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

# ------------------------------------------------------------------ #
# Parameters
# ------------------------------------------------------------------ #

C_VALUES  = [5, 10, 20, 50, 100, 200]   # bandwidth values
M_VALUES  = [32, 64, 128, 256]           # quadrature sizes (convergence check)
M_PRODUCTION = 256                        # m used for final fits

OUTDIR = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ #
# Core: build discretised prolate kernel matrix (Bornemann style)
# ------------------------------------------------------------------ #

def gauss_legendre_on(a, b, m):
    """Gauss-Legendre nodes and weights on [a, b]."""
    xi, wi = leggauss(m)
    x = 0.5*(b - a)*xi + 0.5*(b + a)
    w = 0.5*(b - a)*wi
    return x, w


def prolate_kernel_matrix(c, m):
    """
    Build the m x m matrix  K_{ij} = w_j * K_c(x_i, x_j)
    on [-1, 1] with Gauss-Legendre quadrature of order m.

    K_c(x, y) = sin(c*(x-y)) / (pi*(x-y))
    K_c(x, x) = c / pi  (limit)
    """
    x, w = gauss_legendre_on(-1, 1, m)
    # outer difference matrix
    X = x[:, None] - x[None, :]          # (m, m), X_ij = x_i - x_j
    with np.errstate(divide='ignore', invalid='ignore'):
        K = np.where(np.abs(X) < 1e-14,
                     c / np.pi,
                     np.sin(c * X) / (np.pi * X))
    # weight columns: K_{ij} -> w_j * K_c(x_i, x_j)
    K = K * w[None, :]
    return K


def log_fredholm_det(c, m):
    """
    Compute log|det(I - K_c^{(m)})| via numpy slogdet.
    Returns (log_abs_det, sign).
    """
    K = prolate_kernel_matrix(c, m)
    A = np.eye(m) - K
    sign, logabsdet = slogdet(A)
    return float(logabsdet), int(sign)


# ------------------------------------------------------------------ #
# Convergence check in m
# ------------------------------------------------------------------ #

def convergence_table():
    rows = []
    for c in C_VALUES:
        vals = {}
        for m in M_VALUES:
            ld, sg = log_fredholm_det(c, m)
            vals[m] = ld
        # convergence: difference between successive m
        diffs = {M_VALUES[i+1]: abs(vals[M_VALUES[i+1]] - vals[M_VALUES[i]])
                 for i in range(len(M_VALUES)-1)}
        row = {'c': c}
        for m in M_VALUES:
            row[f'logdet_m{m}'] = vals[m]
        for m, d in diffs.items():
            row[f'diff_m{m}'] = d
        rows.append(row)
    return pd.DataFrame(rows)


# ------------------------------------------------------------------ #
# Production run and scaling fit
# ------------------------------------------------------------------ #

def production_run():
    """Compute log|D_c(1)| at M_PRODUCTION for all C_VALUES."""
    records = []
    for c in C_VALUES:
        ld, sg = log_fredholm_det(c, M_PRODUCTION)
        records.append({
            'c': c,
            'log_det': ld,
            'sign': sg,
            'c23': c**(2/3),
            'logc': np.log(c),
            'c_val': float(c),
        })
    return pd.DataFrame(records)


def fit_scaling(df):
    """
    Fit three models to (c, log|D_c(1)|):
      Model 1 (exp):  log|D| = a1 * c^{2/3} + b1
      Model 2 (poly): log|D| = a2 * log(c) + b2
      Model 3 (bulk): log|D| = a3 * c + b3
    Returns dict of fit parameters and residuals.
    """
    y = df['log_det'].values

    def lstsq_fit(X):
        X_ = np.column_stack([X, np.ones(len(X))])
        coef, res, *_ = np.linalg.lstsq(X_, y, rcond=None)
        y_hat = X_ @ coef
        ss_res = np.sum((y - y_hat)**2)
        ss_tot = np.sum((y - y.mean())**2)
        r2 = 1 - ss_res/ss_tot if ss_tot > 0 else np.nan
        return coef, r2

    fits = {}
    coef1, r2_1 = lstsq_fit(df['c23'].values)
    fits['exp_c23']  = {'slope': coef1[0], 'intercept': coef1[1], 'R2': r2_1,
                         'label': r'$\alpha\,c^{2/3}$'}

    coef2, r2_2 = lstsq_fit(df['logc'].values)
    fits['poly_logc'] = {'slope': coef2[0], 'intercept': coef2[1], 'R2': r2_2,
                          'label': r'$\beta\,\log c$'}

    coef3, r2_3 = lstsq_fit(df['c_val'].values)
    fits['bulk_c']   = {'slope': coef3[0], 'intercept': coef3[1], 'R2': r2_3,
                         'label': r'$\gamma\,c$'}
    return fits


# ------------------------------------------------------------------ #
# Plot
# ------------------------------------------------------------------ #

def make_plot(df, fits):
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not available; skipping plot.")
        return

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    c_arr = df['c'].values.astype(float)
    y_arr = df['log_det'].values

    # --- Left: raw data + three model fits ---
    ax = axes[0]
    ax.scatter(c_arr, y_arr, color='black', zorder=5, s=50,
               label=r'$\log|D_c(1)|$ (numerical)')

    c_fine = np.linspace(c_arr.min(), c_arr.max(), 300)
    colors = {'exp_c23': '#e74c3c', 'poly_logc': '#2ecc71', 'bulk_c': '#3498db'}
    labels = {'exp_c23': r'Fit: $\alpha c^{2/3}$ (Scenario B)',
              'poly_logc': r'Fit: $\beta\log c$ (Scenario A)',
              'bulk_c': r'Fit: $\gamma c$ (bulk)'}
    regressors = {'exp_c23': c_fine**(2/3),
                  'poly_logc': np.log(c_fine),
                  'bulk_c': c_fine}

    for key, fit in fits.items():
        y_fit = fit['slope'] * regressors[key] + fit['intercept']
        ax.plot(c_fine, y_fit, color=colors[key], lw=1.8,
                label=f"{labels[key]}  ($R^2={fit['R2']:.4f}$)")

    ax.set_xlabel('$c$', fontsize=13)
    ax.set_ylabel(r'$\log|D_c(1)|$', fontsize=13)
    ax.set_title('Scaling of Fredholm Determinant', fontsize=13)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # --- Right: log|D_c(1)| / c^{2/3} vs c  (should be ~ const if Scenario B) ---
    ax2 = axes[1]
    ratio = y_arr / c_arr**(2/3)
    ax2.plot(c_arr, ratio, 'o-', color='#e74c3c', lw=1.8)
    ax2.axhline(y=ratio[-1], color='gray', lw=1, linestyle='--')
    ax2.set_xlabel('$c$', fontsize=13)
    ax2.set_ylabel(r'$\log|D_c(1)| / c^{2/3}$', fontsize=13)
    ax2.set_title(r'Ratio test: flat $\Rightarrow$ Scenario B, '
                  r'$\to 0$ $\Rightarrow$ Scenario A', fontsize=11)
    ax2.grid(True, alpha=0.3)

    fig.tight_layout()
    outpath = os.path.join(OUTDIR, 'fredholm_det_scaling.png')
    fig.savefig(outpath, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"Plot saved: {outpath}")


# ------------------------------------------------------------------ #
# Main
# ------------------------------------------------------------------ #

if __name__ == '__main__':
    print("=" * 60)
    print("Fredholm Determinant Scaling Experiment (Paper XI)")
    print("=" * 60)

    # 1. Convergence in m
    print("\n--- Convergence in quadrature size m ---")
    conv = convergence_table()
    print(conv.to_string(index=False, float_format=lambda x: f"{x:.6f}"))

    # 2. Production values
    print(f"\n--- Production run (m = {M_PRODUCTION}) ---")
    df = production_run()
    print(df[['c', 'log_det', 'sign']].to_string(index=False,
          float_format=lambda x: f"{x:.6f}"))

    # 3. Fit
    print("\n--- Scaling fits ---")
    fits = fit_scaling(df)
    for key, fit in fits.items():
        print(f"  {key:12s}:  slope = {fit['slope']:+.4f}, "
              f"intercept = {fit['intercept']:+.4f}, "
              f"R^2 = {fit['R2']:.6f}")

    # 4. Interpretation
    print("\n--- Interpretation ---")
    r2_exp  = fits['exp_c23']['R2']
    r2_poly = fits['poly_logc']['R2']
    r2_bulk = fits['bulk_c']['R2']
    best = max(fits, key=lambda k: fits[k]['R2'])
    print(f"  Best fit: {best}  (R^2 = {fits[best]['R2']:.6f})")
    if best == 'exp_c23':
        print("  => SCENARIO (B) supported: log|D_c(1)| ~ c^{2/3}")
        print("     Superexponential suppression; B-strong likely FALSE.")
    elif best == 'poly_logc':
        print("  => SCENARIO (A) supported: log|D_c(1)| ~ log(c)")
        print("     Polynomial gap possible; B-strong may be TRUE.")
    elif best == 'bulk_c':
        print("  => BULK dominance: log|D_c(1)| ~ c")
        print("     Consistent with Scenario (B), bulk version.")
    else:
        print("  => Inconclusive.")

    # 5. Save CSV
    csv_path = os.path.join(OUTDIR, 'fredholm_det_results.csv')
    df.to_csv(csv_path, index=False)
    print(f"\nResults saved: {csv_path}")

    # 6. Plot
    make_plot(df, fits)

    print("\nDone.")
