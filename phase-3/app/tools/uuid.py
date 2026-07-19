import uuid


def generate_uuid() -> str:
    """
    Generates a version 4 (random) UUID string.
    """
    return str(uuid.uuid4())
