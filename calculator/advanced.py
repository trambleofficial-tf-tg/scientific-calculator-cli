"""Advanced mathematical operations module"""
import math

def factorial(n):
    """Calculate factorial of n"""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n > 170:
        raise ValueError("Number too large for factorial calculation")
    return math.factorial(n)

def percentage(value, total):
    """Calculate percentage"""
    if total == 0:
        raise ValueError("Total cannot be zero")
    return (value / total) * 100

def nth_root(number, n):
    """Calculate nth root of a number"""
    if n == 0:
        raise ValueError("Root degree cannot be zero")
    if number < 0 and n % 2 == 0:
        raise ValueError("Even root of negative number is undefined")
    if number < 0:
        return -math.pow(-number, 1/n)
    return math.pow(number, 1/n)

def gcd(a, b):
    """Calculate Greatest Common Divisor"""
    return math.gcd(abs(a), abs(b))

def lcm(a, b):
    """Calculate Least Common Multiple"""
    return abs(a * b) // math.gcd(abs(a), abs(b))

def mean(numbers):
    """Calculate mean (average) of numbers"""
    if len(numbers) == 0:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(numbers) / len(numbers)

def median(numbers):
    """Calculate median of numbers"""
    if len(numbers) == 0:
        raise ValueError("Cannot calculate median of empty list")
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n % 2 == 0:
        return (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    return sorted_nums[n//2]

def dec_to_bin(n):
    """Convert decimal to binary"""
    if n < 0:
        return '-' + bin(abs(n))[2:]
    return bin(n)[2:]

def bin_to_dec(binary_str):
    """Convert binary to decimal"""
    try:
        return int(binary_str, 2)
    except ValueError:
        raise ValueError("Invalid binary number")

def dec_to_oct(n):
    """Convert decimal to octal"""
    if n < 0:
        return '-' + oct(abs(n))[2:]
    return oct(n)[2:]

def oct_to_dec(octal_str):
    """Convert octal to decimal"""
    try:
        return int(octal_str, 8)
    except ValueError:
        raise ValueError("Invalid octal number")

def dec_to_hex(n):
    """Convert decimal to hexadecimal"""
    if n < 0:
        return '-' + hex(abs(n))[2:].upper()
    return hex(n)[2:].upper()

def hex_to_dec(hex_str):
    """Convert hexadecimal to decimal"""
    try:
        return int(hex_str, 16)
    except ValueError:
        raise ValueError("Invalid hexadecimal number")
