# 📖 SCIENTIFIC CALCULATOR v4.0 - USER GUIDE

## Quick Start

1. Install: `pip install -r requirements.txt`
2. Run: `python main.py`
3. Select from 20 menu options
4. Enjoy 100+ mathematical operations!

## Menu Overview

### [1] Basic Arithmetic
- Addition, Subtraction, Multiplication, Division, Modulo
- Simple and fast calculations

### [2] Scientific Functions
- Power, Square Root, Cube Root
- Logarithms (any base, natural log)
- Exponential functions
- Absolute value

### [3] Trigonometry
- Sin, Cos, Tan (degrees input)
- Arcsin, Arccos, Arctan
- Degree ↔ Radian conversion

### [4] Advanced Math
- Factorial
- Percentage calculations
- nth Root
- GCD, LCM

### [5] Statistics
- Mean, Median
- Standard Deviation, Variance
- Max, Min, Range
- Input: comma-separated numbers

### [6] Number Systems
- Binary ↔ Decimal
- Octal ↔ Decimal
- Hexadecimal ↔ Decimal

### [7] Memory Functions
- M+: Add to memory
- M-: Subtract from memory
- MR: Recall memory value
- MC: Clear memory
- MS: Store new value

### [8] Constants Library
View mathematical and physical constants:
- π (pi) = 3.14159...
- e = 2.71828...
- φ (phi) = 1.61803... (golden ratio)
- c = 299792458 m/s (speed of light)
- And more!

### [9] Expression Evaluator
Type math expressions directly:
```
Examples:
2 + 3 * 4          → 14
sqrt(144)          → 12
sin(30) * 2        → 1.0
log(100)           → 2.0
2**10              → 1024
sqrt(16) + log(100) → 6.0
```

Supported functions:
- sqrt, sin, cos, tan, asin, acos, atan
- log (base 10), ln (natural log)
- exp, abs, factorial
- pow, ceil, floor

### [10] History Manager
- View last 50 calculations
- Export history to text file
- Clear history
- Automatic timestamping

### [11] Calculus
**Derivatives (Numerical)**
- Enter function using 'x' as variable
- Specify point for derivative
- Example: f(x) = x**2, find f'(3)

**Integrals (Numerical)**
- Enter function using 'x'
- Specify bounds [a, b]
- Uses Simpson's rule
- Example: ∫[0,2] x**2 dx

### [12] Complex Numbers
Operations with complex numbers:
- Addition, Subtraction, Multiplication, Division
- Magnitude and Phase angle
- Conjugate
- Polar ↔ Rectangular conversion

Example:
```
z1 = 3 + 4i
z2 = 1 + 2i
z1 * z2 = -5 + 10i
|z1| = 5.0
∠z1 = 53.13°
```

### [13] Equation Solver
**Quadratic Equations**
- Solve: ax² + bx + c = 0
- Handles real and complex solutions
- Example: 2x² + 5x - 3 = 0

**Linear Systems (2x2)**
- Solve two equations with two unknowns
- Format: a₁x + b₁y = c₁
          a₂x + b₂y = c₂

### [14] Number Theory
**Prime Check**
- Determine if number is prime
- Fast algorithm

**Prime Factorization**
- Break number into prime factors
- Example: 60 = 2 × 2 × 3 × 5

**Fibonacci Sequence**
- Generate n terms
- Example: 0, 1, 1, 2, 3, 5, 8, 13...

### [15] Combinatorics
**Permutation (nPr)**
- Arrangements where order matters
- Formula: n!/(n-r)!

**Combination (nCr)**
- Selections where order doesn't matter
- Formula: n!/(r!(n-r)!)

**Binomial Coefficient**
- Same as combination
- Used in binomial theorem

### [16] Unit Converter
**Length**: m, km, cm, mm, mi, yd, ft, in
**Weight**: kg, g, mg, lb, oz, ton
**Temperature**: Celsius, Fahrenheit, Kelvin
**Area**: sq m, sq km, sq mi, acre, hectare
**Volume**: L, mL, gal, qt, pt, cup
**Speed**: m/s, km/h, mph, knot
**Time**: s, min, hr, day, week, month, year

Examples:
- 100 km = 62.137 mi
- 75 kg = 165.347 lb
- 25°C = 77°F

### [17] Function Plotter
**Plot Functions**
- Enter function using 'x'
- Specify x range
- ASCII graph in terminal
- Example: sin(x), x**2, log(x)

**Plot Data Points**
- Enter x and y values
- Visualize data relationships
- Scatter plot style

### [18] Matrix Operations
2x2 Matrix operations:
- Addition
- Multiplication
- Determinant

Input format:
```
Row 1: 1 2
Row 2: 3 4
```

### [19] Settings & Themes
Choose your theme:
- **Default**: Cyan/Yellow (professional)
- **Dark**: Light blue/Light yellow (easy on eyes)
- **Matrix**: Green on black (hacker style)

### [20] Quick Calculator
Fast calculation mode:
- Type expressions directly
- No menu navigation
- Instant results
- Type 'exit' to return

## Tips & Tricks

### Expression Evaluator Tips
1. Use parentheses for clarity: `(2+3)*4`
2. Functions need parentheses: `sqrt(16)` not `sqrt 16`
3. Use `**` for power: `2**8` = 256
4. Chain operations: `sqrt(144) + log(100) - sin(30)`

### Memory Usage
1. Store result: Use MS after calculation
2. Build totals: Use M+ repeatedly
3. Check anytime: Use MR
4. Start fresh: Use MC

### History Management
- History auto-saves last 50 calculations
- Export before clearing for backup
- Exported file: `calculator_history.txt`

### Function Plotting
- Use simple functions for best results
- Adjust range if graph looks wrong
- Try: sin(x), cos(x), x**2, x**3, log(x)

### Unit Conversion
- Use short forms: km, lb, °C
- Case insensitive
- Check available units in menu

## Keyboard Shortcuts

- **Ctrl+C**: Cancel operation
- **Enter**: Confirm/Continue
- **Type 'exit'**: Leave quick calc mode
- **Type 'back'**: Return to previous menu

## Common Issues

### "Invalid expression"
- Check parentheses are balanced
- Ensure function names are correct
- Use 'x' as variable in functions

### "Cannot divide by zero"
- Check denominator isn't zero
- Verify input values

### "Invalid unit"
- Check spelling of unit
- Use provided unit list
- Try short forms (km, lb, etc.)

### Colors not showing
- Install colorama: `pip install colorama`
- Calculator works without colors too

## Advanced Usage

### Calculus Examples
```
Derivative of x**2 at x=5:
f'(5) = 10

Integral of x**2 from 0 to 3:
∫[0,3] x**2 dx = 9
```

### Complex Number Examples
```
Polar to Rectangular:
r=5, θ=53.13° → 3+4i

Operations:
(3+4i) * (1+2i) = -5+10i
|(3+4i)| = 5
```

### Matrix Examples
```
[1 2]   [5 6]   [6  8]
[3 4] + [7 8] = [10 12]

det([1 2]) = -2
    [3 4]
```

## Best Practices

1. **Use Quick Calc** for simple expressions
2. **Save History** before clearing
3. **Check Units** before converting
4. **Use Memory** for multi-step calculations
5. **Try Themes** to find your preference
6. **Export Results** for documentation

## Performance Notes

- Calculations are instant
- History limited to 50 entries (performance)
- Large factorials may take time (>100)
- Function plotting uses 1000 points

## Support

For issues or questions:
1. Check this guide
2. Review README.md
3. Check error messages carefully
4. Verify input format

## Updates

Current Version: 4.0.0 ULTIMATE
- 100+ operations
- Professional UI
- Advanced mathematics
- Complete unit converter

---

**Happy Calculating! 🎉**
