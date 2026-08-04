# Exercise 12 - Wave Class Practice

- Week 1, Day 5 | Type: practice (Python coding) | Date: 2026-08-03
- Companion notes: [day05-python-oop-wave-class.md](../../notes/week01/day05-python-oop-wave-class.md)
- Result: All problems solved correctly

## Questions

**P1.** Write a Python class `Rectangle` with:
- Attributes: `width`, `height`
- Methods: `area()`, `perimeter()`, `is_square()`

**P2.** Extend the `Wave` class with a method `frequency_doubler()` that returns a new `Wave` object with double the frequency.

**P3.** Create a `BankAccount` class with:
- Attributes: `owner`, `balance`
- Methods: `deposit(amount)`, `withdraw(amount)`, `get_balance()`

**P4.** Explain the difference between:
- Returning a new object from a method
- Modifying the current object's attributes

## Key Results

### P1: Rectangle Class

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate area"""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate perimeter"""
        return 2 * (self.width + self.height)
    
    def is_square(self):
        """Check if rectangle is a square"""
        return self.width == self.height

# Test
r = Rectangle(5, 3)
print(f"Area: {r.area()}")           # 15
print(f"Perimeter: {r.perimeter()}") # 16
print(f"Is square: {r.is_square()}") # False

square = Rectangle(4, 4)
print(f"Is square: {square.is_square()}")  # True
```

### P2: frequency_doubler Method

```python
import numpy as np

class Wave:
    def __init__(self, amplitude, frequency, phase=0):
        self.amplitude = amplitude
        self.frequency = frequency
        self.phase = phase
        self.omega = 2 * np.pi * frequency
    
    def evaluate(self, t):
        return self.amplitude * np.sin(self.omega * t + self.phase)
    
    def frequency_doubler(self):
        """Return new Wave with doubled frequency"""
        return Wave(self.amplitude, 2 * self.frequency, self.phase)

# Test
w1 = Wave(2.0, 50.0)
w2 = w1.frequency_doubler()
print(f"Original frequency: {w1.frequency} Hz")  # 50.0
print(f"Doubled frequency: {w2.frequency} Hz")   # 100.0
print(f"Same amplitude: {w1.amplitude == w2.amplitude}")  # True
```

### P3: BankAccount Class

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        """Withdraw money"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")
    
    def get_balance(self):
        """Get current balance"""
        return self.balance

# Test
account = BankAccount("Alice", 1000)
account.deposit(500)       # Deposited 500. New balance: 1500
account.withdraw(200)      # Withdrew 200. New balance: 1300
print(account.get_balance())  # 1300

try:
    account.withdraw(2000)  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")   # Error: Insufficient funds
```

### P4: Return New Object vs Modify Attributes

**Returning New Object (Immutable Style)**:
- Creates a new instance
- Original object unchanged
- Example: `add_wave()`, `frequency_doubler()`

```python
def add_wave(self, other):
    new_amplitude = self.amplitude + other.amplitude
    return Wave(new_amplitude, self.frequency, self.phase)

w1 = Wave(2.0, 50.0)
w2 = Wave(1.0, 50.0)
w3 = w1.add_wave(w2)  # New object created
# w1 unchanged, w3 is new
```

**Modifying Attributes (Mutable Style)**:
- Changes current object's state
- Returns None (typically)
- Example: `shift_phase()`

```python
def shift_phase(self, delta_phi):
    self.phase += delta_phi  # Modifies self
    # Returns None implicitly

w = Wave(2.0, 50.0)
w.shift_phase(np.pi/2)  # w.phase changed
```

**When to Use Which**:
- Return new: When you want to preserve original (functional programming style)
- Modify: When mutation is expected and efficient (imperative style)