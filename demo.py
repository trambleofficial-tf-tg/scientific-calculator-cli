"""
Demo Script - Scientific Calculator
Demonstrates key features without user interaction
"""

from calculator import basic, scientific, advanced, history

def print_section(title):
    """Print section header"""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def demo_basic_operations():
    """Demonstrate basic operations"""
    print_section("BASIC OPERATIONS")
    
    print("\nAddition: 15 + 25 =", basic.add(15, 25))
    print("Subtraction: 100 - 37 =", basic.subtract(100, 37))
    print("Multiplication: 12 * 8 =", basic.multiply(12, 8))
    print("Division: 144 / 12 =", basic.divide(144, 12))
    print("Modulo: 17 % 5 =", basic.modulo(17, 5))

def demo_scientific_operations():
    """Demonstrate scientific operations"""
    print_section("SCIENTIFIC OPERATIONS")
    
    print("\nPower: 2^10 =", scientific.power(2, 10))
    print("Square Root: sqrt(144) =", scientific.square_root(144))
    print("Cube Root: cbrt(27) =", round(scientific.cube_root(27), 2))
    print("Logarithm: log10(1000) =", scientific.logarithm(1000, 10))
    print("Natural Log: ln(e) =", round(scientific.natural_log(2.718281828), 2))
    print("Exponential: e^2 =", round(scientific.exponential(2), 4))
    print("Absolute Value: |-42| =", scientific.absolute_value(-42))

def demo_trigonometric_operations():
    """Demonstrate trigonometric operations"""
    print_section("TRIGONOMETRIC OPERATIONS")
    
    print("\nSine: sin(30°) =", round(scientific.sin(30), 4))
    print("Cosine: cos(60°) =", round(scientific.cos(60), 4))
    print("Tangent: tan(45°) =", round(scientific.tan(45), 4))
    print("Arcsine: asin(0.5) =", round(scientific.asin(0.5), 2), "degrees")
    print("Degrees to Radians: 180° =", round(scientific.deg_to_rad(180), 4), "rad")
    print("Radians to Degrees: 3.14159 rad =", round(scientific.rad_to_deg(3.14159), 2), "degrees")

def demo_advanced_operations():
    """Demonstrate advanced operations"""
    print_section("ADVANCED OPERATIONS")
    
    print("\nFactorial: 5! =", advanced.factorial(5))
    print("Percentage: 25/100 =", advanced.percentage(25, 100), "%")
    print("nth Root: 4th root of 16 =", advanced.nth_root(16, 4))
    print("GCD: GCD(48, 18) =", advanced.gcd(48, 18))
    print("LCM: LCM(4, 6) =", advanced.lcm(4, 6))

def demo_statistics():
    """Demonstrate statistical operations"""
    print_section("STATISTICS")
    
    numbers = [10, 20, 30, 40, 50]
    print(f"\nDataset: {numbers}")
    print("Mean:", advanced.mean(numbers))
    print("Median:", advanced.median(numbers))
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
    print("Range:", max(numbers) - min(numbers))

def demo_number_systems():
    """Demonstrate number system conversions"""
    print_section("NUMBER SYSTEM CONVERSIONS")
    
    print("\nDecimal to Binary: 42 =", advanced.dec_to_bin(42))
    print("Binary to Decimal: 101010 =", advanced.bin_to_dec("101010"))
    print("Decimal to Hexadecimal: 255 =", advanced.dec_to_hex(255))
    print("Hexadecimal to Decimal: FF =", advanced.hex_to_dec("FF"))
    print("Decimal to Octal: 64 =", advanced.dec_to_oct(64))
    print("Octal to Decimal: 100 =", advanced.oct_to_dec("100"))

def demo_history():
    """Demonstrate history tracking"""
    print_section("HISTORY TRACKING")
    
    history.clear_history()
    history.add_entry("15 + 25", 40)
    history.add_entry("sqrt(144)", 12)
    history.add_entry("5!", 120)
    
    print("\nHistory entries added:")
    for i, entry in enumerate(history.get_history(), 1):
        print(f"{i}. {entry['operation']} = {entry['result']} [{entry['timestamp']}]")

def demo_error_handling():
    """Demonstrate error handling"""
    print_section("ERROR HANDLING")
    
    print("\nTesting error handling...")
    
    try:
        basic.divide(10, 0)
    except ValueError as e:
        print(f"[CAUGHT] Division by zero: {e}")
    
    try:
        scientific.square_root(-1)
    except ValueError as e:
        print(f"[CAUGHT] Square root of negative: {e}")
    
    try:
        scientific.logarithm(-5, 10)
    except ValueError as e:
        print(f"[CAUGHT] Log of negative: {e}")
    
    try:
        advanced.factorial(-1)
    except ValueError as e:
        print(f"[CAUGHT] Factorial of negative: {e}")
    
    print("\nAll errors handled gracefully!")

def main():
    """Run all demonstrations"""
    print("\n" + "="*60)
    print("  SCIENTIFIC CALCULATOR - FEATURE DEMONSTRATION")
    print("  Enhanced Edition v2.0")
    print("="*60)
    
    demo_basic_operations()
    demo_scientific_operations()
    demo_trigonometric_operations()
    demo_advanced_operations()
    demo_statistics()
    demo_number_systems()
    demo_history()
    demo_error_handling()
    
    print("\n" + "="*60)
    print("  DEMONSTRATION COMPLETE!")
    print("  Run 'python main.py' to use the interactive calculator")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
