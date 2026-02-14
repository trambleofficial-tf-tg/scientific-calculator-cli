"""Utility functions for input handling and display"""
import sys
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    COLORS_ENABLED = True
except ImportError:
    COLORS_ENABLED = False
    class Fore:
        RED = GREEN = YELLOW = CYAN = MAGENTA = BLUE = WHITE = RESET = ''
    class Style:
        BRIGHT = RESET_ALL = ''

def get_number(prompt):
    """Get and validate numeric input from user"""
    while True:
        try:
            if COLORS_ENABLED:
                return float(input(f"{Fore.CYAN}✏️  {prompt}{Style.RESET_ALL}"))
            else:
                return float(input(f"✏️  {prompt}"))
        except ValueError:
            show_error("Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n\n⚠️  Operation cancelled by user.")
            sys.exit(0)

def get_number_list(prompt):
    """Get and validate a list of numbers from user"""
    while True:
        try:
            if COLORS_ENABLED:
                user_input = input(f"{Fore.CYAN}✏️  {prompt}{Style.RESET_ALL}")
            else:
                user_input = input(f"✏️  {prompt}")
            numbers = [float(x.strip()) for x in user_input.split(',')]
            if len(numbers) == 0:
                raise ValueError("Please enter at least one number")
            return numbers
        except ValueError as e:
            show_error(f"Invalid input: {str(e)}")
        except KeyboardInterrupt:
            print("\n\n⚠️  Operation cancelled by user.")
            sys.exit(0)

def display_result(operation, result):
    """Display calculation result in formatted manner"""
    if COLORS_ENABLED:
        print(f"\n{Fore.GREEN}┌" + "─"*58 + "┐")
        print(f"│{Style.BRIGHT}" + " "*20 + "✨ RESULT ✨" + " "*25 + f"{Style.RESET_ALL}{Fore.GREEN}│")
        print(f"├" + "─"*58 + "┤")
        print(f"│  {Fore.YELLOW}Operation:{Style.RESET_ALL} {operation:<45} {Fore.GREEN}│")
    else:
        print(f"\n┌" + "─"*58 + "┐")
        print(f"│" + " "*20 + "✨ RESULT ✨" + " "*25 + "│")
        print(f"├" + "─"*58 + "┤")
        print(f"│  Operation: {operation:<45} │")
    
    # Format result based on type
    if isinstance(result, float):
        if result.is_integer():
            result_str = f"{int(result)}"
        else:
            result_str = f"{result:.6f}".rstrip('0').rstrip('.')
    else:
        result_str = str(result)
    
    if COLORS_ENABLED:
        print(f"│  {Fore.YELLOW}Result:{Style.RESET_ALL} {Fore.CYAN}{Style.BRIGHT}{result_str:<48}{Style.RESET_ALL} {Fore.GREEN}│")
        print("└" + "─"*58 + f"┘{Style.RESET_ALL}")
    else:
        print(f"│  Result: {result_str:<48} │")
        print("└" + "─"*58 + "┘")
    input("\n⏎ Press Enter to continue...")

def show_error(message):
    """Display error message in formatted manner"""
    if COLORS_ENABLED:
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ ERROR: {message}{Style.RESET_ALL}\n")
    else:
        print(f"\n❌ ERROR: {message}\n")
    input("⏎ Press Enter to continue...")

def show_success(message):
    """Display success message"""
    if COLORS_ENABLED:
        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ {message}{Style.RESET_ALL}\n")
    else:
        print(f"\n✅ {message}\n")
    input("⏎ Press Enter to continue...")

def show_info(message):
    """Display info message"""
    if COLORS_ENABLED:
        print(f"\n{Fore.CYAN}ℹ️  {message}{Style.RESET_ALL}\n")
    else:
        print(f"\nℹ️  {message}\n")

def get_matrix_2x2(prompt):
    """Get 2x2 matrix input from user"""
    print(f"\n{prompt}")
    matrix = []
    for i in range(2):
        while True:
            try:
                if COLORS_ENABLED:
                    row_input = input(f"{Fore.CYAN}Row {i+1} (space-separated): {Style.RESET_ALL}")
                else:
                    row_input = input(f"Row {i+1} (space-separated): ")
                row = [float(x.strip()) for x in row_input.split()]
                if len(row) != 2:
                    raise ValueError("Each row must have exactly 2 numbers")
                matrix.append(row)
                break
            except ValueError as e:
                show_error(str(e))
    return matrix
