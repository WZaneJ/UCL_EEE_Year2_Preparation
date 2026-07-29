# ============================================================
# Week 1 Day 3 - Dynamic systems and circuit ODEs
# ------------------------------------------------------------
# Simulates:
#   Part 1: RC step response (charging + discharging)
#   Part 2: Series RLC step response, three damping regimes
#           (over-damped / critically damped / under-damped),
#           plus one extra low-resistance demo case that makes
#           the under-damped ringing clearly visible.
#
# The analytical formulas from the lesson are cross-checked against
# a numerical ODE solution (scipy.integrate.solve_ivp).
#
# Lesson formulas used:
#   RC charging:    v_C(t) = V0 * (1 - exp(-t/tau)),  tau = R*C
#                   i(t)   = (V0/R) * exp(-t/tau)
#   RC discharging: v_C(t) = V0 * exp(-t/tau)
#   Series RLC:     L*C*v_C'' + R*C*v_C' + v_C = V0
#                   alpha  = R/(2L)
#                   omega0 = 1/sqrt(L*C)
#                   zeta   = alpha/omega0  (zeta < 1 -> rings at omega_d,
#                                           damped by exp(-alpha*t))
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ============================================================
# Part 1: RC circuit (same numbers as exercise P1)
# ODE: R*C * dv_C/dt + v_C = V0,  v_C(0) = 0
# ============================================================

V0 = 5.0                 # V, step amplitude
R_rc = 10e3              # ohm
C_rc = 100e-6            # F
tau_rc = R_rc * C_rc     # time constant, s

t1 = np.linspace(0.0, 5.0 * tau_rc, 1000)
v_charge = V0 * (1.0 - np.exp(-t1 / tau_rc))
v_discharge = V0 * np.exp(-t1 / tau_rc)      # capacitor initially at V0, source removed
i_charge = (V0 / R_rc) * np.exp(-t1 / tau_rc)

print("=== RC circuit ===")
print(f"tau = R*C           = {tau_rc:.3f} s")
print(f"v_C(tau)            = {V0 * (1.0 - np.exp(-1.0)):.3f} V  = 63.2% of V0")
print(f"v_C(5*tau)          = {V0 * (1.0 - np.exp(-5.0)):.4f} V  -> settled (>99%)")
print(f"i(0+)               = {V0 / R_rc:.3e} A  (current jumps; v_C stays continuous)")

# Numerical cross-check of the RC ODE with solve_ivp
def rc_ode(t, y):
    # y[0] = v_C; from the ODE: dv_C/dt = (V0 - v_C) / (R*C)
    return [(V0 - y[0]) / (R_rc * C_rc)]

sol_rc = solve_ivp(rc_ode, (t1[0], t1[-1]), [0.0], t_eval=t1, rtol=1e-9, atol=1e-12)
err_rc = np.max(np.abs(sol_rc.y[0] - v_charge))
print(f"max |analytic - numeric| = {err_rc:.2e} V  (formula verified)")

# ============================================================
# Part 2: Series RLC circuit (L, C from exercise P4)
# ============================================================

V0_2 = 5.0               # V, step amplitude
L = 10e-3                # H
C2 = 100e-6              # F
omega0 = 1.0 / np.sqrt(L * C2)

t2 = np.linspace(0.0, 0.03, 2000)    # 30 ms covers all cases


def rlc_step_response(t, R):
    """Analytical step response v_C(t), with v_C(0)=0, i(0)=0."""
    alpha = R / (2.0 * L)
    zeta = alpha / omega0
    if zeta < 1.0 - 1e-9:
        w_d = np.sqrt(omega0 ** 2 - alpha ** 2)
        v = V0_2 * (1.0 - np.exp(-alpha * t) *
                    (np.cos(w_d * t) + (alpha / w_d) * np.sin(w_d * t)))
        info = f"under-damped, omega_d = {w_d:.1f} rad/s"
    elif abs(zeta - 1.0) <= 1e-9:
        w_d = 0.0
        v = V0_2 * (1.0 - np.exp(-alpha * t) * (1.0 + alpha * t))
        info = "critically damped"
    else:
        w_d = 0.0
        s1 = -alpha + np.sqrt(alpha ** 2 - omega0 ** 2)   # slow pole
        s2 = -alpha - np.sqrt(alpha ** 2 - omega0 ** 2)   # fast pole
        A = -V0_2 * s2 / (s2 - s1)
        B = V0_2 * s1 / (s2 - s1)
        v = V0_2 + A * np.exp(s1 * t) + B * np.exp(s2 * t)
        info = f"over-damped, poles = {s1:.1f}, {s2:.1f} s^-1"
    return v, alpha, zeta, w_d, info


def rlc_ode(t, y, R):
    # y[0] = v_C, y[1] = i
    # dv_C/dt = i/C ;  di/dt = (V0 - v_C - R*i)/L   (from KVL)
    return [y[1] / C2, (V0_2 - y[0] - R * y[1]) / L]


def check_case(t, R, tag):
    v, alpha, zeta, w_d, info = rlc_step_response(t, R)
    overshoot = (np.max(v) / V0_2 - 1.0) * 100.0
    sol = solve_ivp(rlc_ode, (t[0], t[-1]), [0.0, 0.0],
                    args=(R,), t_eval=t, rtol=1e-9, atol=1e-12)
    err = np.max(np.abs(sol.y[0] - v))
    print(f"{tag} R = {R:5.1f} ohm: alpha = {alpha:7.1f} s^-1, zeta = {zeta:4.2f} | "
          f"{info} | overshoot = {overshoot:5.2f}% | num. err = {err:.2e} V")
    return v, alpha, zeta, w_d, info


print(f"\n=== Series RLC: L = {L * 1e3:.0f} mH, C = {C2 * 1e6:.0f} uF, "
      f"omega0 = {omega0:.1f} rad/s ===")

# the three exercise-P4 cases
v_u, a_u, z_u, wd_u, _ = check_case(t2, 16.0, "[P4]")
v_c, a_c, z_c, wd_c, _ = check_case(t2, 20.0, "[P4]")
v_o, a_o, z_o, wd_o, _ = check_case(t2, 40.0, "[P4]")

# extra demo case: small R -> light damping -> visible ringing
# (Day-1 oscillation multiplied by the Q1 exponential envelope)
v_d, a_d, z_d, wd_d, _ = check_case(t2, 4.0, "[demo]")
T_d = 2.0 * np.pi / wd_d
print(f"[demo] ringing period T_d = 2*pi/omega_d = {1e3 * T_d:.2f} ms "
      f"(peaks of the step response sit at n*pi/omega_d)")

# ============================================================
# Part 3: Plots
# ============================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.5, 4.8))

# --- Panel 1: RC ---
l1, = ax1.plot(t1, v_charge, color="tab:blue", label=r"$v_C$ charging")
l2, = ax1.plot(t1, v_discharge, "--", color="tab:orange", label=r"$v_C$ discharging")
ax1.axvline(tau_rc, color="grey", lw=0.8, alpha=0.6)
ax1.axhline(V0 * (1.0 - np.exp(-1.0)), color="grey", lw=0.8, alpha=0.6)
ax1.annotate(r"$t = \tau$: 63.2%", xy=(tau_rc, V0 * 0.632), xytext=(1.35 * tau_rc, 0.45 * V0),
             arrowprops=dict(arrowstyle="->", color="grey"))
ax1b = ax1.twinx()
l3, = ax1b.plot(1e3 * 0 + t1, 1e3 * i_charge, ":", color="tab:green",
                label=r"$i$ (right axis, jumps at $t=0$)")
ax1b.set_ylabel(r"$i$ (mA)", color="tab:green")
ax1b.tick_params(axis="y", labelcolor="tab:green")
ax1.legend(handles=[l1, l2, l3], loc="center right", fontsize=8)
ax1.set_xlabel("t (s)")
ax1.set_ylabel(r"$v_C$ (V)")
ax1.set_title(r"RC step response, $\tau = RC = 1$ s")
ax1.grid(alpha=0.3)

# --- Panel 2: RLC ---
ms = 1e3 * t2    # time axis in ms
ax2.plot(ms, v_u, color="tab:purple", label=rf"$\zeta = {z_u:.1f}$ (P4 under)")
ax2.plot(ms, v_c, color="tab:green", label=rf"$\zeta = {z_c:.1f}$ (critical)")
ax2.plot(ms, v_o, color="tab:blue", label=rf"$\zeta = {z_o:.1f}$ (P4 over)")
ax2.plot(ms, v_d, color="tab:red", lw=1.6,
         label=rf"$\zeta = {z_d:.1f}$ (demo: ringing visible)")
env = V0_2 * np.exp(-a_d * t2)
ax2.plot(ms, V0_2 + env, "--", color="tab:red", lw=0.9, alpha=0.45)
ax2.plot(ms, V0_2 - env, "--", color="tab:red", lw=0.9, alpha=0.45,
         label=r"envelope $V_0 \pm V_0 e^{-\alpha t}$")
ax2.axhline(V0_2, color="grey", lw=0.8, ls=":")
# mark one ringing period of the demo curve (peaks at t = n*pi/omega_d)
t_p1 = 1e3 * np.pi / wd_d
t_p2 = 1e3 * 2.0 * np.pi / wd_d
ax2.annotate("", xy=(t_p2, 8.3), xytext=(t_p1, 8.3),
             arrowprops=dict(arrowstyle="<->", color="tab:red"))
ax2.text(0.5 * (t_p1 + t_p2) - 2.6, 8.7, rf"$T_d \approx {1e3 * T_d:.1f}$ ms, "
         rf"$\omega_d \approx {wd_d:.0f}$ rad/s", color="tab:red")
ax2.set_xlabel("t (ms)")
ax2.set_ylabel(r"$v_C$ (V)")
ax2.set_ylim(0.0, 10.4)
ax2.set_title(r"Series RLC step response, $\omega_0 = 1000$ rad/s")
ax2.legend(loc="center right", fontsize=8)
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("circuit_ode_sim.png", dpi=150)
plt.show()

# ============================================================
# Part 4: Take-home interpretation
# ============================================================
print("\n=== Interpretation ===")
print("1. tau sets the whole timescale of a first-order circuit: 63% at tau, >99% at 5*tau.")
print("2. v_C is continuous (0 at t=0+) while i jumps to V0/R: 'no jump' = continuity,")
print("   the derivative may still jump.")
print("3. Same ODE shape in RC and RL: only tau changes (R*C vs L/R).")
print("4. zeta decides the RLC regime. zeta = 0.8 (P4) already rings only ~1.5%,")
print("   so it looks almost like critical; the zeta = 0.2 demo shows what real")
print("   ringing looks like: oscillation at omega_d < omega0 inside the envelope")
print("   exp(-alpha*t)  (Day-1 oscillation x Q1 exponential decay).")
print("5. solve_ivp reproduces the analytical formulas to ~1e-9 V: the ODE model and")
print("   the closed-form solution agree, so both can be trusted.")
