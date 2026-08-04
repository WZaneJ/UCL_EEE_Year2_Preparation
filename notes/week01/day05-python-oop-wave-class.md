# Week 1 Day 5: Python OOP - Wave Class

- Date: 2026-08-03
- Status: complete (exit test passed; mastery estimate about 90%)
- Knowledge chain: Complex numbers -> OOP -> Wave simulation -> Scientific computing
- Exercises: [11 - OOP diagnostic](exercises/week01/11-oop-diagnostic.md), [12 - Wave class practice](exercises/week01/12-wave-class-practice.md), [13 - OOP exit test](exercises/week01/13-oop-exit-test.md)
- Simulation: [wave_class_basic.py](python/week01/wave_class_basic.py), [wave_class_extended.py](python/week01/wave_class_extended.py), [wave_types_comparison.py](python/week01/wave_types_comparison.py)

## 1. Objectives

- Understand Python OOP concepts: class, object, attributes, methods
- Master `__init__` constructor and `self` parameter
- Implement a Wave class with amplitude, frequency, phase attributes
- Create methods: evaluate, plot, info, shift_phase, add_wave, sample
- Extend to specialized wave types: TravellingWave, StandingWave
- Connect OOP with scientific computing (NumPy, Matplotlib)

## 2. OOP Fundamentals

### 2.1 Class vs Object

**Class**: Blueprint or template for creating objects
- Defines attributes (data) and methods (behavior)
- Example: `Wave` class defines what a wave is

**Object**: Instance of a class
- Created from the class blueprint
- Each object has its own attribute values
- Example: `w = Wave(2.0, 50.0)` creates a specific wave

### 2.2 Basic Syntax

```python
class Wave:
    # Class attribute (shared by all instances)
    wave_type = "sine"
    
    # Constructor method (called when creating objects)
    def __init__(self, amplitude, frequency, phase=0):
        # Instance attributes (unique to each object)
        self.amplitude = amplitude
        self.frequency = frequency
        self.phase = phase
        self.omega = 2 * np.pi * frequency
    
    # Instance method
    def evaluate(self, t):
        return self.amplitude * np.sin(self.omega * t + self.phase)
```

### 2.3 Key Concepts

- `__init__`: Constructor method, automatically called when creating objects
- `self`: Reference to the instance being created/used
- Instance attributes: Unique to each object (`self.amplitude`)
- Class attributes: Shared by all instances (`wave_type`)
- Methods: Functions defined inside a class

## 3. Wave Class Implementation

### 3.1 Basic Wave Class

```python
class Wave:
    def __init__(self, amplitude, frequency, phase=0):
        self.amplitude = amplitude
        self.frequency = frequency
        self.phase = phase
        self.omega = 2 * np.pi * frequency
    
    def evaluate(self, t):
        return self.amplitude * np.sin(self.omega * t + self.phase)
    
    def plot(self):
        period = 1.0 / self.frequency
        t = np.linspace(0, period, 1000)
        y = self.evaluate(t)
        # Matplotlib plotting code
    
    def info(self):
        print(f"Amplitude: {self.amplitude}")
        print(f"Frequency: {self.frequency} Hz")
```

### 3.2 Extended Wave Class

Added methods:
- `shift_phase(delta_phi)`: Modify phase directly (mutation)
- `add_wave(other_wave)`: Create new wave with combined amplitude
- `sample(t_array)`: Evaluate at multiple time points

### 3.3 Specialized Wave Types

**TravellingWave** (inherits from Wave):
$$y(t,x) = A \sin(\omega t - \beta x + \phi)$$
- Has direction property (+1 or -1)
- Wave propagates through space

**StandingWave** (inherits from Wave):
$$y(t,x) = 2A \cos(\beta x) \sin(\omega t + \phi)$$
- Nodes at fixed positions
- Energy oscillates but doesn't propagate

## 4. Computational Verification

### 4.1 Basic Wave Class
- Created Wave objects with different parameters
- Verified evaluate method produces correct sine waves
- Confirmed plotting displays waveforms correctly

### 4.2 Extended Features
- Tested phase shifting: `wave.shift_phase(np.pi/2)`
- Tested wave superposition: `wave3 = wave1.add_wave(wave2)`
- Tested sampling: `samples = wave.sample(t_array)`

### 4.3 Wave Type Comparison
- Compared travelling vs standing wave spatial patterns
- Verified mathematical expressions match physical behavior
- Confirmed node positions in standing waves

## 5. Connection to Day 1 Knowledge

### 5.1 Complex Numbers
- Wave can be represented as complex phasor: $y = A e^{j(\omega t + \phi)}$
- Real part gives physical wave: $Re[y] = A \cos(\omega t + \phi)$
- This connection will be formalized in Week 4 (Fourier analysis)

### 5.2 ODE Solutions
- Wave equation is second-order PDE
- Standing wave solution uses separation of variables
- Travelling wave solution uses characteristic method

## 6. Python Implementation Details

### 6.1 Code Structure
```python
# Import statements
import numpy as np
import matplotlib.pyplot as plt

# Class definition
class Wave:
    # Constructor
    def __init__(self, amplitude, frequency, phase=0):
        # Initialize attributes
    
    # Methods
    def evaluate(self, t):
        # Calculate wave value
    
    def plot(self):
        # Create visualization
    
    def info(self):
        # Print wave properties

# Main execution
if __name__ == "__main__":
    # Create objects and test methods
```

### 6.2 Best Practices
- Complete, runnable code (all imports included)
- Explicit multiplication (`*`, not implied)
- Exponentiation with `**` (not `^`)
- Clear variable names
- Comprehensive documentation

## 7. Review Queue (Carried Forward)

1. OOP self-introspection: Understanding `self` and `__init__` mechanisms
2. Method design: When to return new objects vs modify existing ones
3. Inheritance hierarchy: When to use inheritance vs composition
4. Connection to physics: Wave equation and boundary conditions

## 8. Where This Gets Reused

- Week 4: Fourier analysis - wave decomposition into frequency components
- Week 7: PDE solutions - wave equation and boundary conditions
- ELEC0021: Control systems - frequency response and transfer functions
- ELEC0020: Communications - modulation and signal processing