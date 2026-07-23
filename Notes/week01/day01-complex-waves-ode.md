# Week 1 Day 1: Complex Numbers, Waves and ODEs

## Related modules

- ENGF0004 Mathematical Modelling and Analysis II
- ELEC0019 Physics for Electronics and Nanotechnology 2
- ELEC0020 Photonics and Communication Systems
- ELEC0021 Programming and Control Systems

## 1. Euler's formula

$$
e^{j\theta} = \cos\theta + j\sin\theta
$$

Therefore,

$$
\cos\theta =
\frac{e^{j\theta}+e^{-j\theta}}{2}
$$

and

$$
\sin\theta =
\frac{e^{j\theta}-e^{-j\theta}}{2j}
$$

## 2. Travelling waves

A wave of the form

$$
u(x,t)=A\cos(\omega t-\beta x+\phi)
$$

travels in the positive \(x\)-direction.

A wave of the form

$$
u(x,t)=A\cos(\omega t+\beta x+\phi)
$$

travels in the negative \(x\)-direction.

The direction can be determined by keeping the phase constant.

## 3. Wave parameters

$$
v_p=\frac{\omega}{\beta}
$$

$$
\lambda=\frac{2\pi}{\beta}
$$

$$
f=\frac{\omega}{2\pi}
$$

## 4. ODE solution types

Oscillatory equation:

$$
y''+\beta^2y=0
$$

with solution

$$
y=A\cos(\beta x)+B\sin(\beta x)
$$

Exponential equation:

$$
y''-\alpha^2y=0
$$

with solution

$$
y=Ae^{\alpha x}+Be^{-\alpha x}
$$

## 5. Boundary conditions

If the solution must remain finite as \(x\to+\infty\),
the coefficient of \(e^{\alpha x}\) must be zero.

## 6. Reflection

### What I understood

- I can determine the propagation direction using constant phase.
- I can calculate phase velocity, wavelength and frequency.
- I can distinguish oscillatory and exponential ODE solutions.

### What I need to review

- Full complex field versus spatial phasor
- Complex exponential form of sine
- Spatial attenuation versus temporal variation