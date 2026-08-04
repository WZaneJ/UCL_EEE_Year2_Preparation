# Exercise 13 - OOP Exit Test

- Week 1, Day 5 | Type: exit test (Python coding) | Date: 2026-08-03
- Companion notes: [day05-python-oop-wave-class.md](../../notes/week01/day05-python-oop-wave-class.md)
- Result: 5/5 correct; mastery estimate about 90%

## Questions

**ET1.** Write the complete Python code for a `Circle` class with:
- Attributes: `radius`
- Methods: `area()`, `circumference()`, `describe()`

**ET2.** Given the `Wave` class, what is the output of:
```python
w1 = Wave(2.0, 50.0)
w2 = Wave(1.0, 50.0, np.pi/2)
w3 = w1.add_wave(w2)
print(w3.amplitude)
print(w3.phase)
```

**ET3.** Explain the difference between `TravellingWave` and `StandingWave` in terms of:
- Mathematical expression
- Physical behavior
- Energy propagation

**ET4.** Write a method `time_shift(self, delta_t)` for the `Wave` class that shifts the wave in time.

**ET5.** What is the purpose of `super().__init__()` in inheritance? Provide an example.

## Key Results

### ET1: Circle Class

```python
import numpy as np

class Circle:
    def __init__(self, radius):
        """Initialize circle with radius"""
        self.radius = radius
    
    def area(self):
        """Calculate area: π * r²"""
        return np.pi * self.radius ** 2
    
    def circumference(self):
        """Calculate circumference: 2 * π * r"""
        return 2 * np.pi * self.radius
    
    def describe(self):
        """Print circle description"""
        print(f"Circle with radius {self.radius}")
        print(f"  Area: {self.area():.2f}")
        print(f"  Circumference: {self.circumference():.2f}")

# Test
c = Circle(5)
c.describe()
# Output:
# Circle with radius 5
#   Area: 78.54
#   Circumference: 31.42
```

### ET2: Wave Superposition Output

**Output**:
```
3.0
0.0
```

**Explanation**:
```python
w1 = Wave(2.0, 50.0)        # A=2.0, f=50, φ=0
w2 = Wave(1.0, 50.0, np.pi/2)  # A=1.0, f=50, φ=π/2

w3 = w1.add_wave(w2)
# add_wave: amplitude = w1.amplitude + w2.amplitude = 2.0 + 1.0 = 3.0
# phase: uses w1.phase = 0 (not w2.phase)

print(w3.amplitude)  # 3.0
print(w3.phase)      # 0.0
```

### ET3: TravellingWave vs StandingWave

**Mathematical Expression**:
- TravellingWave: $y(t,x) = A \sin(\omega t - \beta x + \phi)$
- StandingWave: $y(t,x) = 2A \cos(\beta x) \sin(\omega t + \phi)$

**Physical Behavior**:
- TravellingWave: Wave propagates through space, shape moves
- StandingWave: Wave pattern fixed, nodes don't move

**Energy Propagation**:
- TravellingWave: Energy propagates with the wave
- StandingWave: Energy oscillates locally, no net propagation

```python
class TravellingWave(Wave):
    def __init__(self, amplitude, frequency, phase=0, direction=1):
        super().__init__(amplitude, frequency, phase)
        self.direction = direction
    
    def evaluate(self, t, x=0):
        beta = self.omega  # Assuming v=1
        return self.amplitude * np.sin(
            self.omega * t - self.direction * beta * x + self.phase
        )

class StandingWave(Wave):
    def __init__(self, amplitude, frequency, phase=0):
        super().__init__(amplitude, frequency, phase)
    
    def evaluate(self, t, x=0):
        beta = self.omega  # Assuming v=1
        return 2 * self.amplitude * np.cos(beta * x) * np.sin(
            self.omega * t + self.phase
        )
```

### ET4: time_shift Method

```python
class Wave:
    def __init__(self, amplitude, frequency, phase=0):
        self.amplitude = amplitude
        self.frequency = frequency
        self.phase = phase
        self.omega = 2 * np.pi * frequency
    
    def evaluate(self, t):
        return self.amplitude * np.sin(self.omega * t + self.phase)
    
    def time_shift(self, delta_t):
        """
        Shift wave in time by delta_t seconds.
        
        Time shift Δt is equivalent to phase shift Δφ = ω * Δt
        Because: sin(ω(t + Δt) + φ) = sin(ωt + ωΔt + φ)
        """
        self.phase += self.omega * delta_t
        print(f"Time shifted by {delta_t} s")
        print(f"  New phase: {self.phase:.2f} rad")

# Test
w = Wave(2.0, 50.0)  # f=50 Hz, φ=0
w.time_shift(0.005)  # Shift by 5 ms
# New phase = ω * Δt = 2π*50*0.005 = π/2 ≈ 1.57 rad
```

**Explanation**:
- Time shift Δt converts to phase shift: Δφ = ω * Δt
- This works because sin(ω(t + Δt) + φ) = sin(ωt + ωΔt + φ)
- The method modifies the phase attribute directly (mutable style)

### ET5: super().__init__() in Inheritance

**Purpose**: Calls the parent class's `__init__` method to initialize inherited attributes.

**Why Needed**: 
- Ensures parent class is properly initialized
- Avoids code duplication
- Maintains inheritance hierarchy

**Example**:

```python
class Wave:
    """Parent class"""
    def __init__(self, amplitude, frequency, phase=0):
        self.amplitude = amplitude
        self.frequency = frequency
        self.phase = phase
        self.omega = 2 * np.pi * frequency
    
    def evaluate(self, t):
        return self.amplitude * np.sin(self.omega * t + self.phase)

class TravellingWave(Wave):
    """Child class inheriting from Wave"""
    def __init__(self, amplitude, frequency, phase=0, direction=1):
        # Call parent's __init__ to initialize inherited attributes
        super().__init__(amplitude, frequency, phase)
        # Add new attribute specific to TravellingWave
        self.direction = direction
    
    def evaluate(self, t, x=0):
        beta = self.omega
        return self.amplitude * np.sin(
            self.omega * t - self.direction * beta * x + self.phase
        )

# Test
tw = TravellingWave(2.0, 50.0, direction=1)
# super().__init__() initialized: amplitude, frequency, phase, omega
# TravellingWave added: direction
print(tw.amplitude)   # 2.0 (from Wave)
print(tw.direction)   # 1 (from TravellingWave)
```

**What Happens Without super().__init__()**:
```python
class BrokenWave(Wave):
    def __init__(self, amplitude, frequency, direction=1):
        # Missing super().__init__()!
        self.direction = direction

bw = BrokenWave(2.0, 50.0)
# print(bw.amplitude)  # AttributeError: 'BrokenWave' object has no attribute 'amplitude'
# print(bw.omega)      # AttributeError: 'BrokenWave' object has no attribute 'omega'
```