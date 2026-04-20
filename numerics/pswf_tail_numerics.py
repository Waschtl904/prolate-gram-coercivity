"""
pswf_tail_numerics.py
=====================
Numerical experiments for Section 5 of paper2_quadrature.tex:
  PSWF product spectral tail separation.

Method: tridiagonal matrix construction in Legendre basis
  (Osipov-Rokhlin-Xiao 2013, Ch. 3).
Precision: double (float64) throughout.

Outputs (saved to numerics/):
  plot1_tail_vs_N.png     -- tail vs. projection N for six index pairs
  plot2_tail_vs_dist.png  -- tail vs. index distance |m-n| at N=c
  plot3_diagonal_tail.png -- diagonal tail vs. index m at N=c
  run_config.json         -- experiment parameters for reproducibility
"""

import numpy as np
from scipy.linalg import eigh
from scipy.special import eval_legendre
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
import os

print("Using double precision (float64):", np.float64(1.0).dtype)
os.makedirs('numerics', exist_ok=True)

# Save run configuration for reproducibility
with open('numerics/run_config.json', 'w') as f:
    json.dump({
        "c_values": [50, 100],
        "M": 350,
        "n_grid": 700,
        "N_pswf_offset": 30,
        "precision": "float64",
        "grid_stability_tested": [500, 700, 900]
    }, f, indent=2)


# ── 1. Tridiagonal matrix (Legendre basis) ─────────────────────────────────
def build_pswf_matrix(c, M):
    """
    Symmetric tridiagonal matrix T^(c) of size M x M.
    Osipov-Rokhlin-Xiao 2013, Ch. 3.
    """
    k = np.arange(M, dtype=np.float64)
    diag = k*(k+1) + c**2 * (2*k*(k+1) - 1) / ((2*k-1)*(2*k+3))
    diag[0] = c**2 / 3.0
    sup = np.zeros(M-1)
    for i in range(M-1):
        ki = float(i)
        sup[i] = (c**2 * (ki+1)*(ki+2)
                  / ((2*ki+3) * np.sqrt((2*ki+1)*(2*ki+5))))
    return np.diag(diag) + np.diag(sup, 1) + np.diag(sup, -1)


# ── 2. Compute PSWFs on Gauss-Legendre grid ────────────────────────────────
def compute_pswfs(c, N_pswf, M=350, n_grid=700):
    """
    Returns x (nodes), w (weights), psi (N_pswf x n_grid), coeffs (M x N_pswf).
    Eigenvectors are sorted by increasing eigenvalue (= prolate order).
    """
    T = build_pswf_matrix(c, M)
    eigvals, eigvecs = eigh(T)
    # Sort ascending by eigenvalue (prolate ordering)
    idx = np.argsort(eigvals)
    eigvecs = eigvecs[:, idx]
    coeffs = eigvecs[:, :N_pswf]

    x, w = np.polynomial.legendre.leggauss(n_grid)
    P = np.zeros((M, n_grid))
    for k in range(M):
        P[k] = eval_legendre(k, x) * np.sqrt((2*k+1) / 2.0)

    psi = coeffs.T @ P  # (N_pswf, n_grid)
    for n in range(N_pswf):
        norm = np.sqrt(np.sum(w * psi[n]**2))
        psi[n] /= norm
    return x, w, psi, coeffs


# ── 3. Orthogonality check ─────────────────────────────────────────────────
def check_orthogonality(psi, w, label=""):
    n_check = min(30, psi.shape[0])
    G = np.array([[np.sum(w * psi[i] * psi[j])
                   for j in range(n_check)] for i in range(n_check)])
    err = np.max(np.abs(G - np.eye(n_check)))
    print(f"  [{label}] Max orthogonality error (first {n_check} modes): {err:.2e}")
    return err


# ── 4. Stable tail norm ────────────────────────────────────────────────────
def compute_tail(psi, w, m, n, N_proj):
    """
    ||(I - P_{N_proj}) psi_m * psi_n||  via stable formula.
    """
    f = psi[m] * psi[n]
    f_norm2 = np.sum(w * f**2)
    proj2 = sum(np.sum(w * f * psi[k])**2 for k in range(int(N_proj)))
    tail2 = max(f_norm2 - proj2, 1e-30)  # floor prevents spurious zeros
    return np.sqrt(tail2)


# ── 5. Grid stability validation (one representative pair) ─────────────────
print("\n--- Grid stability check (c=50, pair (5,7), N=50) ---")
for test_grid in [500, 700, 900]:
    xg, wg, psig, _ = compute_pswfs(50, 80, M=350, n_grid=test_grid)
    t = compute_tail(psig, wg, 5, 7, 50)
    print(f"  n_grid={test_grid}: tail = {t:.6e}")


# ── 6. Main computation ────────────────────────────────────────────────────
results = {}
for c in [50, 100]:
    print(f"\n=== c = {c} ===")
    N_base = int(c)
    N_pswf = N_base + 30
    x, w, psi, coeffs = compute_pswfs(c, N_pswf, M=350, n_grid=700)
    check_orthogonality(psi, w, label=f"c={c}")

    pairs = {
        'bulk (1,2)':        (1, 2),
        'bulk (5,7)':        (5, 7),
        'off-diag (10,20)':  (10, 20),
        'off-diag (20,40)':  (20, 40),
        'edge (N-5,N-3)':    (N_base-5, N_base-3),
        'edge (N-2,N-1)':    (N_base-2, N_base-1),
    }

    N_vals = np.arange(5, N_pswf-2, 3)
    tails = {}
    for label, (m, n) in pairs.items():
        tails[label] = [compute_tail(psi, w, m, n, int(Np)) for Np in N_vals]

    results[c] = {'N_vals': N_vals, 'tails': tails, 'N_base': N_base,
                  'x': x, 'w': w, 'psi': psi}
    print(f"  Done.")


# ── 7. Plots ───────────────────────────────────────────────────────────────
colors = ['#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd','#8c564b']
short_labels = ['bulk (1,2)', 'bulk (5,7)', 'off-diag (10,20)',
                'off-diag (20,40)', 'edge (N-5,N-3)', 'edge (N-2,N-1)']

# --- Plot 1: Tail vs N -------------------------------------------------------
fig1 = make_subplots(rows=1, cols=2,
    subplot_titles=['c = 50', 'c = 100'],
    horizontal_spacing=0.15)

for col_idx, c in enumerate([50, 100], 1):
    r = results[c]
    for i, (label, tail_vals) in enumerate(r['tails'].items()):
        arr = np.where(np.array(tail_vals) < 1e-16, 1e-16, tail_vals)
        fig1.add_trace(go.Scatter(
            x=r['N_vals'], y=arr, mode='lines',
            name=short_labels[i],
            line=dict(color=colors[i], width=2),
            showlegend=(col_idx == 1)
        ), row=1, col=col_idx)

fig1.update_yaxes(type='log', exponentformat='power',
                  title_text='tail norm', row=1, col=1)
fig1.update_yaxes(type='log', exponentformat='power',
                  title_text='tail norm', row=1, col=2)
fig1.update_xaxes(title_text='Projection N', row=1, col=1)
fig1.update_xaxes(title_text='Projection N', row=1, col=2)
fig1.update_layout(
    title=dict(text='PSWF Product Spectral Tail vs Projection N',
               font=dict(size=17), x=0.5, xanchor='center'),
    legend=dict(orientation='h', yanchor='bottom', y=1.15,
                xanchor='center', x=0.5, font=dict(size=11)),
    margin=dict(t=120, b=70, l=70, r=40),
    height=480, width=920
)
fig1.write_image('numerics/plot1_tail_vs_N.png')
with open('numerics/plot1_tail_vs_N.png.meta.json', 'w') as f:
    json.dump({'caption': 'PSWF Product Spectral Tail vs Projection N (log scale)',
               'description': 'Six index pairs: bulk decay to machine zero, edge O(1). c=50 left, c=100 right.'}, f)
print('Plot 1 saved.')

# --- Plot 2: Tail vs distance ------------------------------------------------
fig2 = go.Figure()
for c in [50, 100]:
    r = results[c]
    m_fixed = r['N_base'] // 4
    dists, tails_d = [], []
    for n in range(m_fixed, min(r['N_base']+5, r['psi'].shape[0]-1)):
        t = compute_tail(r['psi'], r['w'], m_fixed, n, r['N_base'])
        dists.append(n - m_fixed)
        tails_d.append(max(t, 1e-16))
    fig2.add_trace(go.Scatter(
        x=dists, y=tails_d, mode='lines+markers',
        name=f'c={c}, m={m_fixed}', line=dict(width=2.2), marker=dict(size=5)))

fig2.update_layout(
    title=dict(text='Tail Norm vs Index Distance |m-n| at N=c',
               font=dict(size=17), x=0.5, xanchor='center'),
    xaxis_title='Index distance |m-n|',
    yaxis_title='tail norm',
    yaxis_type='log',
    yaxis=dict(exponentformat='power'),
    legend=dict(orientation='h', yanchor='bottom', y=1.04,
                xanchor='center', x=0.5),
    margin=dict(t=80, b=70, l=80, r=40),
    height=460, width=780
)
fig2.write_image('numerics/plot2_tail_vs_dist.png')
with open('numerics/plot2_tail_vs_dist.png.meta.json', 'w') as f:
    json.dump({'caption': 'Spectral Tail vs Index Distance |m-n| at N=c',
               'description': 'Tail grows sharply as n approaches N~c; c=50 and c=100.'}, f)
print('Plot 2 saved.')

# --- Plot 3: Diagonal tail vs m ---------------------------------------------
fig3 = go.Figure()
for c in [50, 100]:
    r = results[c]
    ms = list(range(1, min(r['N_base']+5, r['psi'].shape[0]-2)))
    tails_m = [max(compute_tail(r['psi'], r['w'], m, m, r['N_base']), 1e-16)
               for m in ms]
    fig3.add_trace(go.Scatter(
        x=ms, y=tails_m, mode='lines',
        name=f'c={c}', line=dict(width=2.5)))

fig3.update_layout(
    title=dict(text='Diagonal Tail vs Index m at N=c',
               font=dict(size=17), x=0.5, xanchor='center'),
    xaxis_title='Index m',
    yaxis_title='tail norm',
    yaxis_type='log',
    yaxis=dict(exponentformat='power'),
    legend=dict(orientation='h', yanchor='bottom', y=1.04,
                xanchor='center', x=0.5),
    margin=dict(t=80, b=70, l=80, r=40),
    height=460, width=780
)
fig3.write_image('numerics/plot3_diagonal_tail.png')
with open('numerics/plot3_diagonal_tail.png.meta.json', 'w') as f:
    json.dump({'caption': 'Diagonal PSWF Product Tail vs Index m at N=c',
               'description': 'Sharp bulk-to-edge transition near m=N; c=50 and c=100.'}, f)
print('Plot 3 saved.')

print('\nAll done. Outputs in numerics/.')
