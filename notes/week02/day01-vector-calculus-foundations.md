# Week 2 Day 1: Vector Calculus Foundations

- Date: 2026-08-07
- Status: complete (exit test passed; mastery estimate about 92%)
- Planned workload: B-tier, about 2.5 hours
- Actual study time: about 4 hours, including reading, reflection, external video, additional AI consultation, practice, feedback and correction
- Knowledge chain: Scalar fields -> gradient -> vector fields -> divergence and curl -> line integrals -> Maxwell equations
- Exercises: [14 - entry diagnostic](../../exercises/week02/14-vector-calculus-entry-diagnostic.md), [15 - gradient practice](../../exercises/week02/15-gradient-practice.md), [16 - directional derivative practice](../../exercises/week02/16-directional-derivative-level-curves-practice.md), [17 - divergence practice](../../exercises/week02/17-divergence-practice.md), [18 - line-integral check](../../exercises/week02/18-line-integral-circulation-check.md), [19 - exit test](../../exercises/week02/19-vector-calculus-exit-test.md)
- Simulation: deferred to Week 2 Day 2

## 1. Scope

### Completed

- Scalar fields and vector fields
- Gradient and its geometric meaning
- Electric field as the negative gradient of potential
- Unit direction vectors and directional derivatives
- Level curves and the normal direction
- Divergence as local net outflow
- Curl as local rotation tendency
- Two-dimensional divergence and curl calculations
- Line-integral and circulation intuition

### Deferred to Week 2 Day 2

- Surface integrals and flux calculations
- Divergence theorem
- Stokes' theorem
- Python vector-field visualisation
- Direct connection to Maxwell equations and Poisson's equation

The scope was reduced deliberately after a cognitive-load and time-budget check. Deferred material is not treated as a failed task.

## 2. Scalar and Vector Fields

A scalar field assigns one number to each point in space. Examples include temperature $T(x,y,z)$, electric potential $V(x,y,z)$ and charge density $\rho(x,y,z)$.

A vector field assigns a magnitude and direction to each point. In printed notation a vector may be bold; in handwritten work an arrow is used. This repository writes the components as

$$
\vec{F}(x,y,z)=(F_x,F_y,F_z)
$$

Examples include electric field $\vec{E}$, magnetic field $\vec{B}$, current density $\vec{J}$ and fluid velocity $\vec{v}$.

The input-output map of the three local operators is:

- Gradient: scalar field -> vector field
- Divergence: vector field -> scalar field
- Curl: vector field -> vector field

## 3. Gradient

For a scalar field $u(x,y,z)$,

$$
\nabla u=\left(\frac{\partial u}{\partial x},\frac{\partial u}{\partial y},\frac{\partial u}{\partial z}\right)
$$

The vector $\nabla u$ points in the direction in which $u$ increases most rapidly. Its magnitude is the maximum rate of increase per unit distance.

For electric potential,

$$
\vec{E}=-\nabla V
$$

Therefore the electric field points in the direction of the steepest decrease in potential.

## 4. Directional Derivative

A direction vector $\vec{a}$ must first be normalised:

$$
\vec{u}=\frac{\vec{a}}{|\vec{a}|}
$$

The directional derivative of $f$ along the unit vector $\vec{u}$ is

$$
D_{\vec{u}}f=\nabla f\cdot\vec{u}
$$

A positive value means that $f$ increases in the chosen direction; a negative value means that it decreases. The maximum directional derivative is $|\nabla f|$ and occurs in the gradient direction.

The specified direction and the gradient direction must not be confused. The specified direction is the direction requested by the problem; the gradient gives the direction of maximum increase.

## 5. Level Curves

A level curve is defined by

$$
f(x,y)=C
$$

Along the curve, $f$ remains constant. If $\vec{t}$ is a tangent direction, then

$$
\nabla f\cdot\vec{t}=0
$$

Therefore the gradient is perpendicular to the level curve. Since $\vec{E}=-\nabla V$, electric-field lines are perpendicular to equipotential lines.

## 6. Divergence

For $\vec{F}=(F_x,F_y,F_z)$,

$$
\nabla\cdot\vec{F}=\frac{\partial F_x}{\partial x}+\frac{\partial F_y}{\partial y}+\frac{\partial F_z}{\partial z}
$$

Divergence is a scalar that measures local net outflow:

- $\nabla\cdot\vec{F}>0$: local source or net outflow
- $\nabla\cdot\vec{F}<0$: local sink or net inflow
- $\nabla\cdot\vec{F}=0$: no local net outflow

Zero divergence does not mean that the vector field is zero and does not rule out rotation.

The electromagnetic connection is Gauss's law in differential form:

$$
\nabla\cdot\vec{E}=\frac{\rho}{\varepsilon_0}
$$

Charge density acts as a source of electric field.

## 7. Curl

Curl measures local rotation tendency. A small paddle wheel is the useful physical model: curl describes whether it tends to rotate, how strongly and about which axis.

For a two-dimensional field $\vec{F}(x,y)=(F_x,F_y,0)$,

$$
\nabla\times\vec{F}=\left(0,0,\frac{\partial F_y}{\partial x}-\frac{\partial F_x}{\partial y}\right)
$$

A positive $z$ component corresponds to counter-clockwise rotation when viewed from the positive $z$ direction. A negative $z$ component corresponds to clockwise rotation.

Divergence and curl measure independent local properties:

- Divergence asks whether the field locally spreads out or converges.
- Curl asks whether the field has a local rotation tendency.

A field may be divergent without rotating, rotating without divergence, both, or neither.

## 8. Line Integral and Circulation

For a vector field along a path $C$,

$$
\int_C\vec{F}\cdot d\vec{r}
$$

The dot product selects the component of the field tangent to the path. In mechanics, this line integral gives work.

For a closed path,

$$
\oint_C\vec{F}\cdot d\vec{r}
$$

is the circulation. Divergence concerns local net outflow, whereas circulation concerns the accumulated tangential component around a closed boundary.

The normal component of curl can be interpreted as the limiting circulation per unit area around an infinitesimal loop. The formal integral relation is deferred to Stokes' theorem on Week 2 Day 2.

## 9. Operator Relations Preview

For sufficiently smooth fields,

$$
\nabla\times(\nabla u)=\vec{0}
$$

and

$$
\nabla\cdot(\nabla\times\vec{A})=0
$$

The scalar Laplacian is

$$
\nabla^2u=\nabla\cdot(\nabla u)
$$

Statements that a curl-free field is globally a gradient, or that a divergence-free field is globally a curl, require suitable domain and topology assumptions. These conditions will be addressed later.

## 10. Exit-Test Summary

- ET1: output types correct, but the requested input types were omitted
- ET2: gradient, electric field, magnitude and direction correct
- ET3: directional derivative correct
- ET4: divergence, curl and physical classification correct
- ET5: line-integral intuition correct; divergence/circulation distinction needed fuller wording; curl-circulation relation needed the local limiting-area condition

Mastery estimate: about 92%.

## 11. Review Queue

- State both input and output types when classifying vector-calculus operators
- Keep the specified direction separate from the gradient direction
- Treat two-dimensional curl as the $z$ component of the full curl vector
- State the curl-circulation relation as a local limit per unit area
- Keep vector notation explicit in both handwritten work and archived notes

## 12. Where This Gets Reused

- Week 2 Day 2: surface flux, divergence theorem, Stokes' theorem and vector-field visualisation
- ELEC0019: Maxwell equations, Poisson equation, electromagnetic waves and waveguides
- ELEC0020: optical fields, guided waves and power flow
- ELEC0021: state-space and multidimensional system models
- Semiconductor devices: electric potential, electric field and band bending

## 13. Resource

- Bilibili: Gradient, Divergence and Curl - https://www.bilibili.com/video/BV1GEi4BQEFA/
