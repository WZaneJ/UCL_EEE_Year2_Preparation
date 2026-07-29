# Weekly Progress

## Week 1: Complex numbers, fields and dynamic systems

### Day 1: Complex numbers, travelling waves and ODEs

- [x] Complete the complex-number diagnostic
- [x] Review Euler's formula
- [x] Determine wave direction using constant phase
- [x] Classify second-order ODE solutions
- [x] Run four Python visualisations
- [x] Complete the exit test

### Key results

$$
v_p = \frac{\omega}{\beta}
$$

$$
\lambda = \frac{2\pi}{\beta}
$$

$$
f = \frac{\omega}{2\pi}
$$

### Review queue

- [ ] Review the difference between a complete complex field and a phasor
- [ ] Remember the factor $2j$ in the exponential form of sine
- [ ] Distinguish spatial attenuation from temporal variation


### Day 2: Electric fields and potential

- [x] Coulomb's law
- [x] Electric field
- [x] Electric potential and potential energy
- [x] Relationship between field and potential ($E = -dV/dx$)
- [x] Sign of electron charge and electron potential energy
- [x] Gauss's law and symmetry (preview)
- [x] Python visualisation
- [x] Practice questions
- [x] Exit test

### Key results

$$
\mathbf{E}(r) = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}\,\hat{\mathbf{r}}
$$

$$
V(r) = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r}
$$

$$
E_x = -\frac{dV}{dx}
$$

$$
|\mathbf{E}| = \frac{V_0}{d}\quad	ext{(parallel plate)}
$$

### Review queue

- [ ] Consistently write both magnitude and direction for vector answers
- [ ] Keep $dx$ (spatial) and $dt$ (time) derivatives distinct in notation
- [ ] Reinforce the sign convention for electron potential energy $U = -eV$

### Day 3: Dynamic systems and circuit ODEs

- [x] Entry diagnostic: R1 + Q1-Q4 (exercise 06)
- [x] RC/RL first-order step response and time constants ($\tau = RC$, $\tau = L/R$)
- [x] Continuity rules for $v_C$ and $i_L$
- [x] Series RLC characteristic equation and the three damping regimes
- [x] Mid-session practice P1-P4, about 20 min (exercise 07)
- [x] Python simulation `circuit_ode_sim.py` with figure
- [x] Exit test ET1-ET5 (exercise 08)

### Key results

- Three handwritten tests archived (exercises 06, 07, 08); exit test 5/5; mastery estimate about 95%.
- Gap closed: finishing separation of variables (explicit exponential plus initial condition), done independently in P1 and P2 of exercise 07.
- Time-constant reading in both directions: ODE -> $\tau = RC$; measured $i(t) = 0.02 e^{-500t}$ A -> $\tau = 2$ ms.
- RLC ladder $R = 16, 20, 40~\Omega$ -> $\zeta = 0.8, 1, 2$ classified by hand and confirmed by simulation (numerical error about $10^{-9}$ V).

### Review queue

- [ ] Second-derivative notation $\frac{d^2v_C}{dt^2}$ (flagged twice on Day 3: diagnostic Q4 and exit test ET4).
- [ ] Vector answers need magnitude and direction; numeric answers need units (from Day 2).
- [ ] Keep $dx$ (space) and $dt$ (time) derivatives distinct; recheck before the Week 4 wave equation.
- [ ] Electron-energy sign convention $U = -eV$; recheck before Week 8 PN-junction band bending.

### Day 4: Semiconductor and photonics foundations
