import operator
import math


def calculate(expression: str) -> str:
    """
    Evaluates a simple mathematical expression.
    Handles basic arithmetic: +, -, *, /, (, ).
    """
    try:
        # Using a restricted set of allowed characters for basic security
        allowed_chars = set("0123456789+-*/(). ")
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Invalid characters in expression")

        # Using eval with limited globals for basic math evaluation
        # Note: In production, consider a proper expression parser library
        result = eval(expression, {"__builtins__": {}}, {})
        return str(float(result) if isinstance(result, (int, float)) else result)
    except Exception as e:
        return f"Error: Could not evaluate expression. {str(e)}"
