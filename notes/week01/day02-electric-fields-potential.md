# Week 1 Day 2: Electric Fields and Potential

## Related modules

- ENGF0004 Mathematical Modelling and Analysis II
- ELEC0019 Physics for Electronics and Nanotechnology 2
- ELEC0020 Photonics and Communication Systems
- ELEC0021 Programming and Control Systems

## 1. Coulomb's law and electric field

The force between two point charges is

$$
\mathbf{F} = \frac{1}{4\pi\varepsilon_0}\frac{Qq}{r^2}\,\hat{\mathbf{r}}
$$

The electric field is the force per unit test charge:

$$
\mathbf{E} = \frac{\mathbf{F}}{q}
           = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}\,\hat{\mathbf{r}},
\quad\text{units V/m (or N/C)}
$$

The constant is

$$
\frac{1}{4\pi\varepsilon_0} = 9\times10^9~\text{N·m}^2/\text{C}^2.
$$

## 2. Electric potential and potential energy

The electric potential due to a point charge (taking $V=0$ at infinity) is

$$
V(r) = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r},\qquad\text{units V}.
$$

The potential energy of a charge $q$ placed in a potential $V$ is

$$
U = qV,\qquad\text{units J}.
$$

An electron therefore has $U = -eV$, where $e = 1.6\times10^{-19}~\text{C}$.

The electron-volt is

$$
1~\text{eV} = 1.6\times10^{-19}~\text{J}.
$$

## 3. Relation between field and potential

In one dimension,

$$
E_x = -\frac{dV}{dx}.
$$

The minus sign means the electric field points in the direction of *decreasing* potential.  A positive test charge released from rest moves from higher $V$ to lower $V$.

## 4. Sign traps with the electron

Because the electron charge is $q = -e$:

- Force: $\mathbf{F} = -e\mathbf{E}$ (opposite to $\mathbf{E}$).
- Potential energy: $U = -eV$ (negative in a positive potential).
- The eV unit: gaining $1~\text{eV}$ of kinetic energy means the electron has moved through a potential difference of $1~\text{V}$.

## 5. Parallel-plate capacitor (worked example)

Two parallel plates separated by $d = 5~\text{mm}$ with a potential difference $V_0 = 20~\text{V}$.

The field is uniform between the plates:

$$
|\mathbf{E}| = \frac{V_0}{d} = \frac{20}{0.005} = 4000~\text{V/m}.
$$

The potential varies linearly:

$$
V(x) = V_0\frac{x}{d},
$$

taking $V=0$ at the negative plate and $V=V_0$ at the positive plate.

## 6. Gauss's law preview

Gauss's law relates the flux of $\mathbf{E}$ through a closed surface to the enclosed charge:

$$
\oint \mathbf{E}\cdot d\mathbf{A} = \frac{Q_{\text{enc}}}{\varepsilon_0}.
$$

It is most useful for problems with symmetry:

- **Spherical:** point charge or spherical shell.
- **Cylindrical:** infinite line charge.
- **Planar:** infinite sheet of charge.

## 7. Key conceptual reminders

- $V$ is defined up to an additive constant (only differences matter).
- $V=0$ at a point does **not** imply $\mathbf{E}=0$ there.
- $\mathbf{E}=0$ in a region implies $V$ is constant, not necessarily zero.
- Numerical answers must include units **and** direction.
- Keep $dx$ (spatial derivative) and $dt$ (time derivative) notationally distinct.

## 8. Reflection

### What I understood

- I can calculate $\mathbf{E}$ and $V$ for a point charge.
- I can obtain $\mathbf{E}$ from $V$ using $E_x = -dV/dx$.
- I can explain why the electron experiences force opposite to $\mathbf{E}$.

### What I need to review

- Applying Gauss's law to non-standard geometries
- Energy conservation in electric fields
- Relation between $E$, $V$, and work done

Python visualisation: `python/week01/electric_field_potential.py`
