# Week 1 Day 4: Semiconductor and Photonics Foundations

- Date: 2026-07-30
- Status: complete (exit test 3/3; mastery estimate about 95%)
- Knowledge chain: Quantum mechanics -> band theory -> semiconductor and photonic devices
- Exercises: [09 - entry diagnostic](../exercises/week01/09-semiconductor-diagnostic.md), [10 - exit test](../exercises/week01/10-semiconductor-exit-test.md)
- Simulation: [band_diagram.py](../python/week01/band_diagram.py)

## 1. Objectives

- Understand the transition from discrete atomic energy levels to bands in solids
- Explain the difference between conductors, semiconductors, and insulators in terms of band structure
- Describe intrinsic silicon: electrons, holes, and thermal generation
- Explain doping: donors, acceptors, n-type, p-type, majority/minority carriers
- Draw and interpret qualitative band diagrams for PN junctions at equilibrium
- Connect electron potential energy $U = -eV$ to band diagrams

## 2. From Atomic Levels to Energy Bands

In an isolated atom, electrons occupy discrete energy levels given by:

$$
E_n = -\frac{13.6\,\text{eV}}{n^2} \quad \text{(Hydrogen)}
$$

When atoms form a solid:
- Electron wavefunctions **overlap**
- Discrete levels **broaden** into **bands** due to Pauli exclusion principle

## 3. Band Structure Comparison

| Material | Valence Band | Conduction Band | Band Gap $E_g$ | Conductivity |
|----------|--------------|-----------------|----------------|--------------|
| Conductor | Overlaps with CB | Partially filled | 0 eV | Excellent |
| Semiconductor | Full | Empty | 0.1-2 eV | Moderate (T-dependent) |
| Insulator | Full | Empty | >5 eV | Very poor |

**Key formula:**
$$
E_g = E_C - E_V
$$

## 4. Intrinsic Semiconductors

### 4.1 Carrier Types
- **Electrons**: in conduction band, charge = $-e$
- **Holes**: missing electrons in valence band, effective charge = $+e$

### 4.2 Thermal Generation
$$
\text{Probability} \propto \exp\left(-\frac{E_g}{kT}\right)
$$

### 4.3 Intrinsic Carrier Concentration
$$
n_i = p_i = \sqrt{N_C N_V} \exp\left(-\frac{E_g}{2kT}\right)
$$

For Si at 300K: $n_i \approx 1.5 \times 10^{10}\,\text{cm}^{-3}$

## 5. Doping Basics

### 5.1 n-type
- **Donor** atoms (Group V: P, As, Sb)
- Extra electron donated to conduction band
- **Majority**: electrons; **Minority**: holes

### 5.2 p-type
- **Acceptor** atoms (Group III: B, Al, Ga)
- Creates hole in valence band
- **Majority**: holes; **Minority**: electrons

## 6. PN Junction at Equilibrium

### 6.1 Band Bending
- Electrons diffuse from n to p side
- Creates **depletion region** with fixed ions
- **Built-in potential** forms

### 6.2 Key Concept
$$
U(x) = -eV(x)
$$
- Electrons roll **downhill** in energy
- Holes roll **uphill** in energy

## 7. Review Queue

- [ ] Second-derivative notation $\frac{d^2v_C}{dt^2}$
- [ ] Vector answers: magnitude + direction + units
- [ ] Keep $dx$ and $dt$ distinct
- [ ] Electron-energy sign convention $U = -eV$
- [ ] Band gap concept and carrier generation (check before Week 8)

## 8. Where This Gets Reused

- Week 2: Poisson's equation for quantitative PN junction
- Week 4: Photon absorption $E = hf$ in photonics
- Week 7: Quantum wells and eigenstates
- Week 8: Semiconductor devices (diodes, transistors)