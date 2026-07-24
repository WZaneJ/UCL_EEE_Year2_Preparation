# Week 1 Day 1 Exercises

## Exercise 3: Exit Test

### Question 1: Propagation direction and wave parameters

Given

$$
E(z,t)=6\cos\left(30t+10z-\frac{\pi}{6}\right),
$$

determine:

1. the angular frequency $\omega$;
2. the phase constant $\beta$;
3. the propagation direction;
4. the magnitude of the phase velocity;
5. the wavelength;
6. the frequency.

### Question 2: Complex field and spatial phasor

Given

$$
E(z,t)=4\cos\left(5t-2z+\frac{\pi}{3}\right),
$$

write a complex function $\widetilde{E}(z,t)$ such that

$$
E(z,t)=\Re\{\widetilde{E}(z,t)\}.
$$

Then, using the $e^{j\omega t}$ convention, write the corresponding spatial phasor $\widetilde{E}(z)$.

### Question 3: Classification of ODE solutions

Classify the solutions of the following equations as oscillatory, exponential, or repeated-root exponential. A full solution is not required.

1. 
   $$
   y''+25y=0
   $$

2. 
   $$
   y''-25y=0
   $$

3. 
   $$
   y''+10y'+25y=0
   $$

### Question 4: Physical boundary condition

In the region $z\geq0$, let

$$
E(z)=Ae^{3z}+Be^{-3z}.
$$

If

$$
\lim_{z\to+\infty}|E(z)|<\infty,
$$

determine the required condition on $A$ and explain why.

### Question 5: Interpretation of the Python results

Answer the following in your own words:

1. Why does
   ```python
   np.cos(omega * t - beta * x)
   ```
   represent propagation in the positive $x$-direction?

2. Why does
   ```python
   np.exp(-alpha * x)
   ```
   not represent a periodic travelling wave?

3. If `beta` increases while `omega` remains constant, how do the wavelength and phase velocity change?

## Exit-test answer

![Exit-test answer](03-exit-test-answer.jpg)
