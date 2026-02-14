"""
SCIENTIFIC CALCULATOR - PROFESSIONAL EDITION v4.0 ULTIMATE
Complete mathematical computation system with advanced features
"""

from calculator import (basic, scientific, utils, advanced, history, memory, 
                        constants, expression, advanced_calc, converter, graphing, ui)
import os
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    """Display ultimate main menu"""
    clear()
    ui.print_banner()
    
    mem = memory.memory_recall()
    mem_str = f"Memory: {mem:.4f}" if mem != 0 else "Memory: Empty"
    
    menu_items = [
        "",
        f"  {mem_str}".ljust(78),
        "",
        "  BASIC OPERATIONS                    ADVANCED MATHEMATICS",
        "  ─────────────────                   ────────────────────",
        "  [1]  Basic Arithmetic               [11] Calculus (Derivatives/Integrals)",
        "  [2]  Scientific Functions           [12] Complex Numbers",
        "  [3]  Trigonometry                   [13] Equation Solver",
        "  [4]  Advanced Math                  [14] Number Theory (Primes, Fibonacci)",
        "  [5]  Statistics                     [15] Combinatorics (nPr, nCr)",
        "  [6]  Number Systems                 ",
        "",
        "  UTILITIES                           TOOLS",
        "  ─────────                           ─────",
        "  [7]  Memory Functions               [16] Unit Converter",
        "  [8]  Constants Library              [17] Function Plotter",
        "  [9]  Expression Evaluator           [18] Matrix Operations",
        "  [10] History Manager                [19] Settings & Themes",
        "",
        "  [20] Quick Calculator               [0] Exit",
        ""
    ]
    
    ui.print_box("MAIN MENU", menu_items, 80, 'primary')

def quick_calc():
    """Quick calculator mode"""
    print("\n" + ui.get_color('accent') + "="*80)
    print("QUICK CALCULATOR - Type expressions directly (type 'exit' to return)")
    print("="*80 + "\033[0m")
    print("\nExamples: 2+3*4, sqrt(144), sin(45), log(100), 2**10")
    
    while True:
        try:
            expr = input(f"\n{ui.get_color('secondary')}>>> \033[0m").strip()
            if expr.lower() in ['exit', 'quit', 'back']:
                break
            if not expr:
                continue
            
            result = expression.evaluate_expression(expr)
            print(f"{ui.get_color('success')}= {result}\033[0m")
            history.add_entry(expr, result)
        except Exception as e:
            print(f"{ui.get_color('error')}Error: {e}\033[0m")

def calculus_menu():
    """Calculus operations"""
    while True:
        print("\n" + "="*60)
        print("CALCULUS OPERATIONS".center(60))
        print("="*60)
        print("  1. Derivative (numerical)")
        print("  2. Definite Integral (numerical)")
        print("  3. Back")
        
        choice = input("\nSelect: ").strip()
        if choice == '3':
            break
        
        try:
            if choice == '1':
                func = input("Enter function (use 'x' as variable): ").strip()
                x = utils.get_number("Enter x value: ")
                result = advanced_calc.derivative_numerical(func, x)
                print(f"\n{ui.get_color('success')}f'({x}) = {result}\033[0m")
                history.add_entry(f"d/dx({func}) at x={x}", result)
                input("\nPress Enter...")
            
            elif choice == '2':
                func = input("Enter function (use 'x' as variable): ").strip()
                a = utils.get_number("Enter lower bound (a): ")
                b = utils.get_number("Enter upper bound (b): ")
                result = advanced_calc.integral_numerical(func, a, b)
                print(f"\n{ui.get_color('success')}∫[{a},{b}] {func} dx = {result}\033[0m")
                history.add_entry(f"Integral of {func} from {a} to {b}", result)
                input("\nPress Enter...")
        except Exception as e:
            print(f"{ui.get_color('error')}Error: {e}\033[0m")
            input("\nPress Enter...")

def complex_numbers_menu():
    """Complex number operations"""
    while True:
        print("\n" + "="*60)
        print("COMPLEX NUMBERS".center(60))
        print("="*60)
        print("  1. Add/Subtract/Multiply/Divide")
        print("  2. Magnitude & Phase")
        print("  3. Conjugate")
        print("  4. Polar to Rectangular")
        print("  5. Back")
        
        choice = input("\nSelect: ").strip()
        if choice == '5':
            break
        
        try:
            if choice == '1':
                print("\nEnter first complex number:")
                r1 = utils.get_number("  Real part: ")
                i1 = utils.get_number("  Imaginary part: ")
                z1 = complex(r1, i1)
                
                print("\nEnter second complex number:")
                r2 = utils.get_number("  Real part: ")
                i2 = utils.get_number("  Imaginary part: ")
                z2 = complex(r2, i2)
                
                print(f"\n{z1} + {z2} = {advanced_calc.complex_add(z1, z2)}")
                print(f"{z1} - {z2} = {z1 - z2}")
                print(f"{z1} * {z2} = {advanced_calc.complex_multiply(z1, z2)}")
                print(f"{z1} / {z2} = {advanced_calc.complex_divide(z1, z2)}")
                input("\nPress Enter...")
            
            elif choice == '2':
                r = utils.get_number("Real part: ")
                i = utils.get_number("Imaginary part: ")
                z = complex(r, i)
                mag = advanced_calc.complex_magnitude(z)
                phase = advanced_calc.complex_phase(z)
                print(f"\n{ui.get_color('success')}Magnitude: {mag}")
                print(f"Phase: {phase}°\033[0m")
                input("\nPress Enter...")
            
            elif choice == '3':
                r = utils.get_number("Real part: ")
                i = utils.get_number("Imaginary part: ")
                z = complex(r, i)
                conj = advanced_calc.complex_conjugate(z)
                print(f"\n{ui.get_color('success')}Conjugate: {conj}\033[0m")
                input("\nPress Enter...")
            
            elif choice == '4':
                r = utils.get_number("Magnitude (r): ")
                theta = utils.get_number("Angle (degrees): ")
                z = advanced_calc.complex_polar(r, theta)
                print(f"\n{ui.get_color('success')}Rectangular form: {z}\033[0m")
                input("\nPress Enter...")
        except Exception as e:
            print(f"{ui.get_color('error')}Error: {e}\033[0m")
            input("\nPress Enter...")

def equation_solver_menu():
    """Equation solver"""
    while True:
        print("\n" + "="*60)
        print("EQUATION SOLVER".center(60))
        print("="*60)
        print("  1. Quadratic Equation (ax² + bx + c = 0)")
        print("  2. Linear System 2x2")
        print("  3. Back")
        
        choice = input("\nSelect: ").strip()
        if choice == '3':
            break
        
        try:
            if choice == '1':
                print("\nSolve: ax² + bx + c = 0")
                a = utils.get_number("Enter a: ")
                b = utils.get_number("Enter b: ")
                c = utils.get_number("Enter c: ")
                
                x1, x2, sol_type = advanced_calc.solve_quadratic(a, b, c)
                print(f"\n{ui.get_color('success')}Solutions ({sol_type}):")
                print(f"  x₁ = {x1}")
                print(f"  x₂ = {x2}\033[0m")
                history.add_entry(f"Quadratic: {a}x²+{b}x+{c}=0", f"x1={x1}, x2={x2}")
                input("\nPress Enter...")
            
            elif choice == '2':
                print("\nSolve system:")
                print("  a₁x + b₁y = c₁")
                print("  a₂x + b₂y = c₂")
                a1 = utils.get_number("Enter a₁: ")
                b1 = utils.get_number("Enter b₁: ")
                c1 = utils.get_number("Enter c₁: ")
                a2 = utils.get_number("Enter a₂: ")
                b2 = utils.get_number("Enter b₂: ")
                c2 = utils.get_number("Enter c₂: ")
                
                x, y = advanced_calc.solve_linear_system_2x2(a1, b1, c1, a2, b2, c2)
                print(f"\n{ui.get_color('success')}Solution:")
                print(f"  x = {x}")
                print(f"  y = {y}\033[0m")
                history.add_entry(f"Linear system 2x2", f"x={x}, y={y}")
                input("\nPress Enter...")
        except Exception as e:
            print(f"{ui.get_color('error')}Error: {e}\033[0m")
            input("\nPress Enter...")

def number_theory_menu():
    """Number theory operations"""
    while True:
        print("\n" + "="*60)
        print("NUMBER THEORY".center(60))
        print("="*60)
        print("  1. Prime Check")
        print("  2. Prime Factorization")
        print("  3. Fibonacci Sequence")
        print("  4. Back")
        
        choice = input("\nSelect: ").strip()
        if choice == '4':
            break
        
        try:
            if choice == '1':
                n = int(utils.get_number("Enter number: "))
                is_prime = advanced_calc.prime_check(n)
                result = "PRIME" if is_prime else "NOT PRIME"
                print(f"\n{ui.get_color('success')}{n} is {result}\033[0m")
                input("\nPress Enter...")
            
            elif choice == '2':
                n = int(utils.get_number("Enter number: "))
                factors = advanced_calc.prime_factors(n)
                print(f"\n{ui.get_color('success')}Prime factors: {factors}")
                print(f"Factorization: {' × '.join(map(str, factors))}\033[0m")
                history.add_entry(f"Prime factors of {n}", str(factors))
                input("\nPress Enter...")
            
            elif choice == '3':
                n = int(utils.get_number("How many terms: "))
                fib = advanced_calc.fibonacci(n)
                print(f"\n{ui.get_color('success')}Fibonacci sequence ({n} terms):")
                print(f"{fib}\033[0m")
                input("\nPress Enter...")
        except Exception as e:
            print(f"{ui.get_color('error')}Error: {e}\033[0m")
            input("\nPress Enter...")

def combinatorics_menu():
    """Combinatorics operations"""
    while True:
        print("\n" + "="*60)
        print("COMBINATORICS".center(60))
        print("="*60)
        print("  1. Permutation (nPr)")
        print("  2. Combination (nCr)")
        print("  3. Binomial Coefficient")
        print("  4. Back")
        
        choice = input("\nSelect: ").strip()
        if choice == '4':
            break
        
        try:
            if choice == '1':
                n = int(utils.get_number("Enter n: "))
                r = int(utils.get_number("Enter r: "))
                result = advanced_calc.permutation(n, r)
                print(f"\n{ui.get_color('success')}P({n},{r}) = {result}\033[0m")
                history.add_entry(f"P({n},{r})", result)
                input("\nPress Enter...")
            
            elif choice in ['2', '3']:
                n = int(utils.get_number("Enter n: "))
                r = int(utils.get_number("Enter r: "))
                result = advanced_calc.combination(n, r)
                print(f"\n{ui.get_color('success')}C({n},{r}) = {result}\033[0m")
                history.add_entry(f"C({n},{r})", result)
                input("\nPress Enter...")
        except Exception as e:
            print(f"{ui.get_color('error')}Error: {e}\033[0m")
            input("\nPress Enter...")

def unit_converter_menu():
    """Unit conversion"""
    while True:
        print("\n" + "="*60)
        print("UNIT CONVERTER".center(60))
        print("="*60)
        print("  1. Length        4. Area")
        print("  2. Weight        5. Volume")
        print("  3. Temperature   6. Speed")
        print("  7. Time          8. Back")
        
        choice = input("\nSelect: ").strip()
        if choice == '8':
            break
        
        try:
            if choice == '1':
                print("\nUnits: m, km, cm, mm, mi, yd, ft, in")
                val = utils.get_number("Value: ")
                from_u = input("From unit: ").strip()
                to_u = input("To unit: ").strip()
                result = converter.convert_length(val, from_u, to_u)
                print(f"\n{ui.get_color('success')}{val} {from_u} = {result} {to_u}\033[0m")
                input("\nPress Enter...")
            
            elif choice == '2':
                print("\nUnits: kg, g, mg, lb, oz, ton")
                val = utils.get_number("Value: ")
                from_u = input("From unit: ").strip()
                to_u = input("To unit: ").strip()
                result = converter.convert_weight(val, from_u, to_u)
                print(f"\n{ui.get_color('success')}{val} {from_u} = {result} {to_u}\033[0m")
                input("\nPress Enter...")
            
            elif choice == '3':
                print("\n1. Celsius to Fahrenheit")
                print("2. Fahrenheit to Celsius")
                print("3. Celsius to Kelvin")
                print("4. Kelvin to Celsius")
                t_choice = input("Select: ").strip()
                val = utils.get_number("Value: ")
                
                if t_choice == '1':
                    result = converter.celsius_to_fahrenheit(val)
                    print(f"\n{ui.get_color('success')}{val}°C = {result}°F\033[0m")
                elif t_choice == '2':
                    result = converter.fahrenheit_to_celsius(val)
                    print(f"\n{ui.get_color('success')}{val}°F = {result}°C\033[0m")
                elif t_choice == '3':
                    result = converter.celsius_to_kelvin(val)
                    print(f"\n{ui.get_color('success')}{val}°C = {result}K\033[0m")
                elif t_choice == '4':
                    result = converter.kelvin_to_celsius(val)
                    print(f"\n{ui.get_color('success')}{val}K = {result}°C\033[0m")
                input("\nPress Enter...")
        except Exception as e:
            print(f"{ui.get_color('error')}Error: {e}\033[0m")
            input("\nPress Enter...")

def function_plotter_menu():
    """Function plotting"""
    while True:
        print("\n" + "="*60)
        print("FUNCTION PLOTTER".center(60))
        print("="*60)
        print("  1. Plot Function")
        print("  2. Plot Data Points")
        print("  3. Back")
        
        choice = input("\nSelect: ").strip()
        if choice == '3':
            break
        
        try:
            if choice == '1':
                func = input("Enter function (use 'x'): ").strip()
                x_min = utils.get_number("X min: ")
                x_max = utils.get_number("X max: ")
                plot = graphing.plot_function(func, x_min, x_max)
                print(plot)
                input("\nPress Enter...")
            
            elif choice == '2':
                x_data = utils.get_number_list("Enter x values (comma-separated): ")
                y_data = utils.get_number_list("Enter y values (comma-separated): ")
                plot = graphing.plot_data(x_data, y_data)
                print(plot)
                input("\nPress Enter...")
        except Exception as e:
            print(f"{ui.get_color('error')}Error: {e}\033[0m")
            input("\nPress Enter...")

def settings_menu():
    """Settings and themes"""
    while True:
        print("\n" + "="*60)
        print("SETTINGS & THEMES".center(60))
        print("="*60)
        print(f"  Current Theme: {ui.current_theme}")
        print("\n  1. Default Theme")
        print("  2. Dark Theme")
        print("  3. Matrix Theme")
        print("  4. Back")
        
        choice = input("\nSelect: ").strip()
        if choice == '4':
            break
        
        if choice == '1':
            ui.set_theme('default')
            print(f"{ui.get_color('success')}Theme changed to Default\033[0m")
        elif choice == '2':
            ui.set_theme('dark')
            print(f"{ui.get_color('success')}Theme changed to Dark\033[0m")
        elif choice == '3':
            ui.set_theme('matrix')
            print(f"{ui.get_color('success')}Theme changed to Matrix\033[0m")
        input("\nPress Enter...")

def history_manager():
    """Enhanced history manager"""
    while True:
        print("\n" + "="*60)
        print("HISTORY MANAGER".center(60))
        print("="*60)
        print("  1. View History")
        print("  2. Export to File")
        print("  3. Clear History")
        print("  4. Back")
        
        choice = input("\nSelect: ").strip()
        if choice == '4':
            break
        
        if choice == '1':
            history.display_history()
        elif choice == '2':
            try:
                filename = history.export_history()
                print(f"{ui.get_color('success')}Exported to {filename}\033[0m")
                input("\nPress Enter...")
            except Exception as e:
                print(f"{ui.get_color('error')}Error: {e}\033[0m")
                input("\nPress Enter...")
        elif choice == '3':
            confirm = input("Clear all history? (yes/no): ").strip().lower()
            if confirm == 'yes':
                history.clear_history()
                print(f"{ui.get_color('success')}History cleared\033[0m")
            input("\nPress Enter...")

def run_basic_menu():
    """Run basic operations from original"""
    from main_backup import basic_operations_menu
    basic_operations_menu()

def run_scientific_menu():
    from main_backup import scientific_operations_menu
    scientific_operations_menu()

def run_trig_menu():
    from main_backup import trigonometric_operations_menu
    trigonometric_operations_menu()

def run_advanced_menu():
    from main_backup import advanced_operations_menu
    advanced_operations_menu()

def run_stats_menu():
    from main_backup import statistics_menu
    statistics_menu()

def run_number_systems_menu():
    from main_backup import number_systems_menu
    number_systems_menu()

def run_memory_menu():
    from main_backup import memory_menu
    memory_menu()

def run_constants_menu():
    from main_backup import constants_menu
    constants_menu()

def run_expression_menu():
    from main_backup import expression_evaluator_menu
    expression_evaluator_menu()

def run_matrix_menu():
    from main_backup import matrix_operations_menu
    matrix_operations_menu()

def main():
    """Main application loop"""
    ui.loading_animation("Initializing Calculator", 1.5)
    
    while True:
        main_menu()
        choice = input(f"\n{ui.get_color('secondary')}Select option: \033[0m").strip()
        
        try:
            if choice == '0':
                print(f"\n{ui.get_color('success')}Thank you for using Scientific Calculator v4.0!\033[0m\n")
                break
            elif choice == '1':
                run_basic_menu()
            elif choice == '2':
                run_scientific_menu()
            elif choice == '3':
                run_trig_menu()
            elif choice == '4':
                run_advanced_menu()
            elif choice == '5':
                run_stats_menu()
            elif choice == '6':
                run_number_systems_menu()
            elif choice == '7':
                run_memory_menu()
            elif choice == '8':
                run_constants_menu()
            elif choice == '9':
                run_expression_menu()
            elif choice == '10':
                history_manager()
            elif choice == '11':
                calculus_menu()
            elif choice == '12':
                complex_numbers_menu()
            elif choice == '13':
                equation_solver_menu()
            elif choice == '14':
                number_theory_menu()
            elif choice == '15':
                combinatorics_menu()
            elif choice == '16':
                unit_converter_menu()
            elif choice == '17':
                function_plotter_menu()
            elif choice == '18':
                run_matrix_menu()
            elif choice == '19':
                settings_menu()
            elif choice == '20':
                quick_calc()
            else:
                print(f"{ui.get_color('error')}Invalid option\033[0m")
                input("\nPress Enter...")
        except KeyboardInterrupt:
            print(f"\n{ui.get_color('error')}Operation cancelled\033[0m")
            input("\nPress Enter...")
        except Exception as e:
            print(f"{ui.get_color('error')}Error: {e}\033[0m")
            input("\nPress Enter...")

if __name__ == "__main__":
    main()
