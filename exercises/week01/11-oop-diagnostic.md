# Exercise 11 - OOP Diagnostic

- Week 1, Day 5 | Type: diagnostic (Python coding) | Date: 2026-08-03
- Companion notes: [day05-python-oop-wave-class.md](../../notes/week01/day05-python-oop-wave-class.md)
- Result: All questions answered correctly

## Questions

**Q1.** What is the difference between a class and an object in Python? Provide an example.

**Q2.** Explain the purpose of the `__init__` method. When is it called? What does `self` represent?

**Q3.** What is the difference between a class attribute and an instance attribute? Give an example of each.

**Q4.** Write the complete code to create a `Wave` object with amplitude=2.0, frequency=50.0, and call its `info()` method.

## Key Results

### Q1: Class vs Object

**Class**: A blueprint or template for creating objects. It defines attributes (data) and methods (behavior).

**Object**: An instance of a class. Each object has its own attribute values.

```python
# Class definition
class Wave:
    def __init__(self, amplitude, frequency):
        self.amplitude = amplitude
        self.frequency = frequency

# Object creation
w1 = Wave(2.0, 50.0)  # Object 1
w2 = Wave(1.5, 100.0) # Object 2
```

### Q2: __init__ and self

**`__init__`**: Constructor method, automatically called when creating a new object. Used to initialize attributes.

**`self`**: Reference to the instance being created/accessed. Allows access to object's attributes and methods.

```python
class Wave:
    def __init__(self, amplitude, frequency):  # Called automatically
        self.amplitude = amplitude  # 'self' refers to the new object
        self.frequency = frequency

w = Wave(2.0, 50.0)  # __init__(w, 2.0, 50.0) called implicitly
```

### Q3: Class vs Instance Attributes

**Class Attribute**: Shared by all instances, defined at class level.

**Instance Attribute**: Unique to each object, defined in `__init__`.

```python
class Wave:
    wave_type = "sine"  # Class attribute (shared)
    
    def __init__(self, amplitude):
        self.amplitude = amplitude  # Instance attribute (unique)

w1 = Wave(2.0)
w2 = Wave(3.0)
print(Wave.wave_type)  # "sine" (same for all)
print(w1.amplitude)    # 2.0 (unique to w1)
print(w2.amplitude)    # 3.0 (unique to w2)
```

### Q4: Creating Wave Object

```python
import numpy as np

class Wave:
    def __init__(self, amplitude, frequency, phase=0):
        self.amplitude = amplitude
        self.frequency = frequency
        self.phase = phase
        self.omega = 2 * np.pi * frequency
    
    def info(self):
        print(f"Amplitude: {self.amplitude}")
        print(f"Frequency: {self.frequency} Hz")
        print(f"Phase: {self.phase:.2f} rad")

# Create object and call info()
w = Wave(amplitude=2.0, frequency=50.0)
w.info()
```

**Output**:
```
Amplitude: 2.0
Frequency: 50.0 Hz
Phase: 0.00 rad
```