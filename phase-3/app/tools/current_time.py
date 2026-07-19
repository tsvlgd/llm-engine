from datetime import datetime


def current_time() -> str:
    """
    Returns the current ISO 8601 formatted timestamp.
    """
    # Using isoformat() provides a standard string representation
    return datetime.now().isoformat(timespec="seconds")
