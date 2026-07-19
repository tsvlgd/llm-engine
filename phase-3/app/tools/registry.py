import json

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
        tool_name = tool_call.function.name
        tool_args = json.loads(tool_call.function.arguments)
        func = self.get(tool_name)

        if not func:
            raise ValueError(f"Tool '{tool_name}' not found.")
        return func(**tool_args)


registry = ToolRegistry()
registry.register("calculate", calculate)
registry.register("current_time", current_time)
registry.register("generate_uuid", generate_uuid)
