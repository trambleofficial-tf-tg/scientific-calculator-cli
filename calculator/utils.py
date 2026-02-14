"""Utility functions for input handling and display"""
import sys

def get_number(prompt):
    """Get and validate numeric input from user"""
    while True:
        try:
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
    
    print(f"│  Result: {result_str:<48} │")
    print("└" + "─"*58 + "┘")
    input("\n⏎ Press Enter to continue...")

def show_error(message):
    """Display error message in formatted manner"""
    print(f"\n❌ ERROR: {message}\n")
    input("⏎ Press Enter to continue...")

def show_success(message):
    """Display success message"""
    print(f"\n✅ {message}\n")
    input("⏎ Press Enter to continue...")

def show_info(message):
    """Display info message"""
    print(f"\nℹ️  {message}\n")
