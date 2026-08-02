import uuid

UUID_SCHEMA = {
    "type": "function",
    "function": {
        "name": "uuid",
        "description": "Generate a random unique identifier (UUID v4).",
        "parameters": {"type": "object", "properties": {}, "required": []},
    },
}


def generate_uuid() -> str:
    """
    Generates a version 4 (random) UUID string.
    """
    return str(uuid.uuid4())
