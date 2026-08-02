from datetime import datetime

CURRENT_TIME_SCHEMA = {
    "type": "function",
    "function": {
        "name": "current_time",
        "description": "Get the current date and time in ISO format.",
        "parameters": {"type": "object", "properties": {}, "required": []},
    },
}


def current_time() -> str:
    """
    Returns the current ISO 8601 formatted timestamp.
    """
    # Using isoformat() provides a standard string representation
    return datetime.now().isoformat(timespec="seconds")
