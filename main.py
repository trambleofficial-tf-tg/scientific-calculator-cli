"""
Scientific Calculator - Main Controller
Enhanced menu-driven CLI calculator with history and advanced features
"""

from calculator import basic, scientific, utils, advanced, history
import os

def clear_console():
    """Clear console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    """Display enhanced header"""
    print("\n" + "╔" + "═"*58 + "╗")
    print("║" + " "*15 + "🔬 SCIENTIFIC CALCULATOR 🔬" + " "*15 + "║")
    print("║" + " "*18 + "Enhanced Edition v2.0" + " "*19 + "║")
    print("╚" + "═"*58 + "╝")

def display_main_menu():
    """Display the enhanced main menu options"""
    display_header()
    print("\n┌" + "─"*58 + "┐")
    print("│" + " "*20 + "MAIN MENU" + " "*29 + "│")
    print("├" + "─"*58 + "┤")
    print("│  1. ➕ Basic Operations        │  5. 📊 Statistics          │")
    print("│  2. 🔬 Scientific Operations   │  6. 🔢 Number Systems      │")
    print("│  3. 📐 Trigonometric Ops       │  7. 📜 View History        │")
    print("│  4. 🧮 Advanced Operations     │  8. 🗑️  Clear History      │")
    print("│                                │  9. ❌ Exit                │")
    print("└" + "─"*58 + "┘")

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
        print("│  1. 📈 Mean (Average)    │  4. 📉 Minimum              │")
        print("│  2. 🎯 Median            │  5. 📊 Range                │")
        print("│  3. 📊 Maximum           │  6. ⬅️  Back to Main Menu   │")
        print("└" + "─"*58 + "┘")
        
        choice = input("\n👉 Select operation (1-6): ").strip()
        
        if choice == '6':
            break
        
        if choice not in ['1', '2', '3', '4', '5']:
            utils.show_error("Invalid choice. Please select 1-6.")
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

def main():
    """Main controller function"""
    clear_console()
    print("\n" + "═"*60)
    print("  Welcome to Scientific Calculator - Enhanced Edition! 🎉")
    print("═"*60)
    
    while True:
        display_main_menu()
        choice = input("\n👉 Select an option (1-9): ").strip()
        
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
            history.display_history()
        elif choice == '8':
            history.clear_history()
            utils.show_success("History cleared successfully!")
        elif choice == '9':
            print("\n" + "═"*60)
            print("  Thank you for using Scientific Calculator! 👋")
            print("  Goodbye and have a great day! 🌟")
            print("═"*60 + "\n")
            break
        else:
            utils.show_error("Invalid choice. Please select 1-9.")

if __name__ == "__main__":
    main()
