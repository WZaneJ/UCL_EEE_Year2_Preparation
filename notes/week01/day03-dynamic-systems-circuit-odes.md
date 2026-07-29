# Week 1 Day 3 - Dynamic systems and circuit ODEs

- Date: 2026-07-29
- Status: complete (exit test 5/5; mastery estimate about 95%)
- Knowledge chain: ODEs -> Laplace transforms -> transfer functions -> Bode plots -> feedback and control
- Exercises: [06 - entry diagnostic](../../exercises/week01/06-circuit-ode-diagnostic.md), [07 - circuit ODE practice](../../exercises/week01/07-circuit-ode-practice.md), [08 - circuit ODE exit test](../../exercises/week01/08-circuit-ode-exit-test.md)
- Simulation: [circuit_ode_sim.py](../../python/week01/circuit_ode_sim.py)

## 1. Objectives

- derive ODE models of RC, RL and series RLC circuits from KVL/KCL;
- solve first-order step responses and interpret the time constant;
- apply continuity rules: capacitor voltage and inductor current cannot jump;
- classify second-order responses (over- / critically / under-damped);
- verify closed-form solutions numerically with `scipy.integrate.solve_ivp`;
- foreshadow the natural/forced response split (formalised with Laplace in Week 5).

## 2. From KVL/KCL to circuit ODEs

Series RC driven by a step of amplitude $V_0$ at $t = 0$ (capacitor initially uncharged).
KVL gives $v_R + v_C = V_0$; with $v_R = Ri$ and $i = C\,\frac{dv_C}{dt}$:

$$
RC\frac{dv_C}{dt} + v_C = V_0
$$

Series RL, same reasoning:

$$
L\frac{di}{dt} + Ri = V_0
$$

Both reduce to the standard first-order form

$$
\frac{dy}{dt} + \frac{1}{\tau} y = f(t)
$$

**Reading rule:** the coefficient of $y$ is $1/\tau$, not $\tau$. Dividing the RC
equation by $RC$ leaves the coefficient $1/(RC)$, hence $\tau = RC$. Units check:
$[R]$ is V/A and $[C]$ is A*s/V, so $[RC]$ is s; the wrong guess $1/(RC)$ would be a
frequency, which exposes the slip immediately.

## 3. First-order prototype solution

$$
\frac{dy}{dt} = -\frac{y}{\tau}, \qquad y(0) = y_0
$$

Separation of variables, then the three finishing steps (exponentiate, rename the
constant, apply the initial condition):

$$
\ln|y| = -\frac{t}{\tau} + C \quad \Rightarrow \quad y = e^{C} e^{-t/\tau} = A e^{-t/\tau}
\quad \Rightarrow \quad y = y_0 e^{-t/\tau}
$$

Arbitrary constants absorb signs and scaling factors; rename them ($A = e^{C}$)
instead of carrying them through the algebra.

RC charging with $v_C(0^+) = 0$: the general solution is the homogeneous part plus
the steady state, $v_C = A e^{-t/\tau} + V_0$, and the initial condition gives $A = -V_0$:

$$
v_C(t) = V_0\left(1 - e^{-t/\tau}\right), \qquad \tau = RC
$$

$$
i(t) = C\frac{dv_C}{dt} = \frac{V_0}{R} e^{-t/\tau}
$$

Physical readings: $v_C(\tau) = \left(1 - e^{-1}\right)V_0 \approx 0.632 V_0$;
$v_C(5\tau) > 0.99 V_0$ (settled). Discharging a charged capacitor through $R$
gives the prototype decay $v_C = V_0 e^{-t/\tau}$.

## 4. Continuity rules

From $i = C\,\frac{dv_C}{dt}$: a finite current implies a finite derivative, so $v_C$
is continuous across a switching instant, $v_C(0^+) = v_C(0^-)$. From
$v_L = L\,\frac{di_L}{dt}$, the inductor current is continuous in the same way.
"No jump" means continuity; the derivative can still jump: in RC charging the current
steps from 0 to $V_0/R$ at $t = 0^+$ while $v_C(0^+)$ stays 0.

## 5. Series RLC and the three damping regimes

KVL with $i = C\,\frac{dv_C}{dt}$ and $v_L = L\,\frac{di}{dt} = LC\frac{d^2v_C}{dt^2}$:

$$
LC\frac{d^2v_C}{dt^2} + RC\frac{dv_C}{dt} + v_C = V_0
$$

The trial solution $e^{st}$ (the Day-1 method) gives the characteristic equation

$$
s^2 + \frac{R}{L}s + \frac{1}{LC} = 0
$$

Define

$$
\alpha = \frac{R}{2L}, \qquad \omega_0 = \frac{1}{\sqrt{LC}}, \qquad
\zeta = \frac{\alpha}{\omega_0} = \frac{R}{2}\sqrt{\frac{C}{L}}
$$

so that

$$
s = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2}
$$

| condition | damping | regime | qualitative response |
|---|---|---|---|
| $\alpha > \omega_0$ | $\zeta > 1$ | over-damped | two negative real poles; slow settling, no oscillation |
| $\alpha = \omega_0$ | $\zeta = 1$ | critically damped | repeated pole; fastest non-oscillatory settling; boundary $R = 2\sqrt{L/C}$ |
| $\alpha < \omega_0$ | $\zeta < 1$ | under-damped | ringing at $\omega_d$ inside an exponential envelope |

Under-damped case:

$$
\omega_d = \sqrt{\omega_0^2 - \alpha^2}, \qquad s = -\alpha \pm j\omega_d
$$

$$
v_C(t) = V_0 + e^{-\alpha t}\left(A\cos(\omega_d t) + B\sin(\omega_d t)\right)
$$

Structure: the Day-1 oscillation (sin/cos from complex conjugate roots) multiplied by
the first-order exponential envelope $e^{-\alpha t}$. The limit $R \to 0$ recovers the
undamped oscillator $s = \pm j\omega_0$ of Day 1.

## 6. Natural and forced response (foreshadow)

The homogeneous part (decaying exponentials, fixed by the circuit poles alone) is the
natural response; the particular part (the steady-state value $V_0$, fixed by the
source) is the forced response. Week 5 makes this split systematic with the Laplace
transform and transfer functions.

## 7. Computational verification

`python/week01/circuit_ode_sim.py` (+ `circuit_ode_sim.png`):

- RC charge/discharge curves with a `solve_ivp` cross-check;
  max |analytic - numeric| is about $10^{-9}$ V;
- the three exercise-07 RLC cases ($R = 16, 20, 40$ ohm) reproduce the hand-calculated
  $\alpha$, $\zeta$ and $\omega_d$ exactly, plus a demo case $R = 4$ ohm ($\zeta = 0.2$,
  overshoot about 52.7%, $\omega_d \approx 979.8$ rad/s, $T_d = 2\pi/\omega_d \approx 6.4$ ms)
  that makes the ringing and its envelope $V_0 \pm V_0 e^{-\alpha t}$ visible;
- pattern for solvers: a second-order ODE becomes a first-order system with state
  $[v_C, i]$, where $\frac{dv_C}{dt} = \frac{i}{C}$ and $\frac{di}{dt} = \frac{V_0 - v_C - Ri}{L}$.

## 8. Worked results (exercise 07)

| item | result |
|---|---|
| P1 RC: $R = 10$ k$\Omega$, $C = 100$ $\mu$F, $V_0 = 5$ V | $\tau = 1$ s; $v_C = 5\left(1 - e^{-t}\right)$ V; $i(0^+) = 0.5$ mA; $v_C(\tau) \approx 3.16$ V |
| P2 RL: $L = 0.5$ H, $R = 100$ $\Omega$, 10 V step | $\tau = 5$ ms; $i(\infty) = 0.1$ A; $i(t) = 0.1\left(1 - e^{-200t}\right)$ A |
| P3 read-off: $v_C = 12\left(1 - e^{-t/0.002}\right)$ | $\tau = 2$ ms; steady state 12 V; $R = \tau/C = 100$ $\Omega$ |
| P4 RLC ladder: $L = 10$ mH, $C = 100$ $\mu$F | $\omega_0 = 1000$ rad/s; $R = 16$ $\Omega$: $\zeta = 0.8$ under, $\omega_d = 600$ rad/s; $R = 20$ $\Omega$: critical; $R = 40$ $\Omega$: $\zeta = 2$ over |

## 9. Notation pitfall (flagged to the review queue)

The second derivative is

$$
\frac{d^2v_C}{dt^2}
$$

Writing $\frac{dv_C^2}{dt}$ instead denotes the derivative of the square,
$\frac{d}{dt}\left(v_C^2\right) = 2v_C\frac{dv_C}{dt}$, which is a different object.
The exponent position is part of the meaning. This notation error appeared twice
during Day 3 (diagnostic Q4 and exit test ET4) and is in the review queue.

## 10. Core formulas of Day 3

$$
\frac{dy}{dt} = -\frac{y}{\tau} \Rightarrow y = y_0 e^{-t/\tau},
\qquad \tau = RC \ (\text{RC}), \qquad \tau = \frac{L}{R} \ (\text{RL})
$$

$$
v_C^{\text{charge}} = V_0\left(1 - e^{-t/\tau}\right), \qquad
v_C^{\text{discharge}} = V_0 e^{-t/\tau}
$$

$$
LC\frac{d^2v_C}{dt^2} + RC\frac{dv_C}{dt} + v_C = V_0,
\qquad s^2 + \frac{R}{L}s + \frac{1}{LC} = 0
$$

$$
\alpha = \frac{R}{2L}, \qquad \omega_0 = \frac{1}{\sqrt{LC}}, \qquad
\zeta = \frac{\alpha}{\omega_0}, \qquad
\omega_d = \sqrt{\omega_0^2 - \alpha^2}, \qquad
R_{\text{critical}} = 2\sqrt{\frac{L}{C}}
$$

## 11. Review queue (carried forward)

1. Second-derivative notation $\frac{d^2v_C}{dt^2}$ (flagged twice on Day 3).
2. Vector answers need magnitude and direction; numeric answers need units (from Day 2).
3. Keep $dx$ (space) and $dt$ (time) derivatives distinct; recheck before the Week 4 wave equation.
4. Electron-energy sign convention $U = -eV$; recheck before Week 8 PN-junction band bending.

## 12. Where this gets reused

- Week 4: the same second-order structure dominates the wave equation PDE.
- Week 5: $s = -\alpha \pm j\omega_d$ becomes pole language for transfer functions
  and Bode plots; the RC charging curve is the step response of a first-order low-pass system.
- Week 7: the $e^{st}$ trial solution returns as separation of variables in the
  Schroedinger equation and in waveguide eigenmodes.
- ELEC0009 Analogue Electronics: transient behaviour, compensation and stability all
  use $\tau$ and $\zeta$ directly.
