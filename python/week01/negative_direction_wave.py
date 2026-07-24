"""
Visualise a sinusoidal wave travelling in the negative x-direction.

The wave is

    u(x, t) = cos(omega * t + beta * x)

For a point of constant phase,

    omega * t + beta * x = constant,

so the point moves in the negative x-direction with velocity

    dx/dt = -omega / beta.
"""

import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------
# 1. Define the spatial domain and wave parameters
# --------------------------------------------------

x = np.linspace(-10.0, 10.0, 1000)

amplitude = 1.0
omega = 2.0       # Angular frequency in rad/s
beta = 1.0        # Phase constant in rad/unit length
phase = 0.0       # Initial phase in rad

times = [0.0, 0.5, 1.0, 1.5]


# --------------------------------------------------
# 2. Calculate the wave parameters
# --------------------------------------------------

phase_speed = omega / beta
signed_phase_velocity = -phase_speed

wavelength = (2.0 * np.pi) / beta
frequency = omega / (2.0 * np.pi)


# --------------------------------------------------
# 3. Plot the wave at different times
# --------------------------------------------------

plt.figure(figsize=(10.0, 6.0))

for t in times:
    wave = amplitude * np.cos(
        omega * t + beta * x + phase
    )

    plt.plot(
        x,
        wave,
        linewidth=2.0,
        label=f"t = {t:.1f} s",
    )

plt.xlabel("Position x")
plt.ylabel("Wave amplitude u(x, t)")

plt.title(
    r"Wave travelling in the $-x$ direction: "
    r"$u(x,t)=A\cos(\omega t+\beta x+\phi)$"
)

plt.xlim(-10.0, 10.0)
plt.ylim(-1.2 * amplitude, 1.2 * amplitude)

plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 4. Print the wave parameters
# --------------------------------------------------

print("Wave travelling in the negative x-direction")
print("------------------------------------------------")
print(f"Amplitude                  = {amplitude:.2f}")
print(f"Angular frequency, omega   = {omega:.2f} rad/s")
print(f"Phase constant, beta       = {beta:.2f} rad/unit length")
print(f"Initial phase              = {phase:.2f} rad")
print(f"Phase speed                = {phase_speed:.4f} units/s")
print(f"Signed phase velocity      = {signed_phase_velocity:.4f} units/s")
print(f"Wavelength                 = {wavelength:.4f} units")
print(f"Frequency                  = {frequency:.4f} Hz")
print()

print("Predicted displacement of a constant-phase point")
print("--------------------------------------------------")

for t in times:
    predicted_displacement = signed_phase_velocity * t

    print(
        f"t = {t:.1f} s, "
        f"displacement = {predicted_displacement:.2f} units"
    )