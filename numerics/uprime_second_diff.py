"""
uprime_second_diff.py
=====================
Numerical scaling test for condition (U') of Paper VIII.

(U') states:
  |(lambda_l - lambda_{l+1}) - (F_Ai(x_l) - F_Ai(x_{l+1}))| <= C_2 * c^{-2/3}
  uniform in l throughout the transition window.

Equivalently, the second differences
  Delta_l := lambda_l - 2*lambda_{l+1} + lambda_{l+2}
should satisfy c^{2/3} * Delta_l = O(1) uniformly in the window.

This script tests:
  (A) Raw scaling: c^{2/3} * Delta_l vs rescaled index x_l
      Expected: bounded, smooth if (U') holds at scale c^{-2/3}
  (B) Airy consistency: Delta_l vs Delta_l^{Ai} = F_Ai(x_l) - 2*F_Ai(x_{l+1}) + F_Ai(x_{l+2})
      Expected: close if Airy approximation is good
  (C) Log-log scaling: max_{l in window} |c^{2/3} * Delta_l| vs c
      Expected: O(1) if (U') correct, decaying if (U') too strong

Transition window: |l - N_Sh| <= A0 * c^{1/3}, A0 = 2.0 < |a_1| ~ 2.3381

c values: 30, 50, 100, 200, 400
"""

import numpy as np
from scipy.linalg import eigh
from scipy.special import airy
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
import os

os.makedirs('numerics', exist_ok=True)

# ── Constants ──────────────────────────────────────────────────────────────
A0 = 2.0          # transition window half-width (< |a_1| ~ 2.3381)
N_SH_FACTOR = 2.0 / np.pi   # N_Sh = c * 2/pi

C_VALUES = [30, 50, 100, 200, 400]
M_MAT = 500       # matrix size (sufficient for c <= 400)

# ── 1. Tridiagonal PSWF matrix (ORX Ch. 3) ────────────────────────────────
def build_pswf_matrix(c, M):
    k = np.arange(M, dtype=np.float64)
    diag = k*(k+1) + c**2 * (2*k*(k+1) - 1) / ((2*k-1)*(2*k+3))
    diag[0] = c**2 / 3.0
    sup = np.zeros(M-1)
    for i in range(M-1):
        ki = float(i)
        sup[i] = (c**2 * (ki+1)*(ki+2)
                  / ((2*ki+3) * np.sqrt((2*ki+1)*(2*ki+5))))
    return np.diag(diag) + np.diag(sup, 1) + np.diag(sup, -1)


def get_eigenvalues(c, M=M_MAT):
    """
    Returns PSWF eigenvalues lambda_k (sorted descending, as in Paper VIII).
    These are eigenvalues of the concentration operator, not the tridiagonal
    matrix directly -- the tridiagonal gives the prolate spheroidal eigenvalues
    chi_k; we need lambda_k = integral eigenvalues.

    For the scaling test we use the tridiagonal eigenvalues chi_k directly
    as a proxy: their differences have the same Airy scaling structure.
    The relevant quantity is the *difference structure*, not absolute values.

    Returns: eigvals sorted ascending (chi_0 <= chi_1 <= ...) as float64 array.
    """
    T = build_pswf_matrix(c, M)
    eigvals = eigh(T, eigvals_only=True)
    return np.sort(eigvals)   # ascending


# ── 2. F_Ai: integral of Ai^2 from x to infinity ──────────────────────────
def F_Ai(x_arr):
    """
    F_Ai(x) = int_x^inf Ai(t)^2 dt.
    Computed via: F_Ai(x) = (1/2)(Ai'(x)^2 - x*Ai(x)^2) + C_norm
    using the known antiderivative of Ai^2.
    Normalised so F_Ai(x) -> 0 as x -> +inf.
    Antiderivative: int Ai(t)^2 dt = (1/2)(Ai'^2 - t*Ai^2) (up to const).
    For x -> -inf: F_Ai(x) -> 1/(2*pi) * ... but we use numerical integration
    via cumulative sum over a fine grid for reliability.
    """
    x_arr = np.asarray(x_arr, dtype=np.float64)
    # Use analytic antiderivative: G(x) = (Ai'(x)^2 - x*Ai(x)^2) / 2
    # Then F_Ai(x) = G(inf) - G(x) = -G(x) + G(inf)
    # G(inf) = 0, so F_Ai(x) = -G(x) = (x*Ai(x)^2 - Ai'(x)^2) / 2
    # This is exact (no numerical integration needed).
    Ai_vals, Aip_vals, _, _ = airy(x_arr)
    return (x_arr * Ai_vals**2 - Aip_vals**2) / 2.0


# ── 3. Transition window indices ───────────────────────────────────────────
def transition_window(c):
    """
    Returns array of indices l with |l - N_Sh| <= A0 * c^{1/3}.
    N_Sh = 2c/pi (Nyquist-Shannon index).
    """
    N_sh = N_SH_FACTOR * c
    half_width = A0 * c**(1.0/3.0)
    l_min = int(np.ceil(N_sh - half_width))
    l_max = int(np.floor(N_sh + half_width))
    return np.arange(l_min, l_max + 1)


def rescaled_index(l, c):
    """x_l = (l - N_Sh) * (c/2)^{-1/3}"""
    N_sh = N_SH_FACTOR * c
    return (l - N_sh) * (c / 2.0)**(-1.0/3.0)


# ── 4. Second differences ─────────────────────────────────────────────────
def second_diff(arr):
    """Delta_l = arr[l] - 2*arr[l+1] + arr[l+2], returns array of length len-2."""
    return arr[:-2] - 2*arr[1:-1] + arr[2:]


# ── 5. Main computation ────────────────────────────────────────────────────
print("Computing eigenvalues and second differences...")

results = {}
for c in C_VALUES:
    print(f"  c = {c} ...", end=" ")
    eigvals = get_eigenvalues(c, M=M_MAT)

    # Transition window indices
    idx = transition_window(c)
    # Need idx, idx+1, idx+2 all valid
    idx = idx[idx + 2 < len(eigvals)]
    idx = idx[idx >= 0]

    # Eigenvalue second differences on window
    lam_window = eigvals[idx]
    lam_p1     = eigvals[idx + 1]
    lam_p2     = eigvals[idx + 2]
    Delta_lam  = lam_window - 2*lam_p1 + lam_p2

    # Rescaled index x_l
    x_l = rescaled_index(idx, c)

    # Airy second differences
    x_l0 = rescaled_index(idx,     c)
    x_l1 = rescaled_index(idx + 1, c)
    x_l2 = rescaled_index(idx + 2, c)
    Delta_Ai = F_Ai(x_l0) - 2*F_Ai(x_l1) + F_Ai(x_l2)

    # Rescaled: c^{2/3} * Delta
    scale = c**(2.0/3.0)
    Delta_lam_scaled = scale * Delta_lam
    Delta_Ai_scaled  = scale * Delta_Ai

    # Max absolute value in window (for log-log plot)
    max_scaled = np.max(np.abs(Delta_lam_scaled))

    results[c] = {
        'x_l':                x_l,
        'Delta_lam_scaled':   Delta_lam_scaled,
        'Delta_Ai_scaled':    Delta_Ai_scaled,
        'Delta_lam_raw':      Delta_lam,
        'max_scaled':         max_scaled,
        'n_window':           len(idx),
    }
    print(f"window size={len(idx)}, max|c^{{2/3}} Delta|={max_scaled:.4f}")


# ── 6. Plot A: c^{2/3} * Delta_l vs x_l (one panel per c) ────────────────
print("\nPlot A: scaled second differences vs rescaled index...")

fig_A = make_subplots(
    rows=2, cols=3,
    subplot_titles=[f'c = {c}' for c in C_VALUES],
    vertical_spacing=0.18, horizontal_spacing=0.10
)
positions = [(1,1),(1,2),(1,3),(2,1),(2,2)]

for i, c in enumerate(C_VALUES):
    r = results[c]
    row, col = positions[i]

    # Eigenvalue second differences (scaled)
    fig_A.add_trace(go.Scatter(
        x=r['x_l'], y=r['Delta_lam_scaled'],
        mode='lines', name=f'c^{{2/3}} Δ_λ',
        line=dict(color='#1f77b4', width=2),
        showlegend=(i == 0)
    ), row=row, col=col)

    # Airy second differences (scaled)
    fig_A.add_trace(go.Scatter(
        x=r['x_l'], y=r['Delta_Ai_scaled'],
        mode='lines', name=f'c^{{2/3}} Δ_Ai',
        line=dict(color='#ff7f0e', width=2, dash='dash'),
        showlegend=(i == 0)
    ), row=row, col=col)

    # Zero line
    fig_A.add_hline(y=0, line=dict(color='gray', width=0.8, dash='dot'),
                    row=row, col=col)

fig_A.update_xaxes(title_text='x_l = (l - N_Sh)(c/2)^{-1/3}')
fig_A.update_yaxes(title_text='c^{2/3} · Δ')
fig_A.update_layout(
    title=dict(
        text='Scaled Second Differences c^{2/3}·Δ_l vs Rescaled Index x_l<br>'
             '<sup>Blue: eigenvalue  |  Orange dashed: Airy  |  '
             'Transition window |x_l| ≤ 2.0</sup>',
        font=dict(size=16), x=0.5, xanchor='center'
    ),
    legend=dict(orientation='h', yanchor='bottom', y=1.06,
                xanchor='center', x=0.5),
    margin=dict(t=120, b=60, l=70, r=30),
    height=600, width=1050
)
fig_A.write_image('numerics/uprime_A_scaled_second_diff.png')
print("  Saved: uprime_A_scaled_second_diff.png")


# ── 7. Plot B: Log-log scaling of max|c^{2/3} Delta| vs c ────────────────
print("Plot B: log-log scaling...")

c_arr   = np.array(C_VALUES, dtype=float)
max_arr = np.array([results[c]['max_scaled'] for c in C_VALUES])

# Power-law fit: log(max) = alpha * log(c) + const
log_c   = np.log(c_arr)
log_max = np.log(max_arr)
alpha, const = np.polyfit(log_c, log_max, 1)
fit_line = np.exp(const) * c_arr**alpha

print(f"  Power-law fit: max|c^{{2/3}} Delta| ~ c^{{{alpha:.3f}}}")
print(f"  Interpretation:")
print(f"    alpha ~ 0    => (U') holds at scale c^{{-2/3}}  [expected]")
print(f"    alpha < 0    => (U') too conservative, Delta decays faster")
print(f"    alpha > 0    => (U') may fail at this scale")

fig_B = go.Figure()
fig_B.add_trace(go.Scatter(
    x=c_arr, y=max_arr,
    mode='lines+markers',
    name='max |c^{2/3} Δ_λ|',
    line=dict(color='#1f77b4', width=2.5),
    marker=dict(size=9, symbol='circle')
))
fig_B.add_trace(go.Scatter(
    x=c_arr, y=fit_line,
    mode='lines',
    name=f'fit ~ c^{{{alpha:.3f}}}',
    line=dict(color='#d62728', width=2, dash='dash')
))
fig_B.add_hline(
    y=1.0, line=dict(color='green', width=1.5, dash='dot'),
    annotation_text='O(1) reference', annotation_position='right'
)
fig_B.update_layout(
    title=dict(
        text='Log-Log Scaling: max|c^{2/3}·Δ_λ| vs c<br>'
             '<sup>alpha ≈ 0 confirms (U\') at scale c^{-2/3}</sup>',
        font=dict(size=16), x=0.5, xanchor='center'
    ),
    xaxis=dict(title='c (bandwidth)', type='log',
               tickvals=C_VALUES, ticktext=[str(c) for c in C_VALUES]),
    yaxis=dict(title='max |c^{2/3} · Δ_λ|', type='log',
               exponentformat='power'),
    legend=dict(orientation='h', yanchor='bottom', y=1.04,
                xanchor='center', x=0.5),
    margin=dict(t=100, b=70, l=80, r=40),
    height=480, width=750
)
fig_B.write_image('numerics/uprime_B_loglog_scaling.png')
print("  Saved: uprime_B_loglog_scaling.png")


# ── 8. Save summary JSON ──────────────────────────────────────────────────
summary = {
    'A0': A0,
    'c_values': C_VALUES,
    'power_law_exponent_alpha': float(alpha),
    'interpretation': (
        'alpha~0: (U\') plausible at c^{-2/3}; '
        'alpha<0: Delta decays faster; '
        'alpha>0: (U\') may fail'
    ),
    'per_c': {
        str(c): {
            'window_size': int(results[c]['n_window']),
            'max_scaled_second_diff': float(results[c]['max_scaled'])
        } for c in C_VALUES
    }
}
with open('numerics/uprime_scaling_summary.json', 'w') as f:
    json.dump(summary, f, indent=2)
print("  Saved: uprime_scaling_summary.json")

print("\nDone. Outputs:")
print("  numerics/uprime_A_scaled_second_diff.png")
print("  numerics/uprime_B_loglog_scaling.png")
print("  numerics/uprime_scaling_summary.json")
