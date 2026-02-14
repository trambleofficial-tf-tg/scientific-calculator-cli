"""Advanced calculator features: calculus, complex numbers, equations"""
import math
import cmath

def derivative_numerical(func_str, x, h=1e-7):
    """Numerical derivative using central difference"""
    from calculator.expression import evaluate_expression
    func_str_plus = func_str.replace('x', f'({x+h})')
    func_str_minus = func_str.replace('x', f'({x-h})')
    f_plus = evaluate_expression(func_str_plus)
    f_minus = evaluate_expression(func_str_minus)
    return (f_plus - f_minus) / (2 * h)

def integral_numerical(func_str, a, b, n=1000):
    """Numerical integration using Simpson's rule"""
    from calculator.expression import evaluate_expression
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    x = a
    sum_odd = 0
    sum_even = 0
    
    for i in range(1, n):
        x = a + i * h
        func_at_x = func_str.replace('x', f'({x})')
        f_x = evaluate_expression(func_at_x)
        if i % 2 == 0:
            sum_even += f_x
        else:
            sum_odd += f_x
    
    func_at_a = func_str.replace('x', f'({a})')
    func_at_b = func_str.replace('x', f'({b})')
    f_a = evaluate_expression(func_at_a)
    f_b = evaluate_expression(func_at_b)
    
    return (h / 3) * (f_a + 4 * sum_odd + 2 * sum_even + f_b)

def solve_quadratic(a, b, c):
    """Solve quadratic equation ax^2 + bx + c = 0"""
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (x1, x2, 'real')
    else:
        real_part = -b / (2*a)
        imag_part = math.sqrt(-discriminant) / (2*a)
        return (complex(real_part, imag_part), complex(real_part, -imag_part), 'complex')

def solve_linear_system_2x2(a1, b1, c1, a2, b2, c2):
    """Solve 2x2 linear system: a1*x + b1*y = c1, a2*x + b2*y = c2"""
    det = a1*b2 - a2*b1
    if det == 0:
        raise ValueError("System has no unique solution (determinant = 0)")
    x = (c1*b2 - c2*b1) / det
    y = (a1*c2 - a2*c1) / det
    return (x, y)

def complex_add(z1, z2):
    """Add complex numbers"""
    return z1 + z2

def complex_multiply(z1, z2):
    """Multiply complex numbers"""
    return z1 * z2

def complex_divide(z1, z2):
    """Divide complex numbers"""
    if z2 == 0:
        raise ValueError("Cannot divide by zero")
    return z1 / z2

def complex_conjugate(z):
    """Complex conjugate"""
    return z.conjugate()

def complex_magnitude(z):
    """Magnitude of complex number"""
    return abs(z)

def complex_phase(z):
    """Phase angle of complex number in degrees"""
    return math.degrees(cmath.phase(z))

def complex_polar(r, theta_deg):
    """Create complex number from polar coordinates"""
    theta_rad = math.radians(theta_deg)
    return cmath.rect(r, theta_rad)

def prime_check(n):
    """Check if number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    """Get prime factorization"""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def fibonacci(n):
    """Generate Fibonacci sequence up to n terms"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def permutation(n, r):
    """Calculate permutation nPr"""
    if r > n or r < 0:
        raise ValueError("Invalid permutation parameters")
    return math.factorial(n) // math.factorial(n - r)

def combination(n, r):
    """Calculate combination nCr"""
    if r > n or r < 0:
        raise ValueError("Invalid combination parameters")
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def binomial_coefficient(n, k):
    """Calculate binomial coefficient"""
    return combination(n, k)
