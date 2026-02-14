"""
Test script for Scientific Calculator
Run this to verify all modules are working correctly
"""

from calculator import basic, scientific, advanced, history, utils

def test_basic_operations():
    """Test basic arithmetic operations"""
    print("Testing Basic Operations...")
    assert basic.add(5, 3) == 8, "Addition failed"
    assert basic.subtract(10, 4) == 6, "Subtraction failed"
    assert basic.multiply(6, 7) == 42, "Multiplication failed"
    assert basic.divide(20, 4) == 5, "Division failed"
    assert basic.modulo(17, 5) == 2, "Modulo failed"
    print("[PASS] Basic operations")

def test_scientific_operations():
    """Test scientific operations"""
    print("\nTesting Scientific Operations...")
    assert scientific.power(2, 3) == 8, "Power failed"
    assert scientific.square_root(16) == 4, "Square root failed"
    assert abs(scientific.cube_root(27) - 3) < 0.001, "Cube root failed"
    assert abs(scientific.logarithm(100, 10) - 2) < 0.001, "Logarithm failed"
    assert abs(scientific.natural_log(2.718281828) - 1) < 0.001, "Natural log failed"
    assert scientific.absolute_value(-5) == 5, "Absolute value failed"
    print("[PASS] Scientific operations")

def test_trigonometric_operations():
    """Test trigonometric operations"""
    print("\nTesting Trigonometric Operations...")
    assert abs(scientific.sin(30) - 0.5) < 0.001, "Sine failed"
    assert abs(scientific.cos(60) - 0.5) < 0.001, "Cosine failed"
    assert abs(scientific.tan(45) - 1) < 0.001, "Tangent failed"
    assert abs(scientific.asin(0.5) - 30) < 0.001, "Arcsine failed"
    assert abs(scientific.deg_to_rad(180) - 3.14159) < 0.001, "Deg to rad failed"
    print("[PASS] Trigonometric operations")

def test_advanced_operations():
    """Test advanced operations"""
    print("\nTesting Advanced Operations...")
    assert advanced.factorial(5) == 120, "Factorial failed"
    assert advanced.percentage(25, 100) == 25, "Percentage failed"
    assert abs(advanced.nth_root(27, 3) - 3) < 0.001, "nth root failed"
    assert advanced.gcd(48, 18) == 6, "GCD failed"
    assert advanced.lcm(4, 6) == 12, "LCM failed"
    print("[PASS] Advanced operations")

def test_statistics():
    """Test statistical operations"""
    print("\nTesting Statistics...")
    numbers = [1, 2, 3, 4, 5]
    assert advanced.mean(numbers) == 3, "Mean failed"
    assert advanced.median(numbers) == 3, "Median failed"
    assert advanced.median([1, 2, 3, 4]) == 2.5, "Median (even) failed"
    print("[PASS] Statistics")

def test_number_systems():
    """Test number system conversions"""
    print("\nTesting Number System Conversions...")
    assert advanced.dec_to_bin(10) == "1010", "Dec to bin failed"
    assert advanced.bin_to_dec("1010") == 10, "Bin to dec failed"
    assert advanced.dec_to_hex(255) == "FF", "Dec to hex failed"
    assert advanced.hex_to_dec("FF") == 255, "Hex to dec failed"
    assert advanced.dec_to_oct(8) == "10", "Dec to oct failed"
    assert advanced.oct_to_dec("10") == 8, "Oct to dec failed"
    print("[PASS] Number system conversions")

def test_history():
    """Test history functionality"""
    print("\nTesting History...")
    history.clear_history()
    history.add_entry("5 + 3", 8)
    history.add_entry("10 - 4", 6)
    hist = history.get_history()
    assert len(hist) == 2, "History tracking failed"
    assert hist[0]['result'] == 8, "History entry failed"
    history.clear_history()
    assert len(history.get_history()) == 0, "History clear failed"
    print("[PASS] History")

def test_error_handling():
    """Test error handling"""
    print("\nTesting Error Handling...")
    try:
        basic.divide(10, 0)
        assert False, "Division by zero should raise error"
    except ValueError:
        pass
    
    try:
        scientific.square_root(-1)
        assert False, "Square root of negative should raise error"
    except ValueError:
        pass
    
    try:
        scientific.logarithm(-5, 10)
        assert False, "Log of negative should raise error"
    except ValueError:
        pass
    
    try:
        advanced.factorial(-1)
        assert False, "Factorial of negative should raise error"
    except ValueError:
        pass
    
    print("[PASS] Error handling")

def main():
    """Run all tests"""
    print("="*60)
    print("  Scientific Calculator - Test Suite")
    print("="*60)
    
    try:
        test_basic_operations()
        test_scientific_operations()
        test_trigonometric_operations()
        test_advanced_operations()
        test_statistics()
        test_number_systems()
        test_history()
        test_error_handling()
        
        print("\n" + "="*60)
        print("  ALL TESTS PASSED! Calculator is ready to use!")
        print("="*60)
        print("\n  Run 'python main.py' to start the calculator\n")
        
    except AssertionError as e:
        print(f"\n[FAIL] TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n[ERROR] UNEXPECTED ERROR: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
