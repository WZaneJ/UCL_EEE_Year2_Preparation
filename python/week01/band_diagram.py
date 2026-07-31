# band_diagram.py
# 半导体能带结构可视化

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Intrinsic semiconductor - flat bands
# ============================================================
Eg = 1.12  # Silicon band gap (eV)

# Create x-axis (position)
x_intrinsic = np.linspace(0, 5, 100)

# Band energies
EV_intrinsic = np.zeros_like(x_intrinsic)  # Valence band maximum
EC_intrinsic = np.ones_like(x_intrinsic) * Eg  # Conduction band minimum

# ============================================================
# PN junction - band bending
# ============================================================
x_pn = np.linspace(0, 10, 200)
depletion_center = 5
width = 1.5

# Band bending (Gaussian function to simulate)
bending = 0.3 * np.exp(-((x_pn - depletion_center) / width)**2)

# PN junction valence and conduction bands
EV_pn = -bending
EC_pn = Eg - bending

# ============================================================
# Plotting
# ============================================================
plt.figure(figsize=(10, 5))

# Intrinsic semiconductor
plt.subplot(1, 2, 1)
plt.plot(x_intrinsic, EC_intrinsic, 'b-', linewidth=2, label='Conduction Band')
plt.plot(x_intrinsic, EV_intrinsic, 'b-', linewidth=2, label='Valence Band')
plt.axhline(Eg/2, color='r', linestyle='--', label='Fermi Level')
plt.title('Intrinsic Semiconductor - Flat Bands')
plt.xlabel('Position')
plt.ylabel('Energy (eV)')
plt.ylim(-0.5, Eg + 0.5)
plt.legend()
plt.grid(True, alpha=0.3)

# PN junction
plt.subplot(1, 2, 2)
plt.plot(x_pn, EC_pn, 'g-', linewidth=2, label='Conduction Band')
plt.plot(x_pn, EV_pn, 'g-', linewidth=2, label='Valence Band')
plt.axhline(Eg/2, color='r', linestyle='--', label='Fermi Level')
plt.title('PN Junction - Band Bending')
plt.xlabel('Position')
plt.ylim(-0.5, Eg + 0.5)
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('band_diagram.png', dpi=150)
plt.show()

# Print interpretation
print("=== Band Diagram Interpretation ===")
print(f"Silicon band gap: {Eg} eV")
print("Intrinsic semiconductor: Flat valence and conduction bands")
print("PN junction: Band bending in depletion region")
print("Electrons: move downhill in energy")
print("Holes: move uphill in energy")