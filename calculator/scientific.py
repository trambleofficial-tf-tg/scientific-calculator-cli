"""Scientific and trigonometric operations module"""
import math

def power(base, exponent):
    """Calculate base raised to exponent"""
    return base ** exponent

def square_root(x):
    """Calculate square root with negative number handling"""
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(x)

def cube_root(x):
    """Calculate cube root (works with negative numbers)"""
    if x < 0:
        return -math.pow(-x, 1/3)
    return math.pow(x, 1/3)

def logarithm(x, base=10):
    """Calculate logarithm with error handling"""
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers")
    if base <= 0 or base == 1:
        raise ValueError("Invalid logarithm base")
    return math.log(x, base)

def natural_log(x):
    """Calculate natural logarithm (ln)"""
    if x <= 0:
        raise ValueError("Natural log undefined for non-positive numbers")
    return math.log(x)

def exponential(x):
    """Calculate e^x"""
    return math.exp(x)

def absolute_value(x):
    """Calculate absolute value"""
    return abs(x)

def sin(degrees):
    """Calculate sine (input in degrees)"""
    return math.sin(math.radians(degrees))

def cos(degrees):
    """Calculate cosine (input in degrees)"""
    return math.cos(math.radians(degrees))

def tan(degrees):
    """Calculate tangent (input in degrees)"""
    return math.tan(math.radians(degrees))

def asin(value):
    """Calculate arcsine (returns degrees)"""
    if value < -1 or value > 1:
        raise ValueError("Arcsine input must be between -1 and 1")
    return math.degrees(math.asin(value))

def acos(value):
    """Calculate arccosine (returns degrees)"""
    if value < -1 or value > 1:
        raise ValueError("Arccosine input must be between -1 and 1")
    return math.degrees(math.acos(value))

def atan(value):
    """Calculate arctangent (returns degrees)"""
    return math.degrees(math.atan(value))

def deg_to_rad(degrees):
    """Convert degrees to radians"""
    return math.radians(degrees)

def rad_to_deg(radians):
    """Convert radians to degrees"""
    return math.degrees(radians)
