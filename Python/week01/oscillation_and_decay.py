"""
Compare an oscillatory solution and an exponentially decaying solution.

The oscillatory function

    y_1(x) = cos(beta * x)

satisfies

    y_1'' + beta**2 * y_1 = 0.

The decaying function

    y_2(x) = exp(-alpha * x)

satisfies

    y_2'' - alpha**2 * y_2 = 0.
"""

import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------
# 1. Define the spatial domain and parameters
# --------------------------------------------------

x = np.linspace(0.0, 5.0, 1000)

beta = 3.0
alpha = 1.2


# --------------------------------------------------
# 2. Calculate the two functions
# --------------------------------------------------

oscillatory_solution = np.cos(beta * x)
decaying_solution = np.exp(-alpha * x)


# --------------------------------------------------
# 3. Create the figure
# --------------------------------------------------

figure, axes = plt.subplots(
    nrows=1,
    ncols=2,
    figsize=(12.0, 4.5),
)


# --------------------------------------------------
# 4. Plot the oscillatory solution
# --------------------------------------------------

axes[0].plot(
    x,
    oscillatory_solution,
    color="tab:blue",
    linewidth=2.0,
)

axes[0].set_title(
    r"Oscillatory solution: $y(x)=\cos(\beta x)$"
)

axes[0].set_xlabel("Position x")
axes[0].set_ylabel("y(x)")

axes[0].set_xlim(0.0, 5.0)
axes[0].set_ylim(-1.2, 1.2)

axes[0].grid(True)


# --------------------------------------------------
# 5. Plot the decaying solution
# --------------------------------------------------

axes[1].plot(
    x,
    decaying_solution,
    color="tab:red",
    linewidth=2.0,
)

axes[1].set_title(
    r"Exponentially decaying solution: "
    r"$y(x)=e^{-\alpha x}$"
)

axes[1].set_xlabel("Position x")
axes[1].set_ylabel("y(x)")

axes[1].set_xlim(0.0, 5.0)
axes[1].set_ylim(0.0, 1.1)

axes[1].grid(True)


# --------------------------------------------------
# 6. Display the figure
# --------------------------------------------------

figure.tight_layout()
plt.show()


# --------------------------------------------------
# 7. Print the mathematical interpretation
# --------------------------------------------------

print("Oscillatory solution")
print("--------------------")
print("y_1(x) = cos(beta * x)")
print(f"beta = {beta:.2f}")
print()
print("Differential equation:")
print("y_1'' + beta**2 * y_1 = 0")
print()

print("Exponentially decaying solution")
print("--------------------------------")
print("y_2(x) = exp(-alpha * x)")
print(f"alpha = {alpha:.2f}")
print()
print("Differential equation:")
print("y_2'' - alpha**2 * y_2 = 0")
print()

print("Physical interpretation")
print("-----------------------")
print(
    "The oscillatory solution changes sign repeatedly "
    "and has a spatial period."
)

print(
    "The exponentially decaying solution decreases "
    "monotonically towards zero."
)

print(
    "The term exp(-alpha * x) represents spatial attenuation, "
    "not periodic propagation."
)