import json
import logging

from app.tools.calculator import calculate
from app.tools.current_time import current_time
from app.tools.uuid import generate_uuid


class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, name: str, func: callable):
        self.tools[name] = func

    def get(self, name: str):
        return self.tools.get(name)

    def execute(self, tool_call):
        logger = logging.getLogger(__name__)

        tool_name = tool_call.function.name
        func = self.get(tool_name)

        if not func:
            raise ValueError(f"Tool '{tool_name}' not found.")

        try:
            raw_args = tool_call.function.arguments
            tool_args = json.loads(raw_args) if raw_args else {}
        except json.JSONDecodeError as e:
            logger.error(f"Malformed arguments for tool '{tool_name}': {raw_args}")
            return {"error": f"Failed to parse tool arguments: {str(e)}"}

        try:
            return func(**tool_args)
        except TypeError as e:
            logger.error(f"Argument mismatch for tool '{tool_name}': {e}")
            return {"error": f"Invalid arguments provided for tool: {str(e)}"}


registry = ToolRegistry()
registry.register("calculate", calculate)
registry.register("current_time", current_time)
registry.register("uuid", generate_uuid)
