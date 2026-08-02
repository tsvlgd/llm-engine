import inspect
import json
import time
from collections.abc import Callable
from typing import Any

from app.core.logger import log_event, logger
from app.tools.calculator import CALCULATOR_SCHEMA, calculate
from app.tools.current_time import CURRENT_TIME_SCHEMA, current_time
from app.tools.uuid import UUID_SCHEMA, generate_uuid
from app.tools.weather import WEATHER_SCHEMA, get_weather


class ToolRegistry:
    def __init__(self):
        self._tools: dict[str, dict[str, Any]] = {}

    def register(self, name: str, function: Callable, schema: dict[str, Any]):
        self._tools[name] = {
            "function": function,
            "schema": schema,
        }

    def tool_count(self) -> int:
        return len(self._tools)

    def schemas(self) -> list[dict[str, Any]]:
        return [tool_data["schema"] for tool_data in self._tools.values()]

    async def execute(self, tool_call) -> Any:
        tool_name = tool_call.function.name
        tool_entry = self._tools.get(tool_name)

        if not tool_entry:
            log_event("tool_not_registered", tool=tool_name)
            raise ValueError(f"Tool '{tool_name}' is not registered.")

        func = tool_entry["function"]
        raw_args = getattr(tool_call.function, "arguments", "")

        try:
            tool_args = json.loads(raw_args) if raw_args else {}
        except json.JSONDecodeError as e:
            logger.exception("tool_argument_parse_failed")
            log_event(
                "tool_argument_parse_failed",
                tool=tool_name,
                raw_args=raw_args,
                error=str(e),
            )
            return {"error": f"Failed to parse tool arguments: {e!s}"}

        start_time = time.perf_counter()
        log_event("tool_started", tool=tool_name, arguments=tool_args)

        try:
            if inspect.iscoroutinefunction(func):
                result = await func(**tool_args)
            else:
                result = func(**tool_args)

            elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)
            log_event("tool_completed", tool=tool_name, latency_ms=elapsed_ms)
            return result

        except TypeError as e:
            elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)
            logger.exception("tool_argument_mismatch")
            log_event(
                "tool_failed",
                tool=tool_name,
                latency_ms=elapsed_ms,
                error_type="TypeError",
                error=str(e),
            )
            return {"error": f"Invalid arguments provided for tool: {e!s}"}

        except Exception as e:
            elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)
            logger.exception(f"Execution failed for tool '{tool_name}'")
            log_event(
                "tool_failed",
                tool=tool_name,
                latency_ms=elapsed_ms,
                error_type=type(e).__name__,
                error=str(e),
            )
            return {"error": f"Execution error in tool '{tool_name}': {e!s}"}


registry = ToolRegistry()

registry.register(
    name="calculate",
    function=calculate,
    schema=CALCULATOR_SCHEMA,
)

registry.register(
    name="current_time",
    function=current_time,
    schema=CURRENT_TIME_SCHEMA,
)

registry.register(
    name="uuid",
    function=generate_uuid,
    schema=UUID_SCHEMA,
)

registry.register(
    name="get_weather",
    function=get_weather,
    schema=WEATHER_SCHEMA,
)
