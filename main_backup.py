"""
Scientific Calculator - Main Controller
Enhanced Edition v3.0 with Expression Evaluator, Memory, Constants & More
"""

from calculator import basic, scientific, utils, advanced, history, memory, constants, expression
import os

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLORS = True
except ImportError:
    COLORS = False
    class Fore:
        RED = GREEN = YELLOW = CYAN = MAGENTA = BLUE = WHITE = LIGHTBLUE_EX = RESET = ''
    class Style:
        BRIGHT = RESET_ALL = ''

def clear_console():
    """Clear console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    """Display enhanced header"""
    if COLORS:
        print(f"\n{Fore.CYAN}{Style.BRIGHT}" + "+" + "-"*68 + "+")
        print(f"|{Fore.YELLOW}" + " "*15 + "SCIENTIFIC CALCULATOR" + " "*20 + f"{Fore.CYAN}|")
        print(f"|{Fore.GREEN}" + " "*20 + "Enhanced Edition v3.0" + " "*21 + f"{Fore.CYAN}|")
        print("+" + "-"*68 + f"+{Style.RESET_ALL}")
    else:
        print("\n+" + "-"*68 + "+")
        print("|" + " "*15 + "SCIENTIFIC CALCULATOR" + " "*20 + "|")
        print("|" + " "*20 + "Enhanced Edition v3.0" + " "*21 + "|")
        print("+" + "-"*68 + "+")

def display_main_menu():
    """Display the enhanced main menu options"""
    display_header()
    mem_val = memory.memory_recall()
    mem_display = f"M: {mem_val:.2f}" if mem_val != 0 else "M: Empty"
    
    if COLORS:
        print(f"\n{Fore.LIGHTBLUE_EX}+" + "-"*68 + "+")
        print(f"|{Style.BRIGHT}" + " "*26 + "MAIN MENU" + " "*33 + f"{Style.RESET_ALL}{Fore.LIGHTBLUE_EX}|")
        print(f"|{Fore.YELLOW}  Memory: {mem_display:<56}{Fore.LIGHTBLUE_EX}|")
        print("+" + "-"*68 + "+")
        print(f"|  {Fore.GREEN}1. Basic Operations        |  7. Memory Functions       {Fore.LIGHTBLUE_EX}|")
        print(f"|  {Fore.GREEN}2. Scientific Operations   |  8. Constants Library      {Fore.LIGHTBLUE_EX}|")
        print(f"|  {Fore.GREEN}3. Trigonometric Ops       |  9. Expression Evaluator   {Fore.LIGHTBLUE_EX}|")
        print(f"|  {Fore.GREEN}4. Advanced Operations     | 10. Matrix Operations      {Fore.LIGHTBLUE_EX}|")
        print(f"|  {Fore.GREEN}5. Statistics              | 11. View History           {Fore.LIGHTBLUE_EX}|")
        print(f"|  {Fore.GREEN}6. Number Systems          | 12. Export History         {Fore.LIGHTBLUE_EX}|")
        print(f"|  {Fore.GREEN}                            | 13. Clear History          {Fore.LIGHTBLUE_EX}|")
        print(f"|  {Fore.GREEN}                            | 14. Exit                   {Fore.LIGHTBLUE_EX}|")
        print("+" + "-"*68 + f"+{Style.RESET_ALL}")
    else:
        print("\n+" + "-"*68 + "+")
        print("|" + " "*26 + "MAIN MENU" + " "*33 + "|")
        print(f"|  Memory: {mem_display:<56}|")
        print("+" + "-"*68 + "+")
        print("|  1. Basic Operations        |  7. Memory Functions       |")
        print("|  2. Scientific Operations   |  8. Constants Library      |")
        print("|  3. Trigonometric Ops       |  9. Expression Evaluator   |")
        print("|  4. Advanced Operations     | 10. Matrix Operations      |")
        print("|  5. Statistics              | 11. View History           |")
        print("|  6. Number Systems          | 12. Export History         |")
        print("|                              | 13. Clear History          |")
        print("|                              | 14. Exit                   |")
        print("+" + "-"*68 + "+")

def basic_operations_menu():
    """Handle basic arithmetic operations"""
    while True:
        print("\n┌" + "─"*58 + "┐")
        print("│" + " "*18 + "➕ BASIC OPERATIONS" + " "*21 + "│")
        print("├" + "─"*58 + "┤")
        print("│  1. ➕ Addition          │  4. ➗ Division              │")
        print("│  2. ➖ Subtraction       │  5. 📊 Modulo               │")
        print("│  3. ✖️  Multiplication   │  6. ⬅️  Back to Main Menu   │")
        print("└" + "─"*58 + "┘")
        
        choice = input("\n👉 Select operation (1-6): ").strip()
        
        if choice == '6':
            break
        
        if choice not in ['1', '2', '3', '4', '5']:
            utils.show_error("Invalid choice. Please select 1-6.")
            continue
        
        x = utils.get_number("Enter first number: ")
        y = utils.get_number("Enter second number: ")
        
        try:
            if choice == '1':
                result = basic.add(x, y)
                operation = f"{x} + {y}"
            elif choice == '2':
                result = basic.subtract(x, y)
                operation = f"{x} - {y}"
            elif choice == '3':
                result = basic.multiply(x, y)
                operation = f"{x} × {y}"
            elif choice == '4':
                result = basic.divide(x, y)
                operation = f"{x} ÷ {y}"
            elif choice == '5':
                result = basic.modulo(x, y)
                operation = f"{x} mod {y}"
            
            utils.display_result(operation, result)
            history.add_entry(operation, result)
        except ValueError as e:
            utils.show_error(str(e))

def scientific_operations_menu():
    """Handle scientific operations"""
    while True:
        print("\n┌" + "─"*58 + "┐")
        print("│" + " "*15 + "🔬 SCIENTIFIC OPERATIONS" + " "*19 + "│")
        print("├" + "─"*58 + "┤")
        print("│  1. 🔺 Power (x^y)       │  5. 📐 Cube Root            │")
        print("│  2. √  Square Root       │  6. 🔢 Absolute Value       │")
        print("│  3. 📊 Logarithm (any)   │  7. ⚡ Exponential (e^x)    │")
        print("│  4. 📈 Natural Log (ln)  │  8. ⬅️  Back to Main Menu   │")
        print("└" + "─"*58 + "┘")
        
        choice = input("\n👉 Select operation (1-8): ").strip()
        
        if choice == '8':
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6', '7']:
            utils.show_error("Invalid choice. Please select 1-8.")
            continue
        
        try:
            if choice == '1':
                base = utils.get_number("Enter base: ")
                exponent = utils.get_number("Enter exponent: ")
                result = scientific.power(base, exponent)
                operation = f"{base}^{exponent}"
            elif choice == '2':
                x = utils.get_number("Enter number: ")
                result = scientific.square_root(x)
                operation = f"√{x}"
            elif choice == '3':
                x = utils.get_number("Enter number: ")
                base = utils.get_number("Enter logarithm base: ")
                result = scientific.logarithm(x, base)
                operation = f"log_{base}({x})"
            elif choice == '4':
                x = utils.get_number("Enter number: ")
                result = scientific.natural_log(x)
                operation = f"ln({x})"
            elif choice == '5':
                x = utils.get_number("Enter number: ")
                result = scientific.cube_root(x)
                operation = f"∛{x}"
            elif choice == '6':
                x = utils.get_number("Enter number: ")
                result = scientific.absolute_value(x)
                operation = f"|{x}|"
            elif choice == '7':
                x = utils.get_number("Enter exponent: ")
                result = scientific.exponential(x)
                operation = f"e^{x}"
            
            utils.display_result(operation, result)
            history.add_entry(operation, result)
        except ValueError as e:
            utils.show_error(str(e))

def trigonometric_operations_menu():
    """Handle trigonometric operations"""
    while True:
        print("\n┌" + "─"*58 + "┐")
        print("│" + " "*13 + "📐 TRIGONOMETRIC OPERATIONS" + " "*18 + "│")
        print("├" + "─"*58 + "┤")
        print("│  1. 📊 Sine (sin)        │  5. 🔄 Arcsine (asin)       │")
        print("│  2. 📈 Cosine (cos)      │  6. 🔄 Arccosine (acos)     │")
        print("│  3. 📉 Tangent (tan)     │  7. 🔄 Arctangent (atan)    │")
        print("│  4. 🔢 Degrees/Radians   │  8. ⬅️  Back to Main Menu   │")
        print("└" + "─"*58 + "┘")
        
        choice = input("\n👉 Select operation (1-8): ").strip()
        
        if choice == '8':
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6', '7']:
            utils.show_error("Invalid choice. Please select 1-8.")
            continue
        
        try:
            if choice == '4':
                print("\n1. Degrees to Radians")
                print("2. Radians to Degrees")
                conv_choice = input("Select (1-2): ").strip()
                angle = utils.get_number("Enter angle: ")
                if conv_choice == '1':
                    result = scientific.deg_to_rad(angle)
                    operation = f"{angle}° to radians"
                else:
                    result = scientific.rad_to_deg(angle)
                    operation = f"{angle} rad to degrees"
            else:
                angle = utils.get_number("Enter angle in degrees: ")
                if choice == '1':
                    result = scientific.sin(angle)
                    operation = f"sin({angle}°)"
                elif choice == '2':
                    result = scientific.cos(angle)
                    operation = f"cos({angle}°)"
                elif choice == '3':
                    result = scientific.tan(angle)
                    operation = f"tan({angle}°)"
                elif choice == '5':
                    result = scientific.asin(angle)
                    operation = f"asin({angle})"
                elif choice == '6':
                    result = scientific.acos(angle)
                    operation = f"acos({angle})"
                elif choice == '7':
                    result = scientific.atan(angle)
                    operation = f"atan({angle})"
            
            utils.display_result(operation, result)
            history.add_entry(operation, result)
        except ValueError as e:
            utils.show_error(str(e))

def advanced_operations_menu():
    """Handle advanced mathematical operations"""
    while True:
        print("\n┌" + "─"*58 + "┐")
        print("│" + " "*15 + "🧮 ADVANCED OPERATIONS" + " "*21 + "│")
        print("├" + "─"*58 + "┤")
        print("│  1. 🔢 Factorial         │  4. 🎲 GCD                  │")
        print("│  2. 📊 Percentage        │  5. 🎯 LCM                  │")
        print("│  3. 🔺 nth Root          │  6. ⬅️  Back to Main Menu   │")
        print("└" + "─"*58 + "┘")
        
        choice = input("\n👉 Select operation (1-6): ").strip()
        
        if choice == '6':
            break
        
        if choice not in ['1', '2', '3', '4', '5']:
            utils.show_error("Invalid choice. Please select 1-6.")
            continue
        
        try:
            if choice == '1':
                n = int(utils.get_number("Enter number: "))
                result = advanced.factorial(n)
                operation = f"{n}!"
            elif choice == '2':
                value = utils.get_number("Enter value: ")
                total = utils.get_number("Enter total: ")
                result = advanced.percentage(value, total)
                operation = f"{value}/{total} as %"
            elif choice == '3':
                number = utils.get_number("Enter number: ")
                n = int(utils.get_number("Enter root degree: "))
                result = advanced.nth_root(number, n)
                operation = f"{n}√{number}"
            elif choice == '4':
                a = int(utils.get_number("Enter first number: "))
                b = int(utils.get_number("Enter second number: "))
                result = advanced.gcd(a, b)
                operation = f"GCD({a}, {b})"
            elif choice == '5':
                a = int(utils.get_number("Enter first number: "))
                b = int(utils.get_number("Enter second number: "))
                result = advanced.lcm(a, b)
                operation = f"LCM({a}, {b})"
            
            utils.display_result(operation, result)
            history.add_entry(operation, result)
        except ValueError as e:
            utils.show_error(str(e))

def statistics_menu():
    """Handle statistical operations"""
    while True:
        print("\n┌" + "─"*58 + "┐")
        print("│" + " "*19 + "📊 STATISTICS" + " "*26 + "│")
        print("├" + "─"*58 + "┤")
        print("│  1. 📈 Mean (Average)    │  5. 📊 Range                │")
        print("│  2. 🎯 Median            │  6. 📉 Std Deviation        │")
        print("│  3. 📊 Maximum           │  7. 📊 Variance             │")
        print("│  4. 📉 Minimum           │  8. ⬅️  Back to Main Menu   │")
        print("└" + "─"*58 + "┘")
        
        choice = input("\n👉 Select operation (1-8): ").strip()
        
        if choice == '8':
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6', '7']:
            utils.show_error("Invalid choice. Please select 1-8.")
            continue
        
        try:
            numbers = utils.get_number_list("Enter numbers (comma-separated): ")
            
            if choice == '1':
                result = advanced.mean(numbers)
                operation = f"Mean of {len(numbers)} numbers"
            elif choice == '2':
                result = advanced.median(numbers)
                operation = f"Median of {len(numbers)} numbers"
            elif choice == '3':
                result = max(numbers)
                operation = f"Maximum of {len(numbers)} numbers"
            elif choice == '4':
                result = min(numbers)
                operation = f"Minimum of {len(numbers)} numbers"
            elif choice == '5':
                result = max(numbers) - min(numbers)
                operation = f"Range of {len(numbers)} numbers"
            elif choice == '6':
                result = advanced.standard_deviation(numbers)
                operation = f"Std Dev of {len(numbers)} numbers"
            elif choice == '7':
                result = advanced.variance(numbers)
                operation = f"Variance of {len(numbers)} numbers"
            
            utils.display_result(operation, result)
            history.add_entry(operation, result)
        except ValueError as e:
            utils.show_error(str(e))

def number_systems_menu():
    """Handle number system conversions"""
    while True:
        print("\n┌" + "─"*58 + "┐")
        print("│" + " "*18 + "🔢 NUMBER SYSTEMS" + " "*23 + "│")
        print("├" + "─"*58 + "┤")
        print("│  1. 🔟 Decimal to Binary    │  4. 🔢 Octal to Decimal    │")
        print("│  2. 🔢 Binary to Decimal    │  5. 🔠 Decimal to Hex      │")
        print("│  3. 🔟 Decimal to Octal     │  6. 🔢 Hex to Decimal      │")
        print("│  7. ⬅️  Back to Main Menu                                │")
        print("└" + "─"*58 + "┘")
        
        choice = input("\n👉 Select operation (1-7): ").strip()
        
        if choice == '7':
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6']:
            utils.show_error("Invalid choice. Please select 1-7.")
            continue
        
        try:
            if choice == '1':
                num = int(utils.get_number("Enter decimal number: "))
                result = advanced.dec_to_bin(num)
                operation = f"Dec {num} to Binary"
            elif choice == '2':
                num = input("Enter binary number: ").strip()
                result = advanced.bin_to_dec(num)
                operation = f"Binary {num} to Dec"
            elif choice == '3':
                num = int(utils.get_number("Enter decimal number: "))
                result = advanced.dec_to_oct(num)
                operation = f"Dec {num} to Octal"
            elif choice == '4':
                num = input("Enter octal number: ").strip()
                result = advanced.oct_to_dec(num)
                operation = f"Octal {num} to Dec"
            elif choice == '5':
                num = int(utils.get_number("Enter decimal number: "))
                result = advanced.dec_to_hex(num)
                operation = f"Dec {num} to Hex"
            elif choice == '6':
                num = input("Enter hexadecimal number: ").strip()
                result = advanced.hex_to_dec(num)
                operation = f"Hex {num} to Dec"
            
            utils.display_result(operation, result)
            history.add_entry(operation, result)
        except ValueError as e:
            utils.show_error(str(e))

def memory_menu():
    """Handle memory operations"""
    while True:
        mem_val = memory.memory_recall()
        print("\n┌" + "─"*58 + "┐")
        print("│" + " "*17 + "🧠 MEMORY FUNCTIONS" + " "*22 + "│")
        print("├" + "─"*58 + "┤")
        print(f"│  Current Memory: {mem_val:<40} │")
        print("├" + "─"*58 + "┤")
        print("│  1. M+ (Add to Memory)       │  4. MC (Clear Memory)       │")
        print("│  2. M- (Subtract from Mem)   │  5. MS (Store in Memory)    │")
        print("│  3. MR (Recall Memory)       │  6. ⬅️  Back to Main Menu   │")
        print("└" + "─"*58 + "┘")
        
        choice = input("\n👉 Select operation (1-6): ").strip()
        
        if choice == '6':
            break
        
        if choice not in ['1', '2', '3', '4', '5']:
            utils.show_error("Invalid choice. Please select 1-6.")
            continue
        
        try:
            if choice == '1':
                value = utils.get_number("Enter value to add: ")
                result = memory.memory_add(value)
                utils.show_success(f"Added {value} to memory. New value: {result}")
            elif choice == '2':
                value = utils.get_number("Enter value to subtract: ")
                result = memory.memory_subtract(value)
                utils.show_success(f"Subtracted {value} from memory. New value: {result}")
            elif choice == '3':
                result = memory.memory_recall()
                utils.show_info(f"Memory value: {result}")
            elif choice == '4':
                memory.memory_clear()
                utils.show_success("Memory cleared!")
            elif choice == '5':
                value = utils.get_number("Enter value to store: ")
                result = memory.memory_store(value)
                utils.show_success(f"Stored {value} in memory")
        except ValueError as e:
            utils.show_error(str(e))

def constants_menu():
    """Display and use mathematical constants"""
    const_list = constants.list_constants()
    
    print("\n┌" + "─"*68 + "┐")
    print("│" + " "*22 + "🔢 CONSTANTS LIBRARY" + " "*27 + "│")
    print("├" + "─"*68 + "┤")
    print("│  Mathematical Constants:                                       │")
    for name, value in const_list['Mathematical'].items():
        print(f"│    {name:<30} = {value:<30.10g} │")
    print("│                                                                │")
    print("│  Physical Constants:                                           │")
    for name, value in const_list['Physical'].items():
        print(f"│    {name:<30} = {value:<30.10g} │")
    print("└" + "─"*68 + "┘")
    input("\n⏎ Press Enter to continue...")

def expression_evaluator_menu():
    """Handle direct expression evaluation"""
    print("\n┌" + "─"*68 + "┐")
    print("│" + " "*20 + "🧮 EXPRESSION EVALUATOR" + " "*25 + "│")
    print("├" + "─"*68 + "┤")
    print("│  Enter mathematical expressions directly!                     │")
    print("│  Examples: 2+3*4, sqrt(16), sin(30), log(100), 2**8           │")
    print("│  Functions: sqrt, sin, cos, tan, log, ln, abs, factorial      │")
    print("│  Constants: pi, e                                             │")
    print("│  Type 'back' to return to main menu                           │")
    print("└" + "─"*68 + "┘")
    
    while True:
        expr = input("\n📝 Enter expression: ").strip()
        
        if expr.lower() == 'back':
            break
        
        if not expr:
            continue
        
        try:
            result = expression.evaluate_expression(expr)
            utils.display_result(expr, result)
            history.add_entry(expr, result)
        except ValueError as e:
            utils.show_error(str(e))

def matrix_operations_menu():
    """Handle matrix operations"""
    while True:
        print("\n┌" + "─"*58 + "┐")
        print("│" + " "*16 + "📊 MATRIX OPERATIONS" + " "*23 + "│")
        print("│" + " "*19 + "(2x2 Matrices)" + " "*26 + "│")
        print("├" + "─"*58 + "┤")
        print("│  1. ➕ Matrix Addition       │  3. 🔢 Determinant          │")
        print("│  2. ✖️  Matrix Multiplication │  4. ⬅️  Back to Main Menu   │")
        print("└" + "─"*58 + "┘")
        
        choice = input("\n👉 Select operation (1-4): ").strip()
        
        if choice == '4':
            break
        
        if choice not in ['1', '2', '3']:
            utils.show_error("Invalid choice. Please select 1-4.")
            continue
        
        try:
            if choice in ['1', '2']:
                m1 = utils.get_matrix_2x2("Enter first matrix:")
                m2 = utils.get_matrix_2x2("Enter second matrix:")
                
                if choice == '1':
                    result = advanced.matrix_add(m1, m2)
                    operation = "Matrix Addition"
                else:
                    result = advanced.matrix_multiply(m1, m2)
                    operation = "Matrix Multiplication"
                
                print(f"\n✨ Result:")
                print(f"  [{result[0][0]:.2f}  {result[0][1]:.2f}]")
                print(f"  [{result[1][0]:.2f}  {result[1][1]:.2f}]")
                history.add_entry(operation, str(result))
                input("\n⏎ Press Enter to continue...")
            
            elif choice == '3':
                m = utils.get_matrix_2x2("Enter matrix:")
                result = advanced.matrix_determinant(m)
                operation = "Matrix Determinant"
                utils.display_result(operation, result)
                history.add_entry(operation, result)
        
        except ValueError as e:
            utils.show_error(str(e))

def main():
    """Main controller function"""
    clear_console()
    if COLORS:
        print(f"\n{Fore.CYAN}{Style.BRIGHT}" + "="*70)
        print(f"{Fore.YELLOW}  Welcome to Scientific Calculator - Enhanced Edition v3.0! " + "\U0001F389")
        print(f"{Fore.CYAN}" + "="*70 + f"{Style.RESET_ALL}")
    else:
        print("\n" + "="*70)
        print("  Welcome to Scientific Calculator - Enhanced Edition v3.0! " + "\U0001F389")
        print("="*70)
    
    while True:
        display_main_menu()
        choice = input("\n👉 Select an option (1-14): ").strip()
        
        if choice == '1':
            basic_operations_menu()
        elif choice == '2':
            scientific_operations_menu()
        elif choice == '3':
            trigonometric_operations_menu()
        elif choice == '4':
            advanced_operations_menu()
        elif choice == '5':
            statistics_menu()
        elif choice == '6':
            number_systems_menu()
        elif choice == '7':
            memory_menu()
        elif choice == '8':
            constants_menu()
        elif choice == '9':
            expression_evaluator_menu()
        elif choice == '10':
            matrix_operations_menu()
        elif choice == '11':
            history.display_history()
        elif choice == '12':
            try:
                filename = history.export_history()
                utils.show_success(f"History exported to {filename}")
            except ValueError as e:
                utils.show_error(str(e))
        elif choice == '13':
            history.clear_history()
            utils.show_success("History cleared successfully!")
        elif choice == '14':
            if COLORS:
                print(f"\n{Fore.CYAN}{Style.BRIGHT}" + "="*70)
                print(f"{Fore.YELLOW}  Thank you for using Scientific Calculator! " + "\U0001F44B")
                print(f"{Fore.GREEN}  Goodbye and have a great day! " + "\U0001F31F")
                print(f"{Fore.CYAN}" + "="*70 + f"{Style.RESET_ALL}\n")
            else:
                print("\n" + "="*70)
                print("  Thank you for using Scientific Calculator! " + "\U0001F44B")
                print("  Goodbye and have a great day! " + "\U0001F31F")
                print("="*70 + "\n")
            break
        else:
            utils.show_error("Invalid choice. Please select 1-14.")

if __name__ == "__main__":
    main()
