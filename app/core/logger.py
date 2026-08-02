import logging
import sys

# Configure standard stream logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger("ai_workbench")


def log_event(event: str, **fields):
    """
    Helper to emit structured event logs.
    Usage: log_event("tool_started", tool="calculator")
    """
    field_str = " ".join(f"{k}={v!r}" for k, v in fields.items())
    logger.info(f"EVENT: {event} {field_str}".strip())
