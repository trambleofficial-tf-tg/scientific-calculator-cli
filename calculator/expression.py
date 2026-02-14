"""Expression evaluator module for direct math expressions"""
import math
import re

def evaluate_expression(expression):
    """
    Safely evaluate mathematical expressions
    Supports: +, -, *, /, **, (), sqrt, sin, cos, tan, log, ln, abs, pi, e
    """
    # Replace common math functions and constants
    expression = expression.replace('^', '**')
    expression = expression.replace('π', str(math.pi))
    expression = expression.replace('pi', str(math.pi))
    expression = expression.replace('e', str(math.e), 1)  # Only first occurrence
    
    # Create safe namespace with math functions
    safe_dict = {
        'sqrt': math.sqrt,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'asin': math.asin,
        'acos': math.acos,
        'atan': math.atan,
        'log': math.log10,
        'ln': math.log,
        'log10': math.log10,
        'exp': math.exp,
        'abs': abs,
        'pow': pow,
        'factorial': math.factorial,
        'ceil': math.ceil,
        'floor': math.floor,
        'pi': math.pi,
        'e': math.e,
        '__builtins__': {}
    }
    
    try:
        # Validate expression (only allow safe characters)
        if not re.match(r'^[0-9+\-*/().,\s\w]+$', expression):
            raise ValueError("Invalid characters in expression")
        
        result = eval(expression, safe_dict, {})
        return result
    except ZeroDivisionError:
        raise ValueError("Division by zero")
    except SyntaxError:
        raise ValueError("Invalid expression syntax")
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {str(e)}")
