calculator_schema = {
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

current_time_schema = {
    "type": "function",
    "function": {
        "name": "current_time",
        "description": "Get the current date and time in ISO format.",
        "parameters": {"type": "object", "properties": {}},
    },
}

uuid_schema = {
    "type": "function",
    "function": {
        "name": "generate_uuid",
        "description": "Generate a random unique identifier (UUID v4).",
        "parameters": {"type": "object", "properties": {}},
    },
}

TOOLS = [calculator_schema, current_time_schema, uuid_schema]
