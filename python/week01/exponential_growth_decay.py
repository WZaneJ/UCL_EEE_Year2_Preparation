"""
Compare exponentially growing and decaying solutions.

Both functions are associated with the differential equation

    y'' - alpha**2 * y = 0.

The general solution is

    y(x) = A * exp(alpha * x) + B * exp(-alpha * x).

If the solution must remain finite as x tends to positive infinity,
the coefficient A must be zero.
"""

import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------
# 1. Define the spatial domain and parameter
# --------------------------------------------------

x = np.linspace(0.0, 3.0, 1000)

alpha = 1.2


# --------------------------------------------------
# 2. Calculate the growing and decaying solutions
# --------------------------------------------------

growing_solution = np.exp(alpha * x)
decaying_solution = np.exp(-alpha * x)


# --------------------------------------------------
# 3. Plot the two functions
# --------------------------------------------------

plt.figure(figsize=(10.0, 6.0))

plt.plot(
    x,
    growing_solution,
    color="tab:red",
    linewidth=2.0,
    label=r"$e^{+\alpha x}$",
)

plt.plot(
    x,
    decaying_solution,
    color="tab:blue",
    linewidth=2.0,
    label=r"$e^{-\alpha x}$",
)

plt.xlabel("Position x")
plt.ylabel("y(x)")

plt.title(
    "Exponentially growing and decaying solutions"
)

plt.xlim(0.0, 3.0)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 4. Print representative numerical values
# --------------------------------------------------

print("Comparison of exponential solutions")
print("-----------------------------------")
print(f"alpha = {alpha:.2f}")
print()

sample_positions = [0.0, 1.0, 2.0, 3.0]

for position in sample_positions:
    growing_value = np.exp(alpha * position)
    decaying_value = np.exp(-alpha * position)

    print(
        f"x = {position:.1f}: "
        f"exp(+alpha * x) = {growing_value:10.4f}, "
        f"exp(-alpha * x) = {decaying_value:10.4f}"
    )


# --------------------------------------------------
# 5. Print the physical interpretation
# --------------------------------------------------

print()
print("Boundary-condition interpretation")
print("---------------------------------")

print(
    "As x increases, exp(+alpha * x) grows without bound."
)

print(
    "As x increases, exp(-alpha * x) approaches zero."
)

print(
    "If a physical solution must remain finite as x tends "
    "to positive infinity, the coefficient multiplying "
    "exp(+alpha * x) must be zero."
)