# Day 2 — Surface Integrals and Flux

- **Date:** 2026-08-08
- **Status:** Completed
- **Planned workload tier:** A-tier (120 min), dynamically reduced to one concept cluster at student request (fatigue, 60 min budget)
- **Actual study time:** about 55 minutes
- **Time-budget adjustment:** Scoped to surface integrals and flux only. Divergence theorem, Stokes' theorem, Python vector-field visualisation and Maxwell/Poisson connections deferred to later sessions.
- **Knowledge chain:** Vector calculus -> Maxwell equations -> PDEs -> eigenmodes/waveguides (Chain 3). Builds directly on Week 2 Day 1 (gradient, divergence, curl, line integral/circulation). Prepares the surface-integral side of the Divergence Theorem (W2D3).
- **Companion exercises:**
  - [20 — Flux entry diagnostic](../../exercises/week02/20-flux-entry-diagnostic.md)
  - [21 — Flux guided example](../../exercises/week02/21-flux-guided-example.md)
  - [22 — Flux independent practice](../../exercises/week02/22-flux-independent-practice.md)
  - [23 — Flux exit test](../../exercises/week02/23-flux-exit-test.md)
- **Simulation:** Deferred (no Python file this session per G4 and fatigue budget).

---

## Scope completed

1. Closed-book recall of Week 2 Day 1 operators (gradient, divergence, curl) plus two flux-intuition pre-diagnostic questions.
2. Three-layer definition of flux, from the uniform perpendicular case to the general surface integral.
3. Sign convention, angle interpretation ($\theta$ between field and unit normal), normal-vector choice.
4. Open vs closed surfaces and the outward-normal convention (preview for Gauss's law / Divergence Theorem).
5. One guided example, one independent-practice problem, one two-part exit test, all marked in detail.

## Scope deferred

- Divergence theorem (Gauss's theorem) — Week 2 Day 3.
- Stokes' theorem and curl–circulation in surface form.
- Python vector-field visualisation (slanting/n̂ coloring of a small patch under a tilted field).
- Direct connection to Maxwell equations and Poisson's equation.
- Computation of flux on genuinely curved surfaces (spheres, cylinders) — deferred until after the Divergence theorem provides a shortcut.

---

## 1. Concrete model

The magnetic-flux intuition the student volunteered in the diagnostic — "flux = number of field lines crossing a patch, per unit area times area" — is the model we kept.

Picture a small rectangular wire frame held in a steady shower of rain (the "field" is the rain velocity vector). The amount of water collected per second depends on:

- how hard it is raining (field strength $|\vec{F}|$);
- how big the frame is (area $A$);
- how the frame is tilted (angle $\theta$ between the field direction and the normal to the frame).

Hold the frame face-on to the rain: maximum collection. Tilt it $90°$ so rain runs along the frame: zero collection. Hold it the other way around, so the "front" faces away from the rain: same magnitude as face-on, but negative by the counting convention.

This model applies identically to:

- electric flux $\Phi_E$ (electric field lines through a patch);
- magnetic flux $\Phi_B$ (magnetic field lines through a loop, basis of Faraday's law);
- fluid volume flux (velocity field through a surface);
- any vector-field surface integral.

## 2. What is being studied

The object of study is the **flux** of a vector field $\vec{F}(x,y,z)=(F_x,F_y,F_z)$ through a surface $S$.

- **Input:** a vector field $\vec{F}$ (every point has an arrow) plus an oriented surface $S$ (every point has a chosen unit normal $\hat{n}$).
- **Output:** a single scalar $\Phi$, with units $[\vec{F}]\cdot\text{area}$.
- For the electric field $\vec{E}$ the units are $\text{V/m}\cdot\text{m}^2=\text{V·m}=\text{N·m}^2/\text{C}$ (both equivalent).
- For the magnetic field $\vec{B}$ the units are $\text{Wb}=\text{T·m}^2$.

Flux is therefore a **scalar accumulation of the normal component of a vector field over a surface**. Contrast with the line integral of Day 1 (tangential component along a curve) and the volume integral of a scalar (just add up scalars over a region).

## 3. Three-layer definition (build from simplest to general)

### Layer 1 — uniform field, perpendicular to a flat patch

$$
\Phi=|\vec{F}|A=EA.
$$

Example: uniform $\vec{E}=2~\text{V/m}$ perpendicular to a $5~\text{m}^2$ plate gives $\Phi=10~\text{V·m}$.

### Layer 2 — uniform field at an angle to a flat patch

Define the unit normal $\hat{n}$ (dimensionless, length 1, perpendicular to the surface), and define the oriented area vector $\vec{A}=\hat{n}A$ (units of area). Then

$$
\Phi=\vec{E}\cdot\vec{A}=(\vec{E}\cdot\hat{n})A=EA\cos\theta,
$$

where $\theta$ is the angle between $\vec{E}$ and $\hat{n}$.

Key cases:

| $\theta$ | $\cos\theta$ | $\Phi$ | Physical meaning |
|---|---:|---:|---|
| $0°$ | $1$ | $+EA$ | Field points straight out of the chosen front face (maximum outflow) |
| $90°$ | $0$ | $0$ | Field runs parallel to the surface; no field lines cross |
| $180°$ | $-1$ | $-EA$ | Field points straight into the chosen front face (maximum inflow) |

Only the component of $\vec{E}$ parallel to $\hat{n}$ contributes. The tangential (surface-parallel) component "slides past" and contributes zero. This is the geometric heart of flux and is the reason every flux formula has a dot product.

### Layer 3 — non-uniform field, curved surface

Chop the surface into infinitesimal patches $dA$. On each patch the field is approximately constant and the patch is approximately flat, so Layer 2 applies patch-by-patch. Define the vector area element $d\vec{A}=\hat{n}\,dA$. Then

$$
\Phi=\iint_S \vec{F}\cdot d\vec{A}=\iint_S \vec{F}\cdot\hat{n}\,dA.
$$

This is the **surface integral of the normal component of $\vec{F}$**. For flat patches and uniform fields it collapses to Layer 2, and for perpendicular uniform fields to Layer 1, so the definition is backward-compatible.

All genuinely curved-surface computations (spheres around point charges, cylinders around wires) are deferred until after the Divergence Theorem provides a symmetric-geometry shortcut.

## 4. Sign convention and choice of normal

- **Open surface** (a sheet of paper, a bowl, a disk): there are two possible choices of $\hat{n}$ that are consistent across the surface. Pick one and stick to it; flipping $\hat{n}$ flips the sign of $\Phi$ but does not change the physics.
- **Closed surface** (a balloon, a cube, a Gaussian sphere): by universal convention $\hat{n}$ is the **outward** normal. Then $\Phi>0$ means net field-line outflow (source inside), $\Phi<0$ means net inflow (sink inside), $\Phi=0$ means what goes in comes out (no enclosed source).

The closed-surface, outward-normal convention is the convention that makes Gauss's law

$$
\oint_S \vec{E}\cdot d\vec{A}=\frac{Q_{\text{enclosed}}}{\varepsilon_0}
$$

and the Divergence Theorem (W2D3) work without extra sign factors.

## 5. Worked examples

### 5.1 Guided example (3×2 rectangle, $\vec{E}$ along x̂ with a y-parallel component)

Rectangular plate $a=3~\text{m}$, $b=2~\text{m}$, $\hat{n}=\hat{x}=(1,0,0)$, uniform $\vec{E}=(4,3,0)~\text{V/m}$.

- $A=ab=6~\text{m}^2$.
- $\vec{E}\cdot\hat{n}=E_x=4~\text{V/m}$. The $E_y=3~\text{V/m}$ component is parallel to the plate and contributes nothing.
- $\Phi=(\vec{E}\cdot\hat{n})A=4\times 6=24~\text{V·m}$.

### 5.2 Independent practice ($\vec{E}$ along ŷ, normal tilted 60° in yz-plane)

Plate area $A=5~\text{m}^2$, $\vec{E}=(0,10,0)~\text{V/m}$, $\hat{n}=(0,\cos60°,\sin60°)=(0,0.5,\sqrt{3}/2)$.

- $\vec{E}\cdot\hat{n}=10\times 0.5=5~\text{V/m}$. The z-component of $\hat{n}$ pairs with $E_z=0$ and contributes nothing.
- $\Phi=5\times 5=25~\text{V·m}$.
- Cross-check by angle formula: $\theta=60°$, $EA\cos\theta=10\times 5\times 0.5=25~\text{V·m}$, agreeing.

### 5.3 Exit test ($\vec{E}$ along x̂, normal tilted 60° in xy-plane, then flipped)

Plate area $A=3~\text{m}^2$, $\vec{E}=(8,0,0)~\text{V/m}$, $\hat{n}=(\cos60°,\sin60°,0)=(0.5,\sqrt{3}/2,0)$.

(a) $\vec{E}\cdot\hat{n}=8\times 0.5=4~\text{V/m}$; $\Phi=4\times 3=12~\text{V·m}$.

(b) Flipping the normal to $-\hat{n}$ gives $\Phi'=-12~\text{V·m}$. Physics: the field itself and the physical patch are unchanged; the counting convention is reversed, so what was "12 field lines exiting the front face" is now "12 field lines entering the (newly chosen) front face". The closed-surface outward-normal convention removes this ambiguity.

## 6. Key conceptual reminders

1. **Flux is a scalar**, not a vector — you get one number per (field, oriented surface) pair.
2. **Only the normal component matters.** Tangential components slide past and contribute zero. This is why every flux formula contains a dot product with $\hat{n}$.
3. **The $\cos\theta$ rule is not an extra rule** — it is just the geometric interpretation of $\vec{E}\cdot\hat{n}$ when both vectors are written as magnitude-times-direction.
4. **Sign tells you direction of net flow.** $\Phi>0$ net outflow, $\Phi<0$ net inflow, $\Phi=0$ either no crossing or equal in-and-out.
5. **Open surface: choose $\hat{n}$ consistently.** Closed surface: outward normal by convention.
6. **Unit consistency.** $\text{V·m}$ and $\text{N·m}^2/\text{C}$ are identical because $1~\text{V/m}=1~\text{N/C}$.
7. **Notation conventions used from this day onward:** uppercase $\Phi$ for flux (lowercase $\phi$ is reserved for electric potential phase); $\hat{n}$ with a hat for the unit normal; oriented area vector $\vec{A}=\hat{n}A$; vector area element $d\vec{A}=\hat{n}\,dA$.

## 7. Exit-test summary

- ET(a) $\Phi=12~\text{V·m}$: answer 12 V·m correct.
- ET(b) $\Phi'=-12~\text{V·m}$: numerical value correct; physical interpretation of the sign flip ("normal convention reversed, physics unchanged") was initially omitted and was supplied in marking feedback.
- Mastery of the projection rule and sign convention is secure; remaining points are notational and presentation.

## 8. Review queue (carried forward)

- **Notation (new, low priority):** write flux as uppercase $\Phi$ and the unit normal as $\hat{n}$ in handwritten work.
- **Answer writing (new, low priority):** when a problem asks for a one-sentence physical interpretation, write it rather than giving only the numerical result.
- Vector-operator input/output types (from W2D1): always state both what goes in and what comes out when classifying grad/div/curl.
- Two-dimensional curl is the z-component of the full 3D curl; state the curl–circulation relation as a local limit per unit area in a chosen normal.
- OOP: continue deepening `self`, mutation vs returning new objects, inheritance vs composition (W1D5 carried).

## 9. Mastery

Approximately **90%** for the flux concept cluster, assessed across four problems (two diagnostic questions on prior intuition, one guided example, one independent practice, one two-part exit test). The geometric projection idea and sign convention are both secure; the only gaps are notational habit and one missing sentence of interpretation.

## 10. Where this gets reused

- **W2D3 Divergence theorem:** connects today's closed-surface flux to the volume integral of divergence:

$$
\oint_S\vec{F}\cdot\hat{n}\,dA=\iiint_V(\nabla\cdot\vec{F})\,dV.
$$

This is the mathematical backbone of Gauss's law.
- **ELEC0019 Gauss's law:** spherical, cylindrical and planar symmetry all rely on the Layer-2 perpendicular/parallel split on carefully chosen Gaussian surfaces.
- **ELEC0020 Faraday's law:** magnetic flux $\Phi_B$ through a loop and its time derivative drive induced emf: $\mathcal{E}=-d\Phi_B/dt$.
- **Photonics / waveguides:** Poynting-vector flux through a cross-section gives optical power.
- **Heat transfer / fluids:** heat flux and mass flux are the same mathematical object with different fields.

## 11. Resources

- W2D1 notes and exercises (gradient, divergence, curl, line integral as direct precursors).
- UCL ENGF0004 recommended textbook sections on surface integrals and flux (the three-layer structure above follows the standard engineering-text presentation).
- The magnetic-flux intuition offered by the student in the diagnostic is consistent with the A-level/Further Maths treatment and is a valid anchor.

---

**Next session (Week 2 Day 3):** Divergence theorem, Gauss's law in integral form, and symmetric-surface flux computations. Stokes' theorem, Python visualisation and Maxwell/Poisson connections remain queued after that.
