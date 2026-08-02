import ast
import operator as op
from typing import Any, Dict, Union
from pydantic import BaseModel, Field

CALCULATOR_SCHEMA = {
    "type": "function",
    "function": {
        "name": "calculate",
        "description": "Evaluate a mathematical expression (e.g., '5*9' or '(10+5)/3').",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "The math expression to evaluate.",
                }
            },
            "required": ["expression"],
        },
    },
}

# Allowed operators for safe AST evaluation
ALLOWED_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}


class CalculatorInput(BaseModel):
    expression: str = Field(
        ...,
        description="The mathematical expression to evaluate, e.g., '2 + 2' or '(12 * 4) / 2'.",
    )


class CalculatorOutput(BaseModel):
    success: bool
    result: Union[float, int, None] = None
    error: Union[str, None] = None


def safe_eval_node(node: ast.AST) -> Union[int, float]:
    """Recursively evaluates an AST node securely."""
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    elif isinstance(node, ast.BinOp):
        left = safe_eval_node(node.left)
        right = safe_eval_node(node.right)
        op_type = type(node.op)
        if op_type in ALLOWED_OPERATORS:
            # Prevent excessive exponentiation DoS
            if op_type == ast.Pow and (right > 100 or left > 1000):
                raise ValueError("Exponent or base too large")
            return ALLOWED_OPERATORS[op_type](left, right)
        raise ValueError(f"Unsupported operator: {op_type.__name__}")
    elif isinstance(node, ast.UnaryOp):
        operand = safe_eval_node(node.operand)
        op_type = type(node.op)
        if op_type in ALLOWED_OPERATORS:
            return ALLOWED_OPERATORS[op_type](operand)
        raise ValueError(f"Unsupported unary operator: {op_type.__name__}")
    else:
        raise ValueError("Invalid mathematical expression")


def calculate(expression: str) -> CalculatorOutput:
    """
    Evaluates a mathematical expression safely using Python AST parsing.
    Supports basic arithmetic (+, -, *, /) and powers (**).
    """
    try:
        # Parse expression into an Abstract Syntax Tree (AST)
        parsed_tree = ast.parse(expression, mode="eval")
        numeric_result = safe_eval_node(parsed_tree.body)

        if isinstance(numeric_result, float) and numeric_result.is_integer():
            numeric_result = int(numeric_result)

        return CalculatorOutput(success=True, result=numeric_result)
    except ZeroDivisionError:
        return CalculatorOutput(success=False, error="Division by zero is undefined")
    except Exception as e:
        return CalculatorOutput(success=False, error=f"Invalid expression: {str(e)}")
