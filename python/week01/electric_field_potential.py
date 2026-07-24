"""
electric_field_potential.py
Week 1 Day 2 — Electric field and potential visualisation.

Plots three 1D examples to build intuition for E_x = -dV/dx:
  1. Point charge: V(r) and |E(r)| on a line avoiding r=0.
  2. Linear potential V(x) = 5*x**2 - 3*x + 2 (same as Practice P2):
     shows E pointing down the V-hill.
  3. Parallel-plate capacitor (uniform E region + fringe-free model):
     V(x) is linear inside the gap, so E is constant and points -x.

Every example prints a short physical interpretation.
"""

import numpy as np
import matplotlib.pyplot as plt

# Use a clean style
plt.rcParams.update({
    "figure.figsize": (10, 8),
    "axes.grid": True,
    "grid.alpha": 0.3,
    "font.size": 11,
})

# Physical constant used in Example 1
k_coulomb = 9.0e9   # 1/(4 pi epsilon_0), N*m^2/C^2


def example1_point_charge(ax_v, ax_e):
    """V(r) and E(r) for a +1 muC point charge along a radial line."""
    Q = 1.0e-6  # 1 microcoulomb
    r = np.linspace(0.05, 0.5, 400)  # avoid r=0 singularity
    V = k_coulomb * Q / r            # volts, V(infty)=0
    E = k_coulomb * Q / r ** 2       # V/m, radial outward

    ax_v.plot(r, V / 1000.0, color="tab:blue", lw=2)
    ax_v.set_title("Example 1: Point charge $Q=+1\\,\\mu$C  —  Potential")
    ax_v.set_xlabel("r  (m)")
    ax_v.set_ylabel("V  (kV)")
    ax_v.axhline(0, color="k", lw=0.6)

    ax_e.plot(r, E / 1000.0, color="tab:red", lw=2)
    ax_e.set_title("Example 1: Point charge  —  Electric field |E|")
    ax_e.set_xlabel("r  (m)")
    ax_e.set_ylabel("|E|  (kV/m)")
    ax_e.axhline(0, color="k", lw=0.6)

    # Numerical checks at r = 0.1 m
    r_check = 0.1
    V_check = k_coulomb * Q / r_check
    E_check = k_coulomb * Q / r_check ** 2
    print("=== Example 1: point charge ===")
    print(f"At r = {r_check} m:  V = {V_check:.3e} V  ({V_check/1000:.1f} kV)")
    print(f"At r = {r_check} m:  E = {E_check:.3e} V/m  ({E_check/1000:.0f} kV/m)")
    print("V falls as 1/r, E falls as 1/r^2.  Close to the charge both diverge.")
    print()


def example2_quadratic_potential(ax_v, ax_e):
    """V(x) = 5 x^2 - 3 x + 2, E_x = -dV/dx = -10 x + 3 (Practice P2)."""
    x = np.linspace(-1.0, 2.0, 600)
    V = 5.0 * x ** 2 - 3.0 * x + 2.0
    E_x = -10.0 * x + 3.0

    # Find minimum of V (where E_x = 0 -> x = 0.3)
    x_min = 0.3
    V_min = 5.0 * x_min ** 2 - 3.0 * x_min + 2.0

    ax_v.plot(x, V, color="tab:blue", lw=2, label="V(x)")
    ax_v.axvline(x_min, color="gray", ls="--", lw=1,
                 label=f"minimum at x = {x_min} m, E=0")
    ax_v.axvline(1.0, color="tab:orange", ls=":", lw=1.2,
                label="x = 1 m (Practice P2 point)")
    ax_v.set_title("Example 2: $V(x)=5x^2-3x+2$  —  quadratic well")
    ax_v.set_xlabel("x  (m)")
    ax_v.set_ylabel("V  (V)")
    ax_v.legend(loc="upper right", fontsize=9)

    ax_e.plot(x, E_x, color="tab:red", lw=2, label="$E_x(x) = -10x+3$")
    ax_e.axhline(0, color="k", lw=0.6)
    ax_e.axvline(x_min, color="gray", ls="--", lw=1, label="E=0 at x = 0.3 m")
    ax_e.axvline(1.0, color="tab:orange", ls=":", lw=1.2, label="x = 1 m")
    ax_e.set_title("Example 2: Electric field  —  minus slope of V")
    ax_e.set_xlabel("x  (m)")
    ax_e.set_ylabel("$E_x$  (V/m)")
    ax_e.legend(loc="upper right", fontsize=9)

    print("=== Example 2: quadratic potential (Practice P2) ===")
    print(f"V(x) is a parabola with minimum at x = {x_min} m, V_min = {V_min:.2f} V")
    print(f"At x = 1 m: V = {5-3+2} V,  E_x = {-10+3} V/m (points -x, i.e. 'downhill')")
    print("Key intuition: E points from HIGH V to LOW V (down the slope of V).")
    print("Where V is flat (dV/dx=0), E = 0.  That is the 'bottom of the hill'.")
    print()


def example3_parallel_plate(ax_v, ax_e):
    """Ideal parallel-plate capacitor (no fringing): V(x) linear, E uniform."""
    d = 0.02  # 2 cm gap
    V0 = 100.0  # 100 V across plates
    x = np.linspace(0.0, d, 300)

    # V(x): 0 at x=0 (negative plate), V0 at x=d (positive plate)
    V = (V0 / d) * x
    # E points from + plate to - plate, i.e. in -x direction here, magnitude V0/d
    E_x = -V0 / d * np.ones_like(x)
    E_mag = V0 / d

    x_cm = x * 100.0  # convert to cm for display
    ax_v.plot(x_cm, V, color="tab:blue", lw=2)
    ax_v.axhline(0, color="k", lw=0.6)
    ax_v.set_title("Example 3: Parallel-plate capacitor  —  V across gap")
    ax_v.set_xlabel("x  (cm)   [0 = negative plate, 2 cm = positive plate]")
    ax_v.set_ylabel("V  (V)")

    ax_e.plot(x_cm, E_x, color="tab:red", lw=2,
              label=f"$E_x$ = {E_x[0]:.0f} V/m (constant)")
    ax_e.axhline(0, color="k", lw=0.6)
    ax_e.set_title("Example 3: Parallel-plate capacitor  —  uniform E")
    ax_e.set_xlabel("x  (cm)")
    ax_e.set_ylabel("$E_x$  (V/m)")
    ax_e.legend(loc="upper right", fontsize=9)
    ax_e.set_ylim(E_x[0] * 1.5, -E_x[0] * 0.2)

    print("=== Example 3: parallel-plate capacitor ===")
    print(f"Gap d = {d*100:.1f} cm, voltage V0 = {V0:.0f} V")
    print(f"Uniform field |E| = V0/d = {E_mag:.0f} V/m, pointing from + plate to - plate")
    print("Inside an ideal capacitor V varies LINEARLY  =>  dV/dx = constant  =>  E is uniform.")
    print("In a conductor at equilibrium E = 0, so V must be constant (the flat plateau on either side).")
    print()


def main():
    fig, axes = plt.subplots(3, 2, figsize=(11, 11))

    example1_point_charge(axes[0, 0], axes[0, 1])
    example2_quadratic_potential(axes[1, 0], axes[1, 1])
    example3_parallel_plate(axes[2, 0], axes[2, 1])

    fig.suptitle("Week 1 Day 2  —  Electric potential V and electric field E  |  E = -dV/dx",
                 fontsize=13, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.97])

    out_path = "python/week01/electric_field_potential.png"
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    print(f"Saved figure to: {out_path}")
    plt.show()


if __name__ == "__main__":
    main()
