# Weekly Progress

## Week 1: Complex numbers, fields and dynamic systems

### Day 1: Complex numbers, travelling waves and ODEs

- [x]  Complete the complex-number diagnostic
- [x]  Review Euler's formula
- [x]  Determine wave direction using constant phase
- [x]  Classify second-order ODE solutions
- [x]  Run four Python visualisations
- [x]  Complete the exit test

### Key results

$v_p = \frac{\omega}{\beta}$

$\lambda = \frac{2\pi}{\beta}$

$f = \frac{\omega}{2\pi}$

### Review queue

- [x]  Review the difference between a complete complex field and a phasor
- [x]  Remember the factor 2j in the exponential form of sine
- [x]  Distinguish spatial attenuation from temporal variation

### Day 2: Electric fields and potential

- [x]  Coulomb's law
- [x]  Electric field
- [x]  Electric potential and potential energy
- [x]  Relationship between field and potential (E=-dV/dx)
- [x]  Sign of electron charge and electron potential energy
- [x]  Gauss's law and symmetry (preview)
- [x]  Python visualisation
- [x]  Practice questions
- [x]  Exit test

### Key results

$E(r) = \frac{1}{4\pi\varepsilon_0} \frac{Q}{r^2} \hat{r}$

$V(r) = \frac{1}{4\pi\varepsilon_0} \frac{Q}{r}$

$E_x = -\frac{dV}{dx}$

$|E| = \frac{V_0}{d}$ (parallel plate)

### Review queue

- [x]  Consistently write both magnitude and direction for vector answers
- [x]  Keep dx (spatial) and dt (time) derivatives distinct in notation
- [x]  Reinforce the sign convention for electron potential energy U=-eV

### Day 3: Dynamic systems and circuit ODEs

- [x]  Entry diagnostic: R1 + Q1-Q4 (exercise 06)
- [x]  RC/RL first-order step response and time constants (τ=RC, τ=L/R)
- [x]  Continuity rules for vC and iL
- [x]  Series RLC characteristic equation and the three damping regimes
- [x]  Mid-session practice P1-P4, about 20 min (exercise 07)
- [x]  Python simulation `circuit_ode_sim.py` with figure
- [x]  Exit test ET1-ET5 (exercise 08)

### Key results

- Three handwritten tests archived (exercises 06, 07, 08); exit test 5/5; mastery estimate about 95%.
- Gap closed: finishing separation of variables (explicit exponential plus initial condition), done independently in P1 and P2 of exercise 07.
- Time-constant reading in both directions: ODE -> τ=RC; measured i(t)=0.02e−500t A -> τ=2 ms.
- RLC ladder R=16,20,40Ω -> ζ=0.8,1,2 classified by hand and confirmed by simulation (numerical error about 10−9 V).

### Review queue

- [x]  Second-derivative notation d2vCdt2 (flagged twice on Day 3: diagnostic Q4 and exit test ET4).
- [x]  Vector answers need magnitude and direction; numeric answers need units (from Day 2).
- [x]  Keep dx (space) and dt (time) derivatives distinct; recheck before the Week 4 wave equation.
- [x]  Electron-energy sign convention U=−eV; recheck before Week 8 PN-junction band bending.

### Day 4: Semiconductor and photonics foundations

- [x]  Entry diagnostic: Q1-Q4 (exercise 09)
- [x]  Band formation from atomic levels to solids
- [x]  Conductor/semiconductor/insulator band structure comparison
- [x]  Intrinsic carriers: electrons and holes
- [x]  Doping: n-type and p-type basics
- [x]  PN junction band bending (qualitative)
- [x]  Python visualization: band diagram
- [x]  Exit test: ET1-ET3 (exercise 10)

### Key results

- Band gap Eg=EC−EV; silicon Eg=1.12,eV
- Intrinsic carrier concentration ni=pi=NCNVexp(−Eg/2kT)
- n-type: donor atoms, majority = electrons; p-type: acceptor atoms, majority = holes
- PN junction: built-in electric field causes band bending in depletion region
- Photon absorption: Ephoton≥Eg

### Review queue

- [x]  Second-derivative notation d2vCdt2
- [x]  Vector answers: magnitude + direction + units
- [x]  Keep dx and dt distinct
- [x]  Electron-energy sign convention U=−eV
- [x]  Band gap concept and carrier generation (check before Week 8)

### Day 5: Python OOP - Wave class

- [x]  Entry diagnostic: OOP concepts (exercise 11)
- [x]  Python OOP fundamentals: class, object, attributes, methods
- [x]  `__init__` constructor and `self` parameter
- [x]  Implement basic Wave class with amplitude, frequency, phase
- [x]  Methods: evaluate, plot, info, shift_phase, add_wave, sample
- [x]  Wave class practice (exercise 12)
- [x]  Extend to specialized wave types: TravellingWave, StandingWave
- [x]  Python visualization: wave_class.py with wave_visualization.png
- [x]  Exit test: OOP concepts (exercise 13)

### Key results

- OOP fundamentals: class vs object, `__init__`, `self`, instance vs class attributes
- Wave class implementation: complete with evaluation, plotting, and manipulation methods
- Wave superposition: `add_wave()` creates new wave with combined amplitude
- Specialized waves: TravellingWave (propagating) vs StandingWave (fixed nodes)
- Connection to Day 1: complex number representation of waves

### Review queue

- [ ]  OOP self-introspection: Understanding `self` and `__init__` mechanisms
- [ ]  Method design: When to return new objects vs modify existing ones
- [ ]  Inheritance hierarchy: When to use inheritance vs composition
- [ ]  Connection to physics: Wave equation and boundary conditions

## Week 2: Vector calculus, Maxwell and Poisson

### Day 1: Vector calculus foundations

- [x]  Entry diagnostic and Week 1 recall (exercise 14)
- [x]  Scalar fields, vector fields and gradient
- [x]  Electric field as $\vec{E}=-\nabla V$
- [x]  Directional derivatives and level curves
- [x]  Gradient practice (exercise 15)
- [x]  Directional-derivative and level-curve practice (exercise 16)
- [x]  Divergence, source and sink intuition (exercise 17)
- [x]  Curl and local rotation intuition
- [x]  Line-integral and circulation concept check (exercise 18)
- [x]  Exit test (exercise 19)
- [x]  Scope reduced after cognitive-load and time-budget check

### Key results

- Gradient maps a scalar field to a vector field and points in the direction of maximum increase.
- $D_{\vec{u}}f=\nabla f\cdot\vec{u}$ gives the rate of change along a unit direction.
- $\nabla\cdot\vec{F}$ is a scalar measuring local net outflow; $\nabla\times\vec{F}$ is a vector measuring local rotation tendency.
- A vector line integral accumulates the tangential component of a field along a path; a closed-path line integral is circulation.
- Six handwritten exercises archived (14-19); exit-test mastery estimate about 92%.
- Planned B-tier was about 2.5 hours; actual study time was about 4 hours including external learning, feedback and correction.

### Review queue

- [ ]  State both input and output types when classifying vector-calculus operators
- [ ]  Keep the specified direction separate from the gradient direction
- [ ]  Treat two-dimensional curl as the $z$ component of the full curl vector
- [ ]  State the curl-circulation relation as a local limit per unit area
- [ ]  Keep vector notation explicit in handwritten work and archived notes

### Day 2: Flux, integral theorems and Maxwell connections

- [ ]  Surface integrals and flux
- [ ]  Divergence theorem
- [ ]  Stokes' theorem
- [ ]  Python vector-field visualisation
- [ ]  Connection to Maxwell equations and Poisson's equation

### Key results

(To be completed)

### Review queue

(To be completed)