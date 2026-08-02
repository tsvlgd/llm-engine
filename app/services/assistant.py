import time

from app.core.config import settings
from app.core.logger import log_event, logger
from app.llm.client import client
from app.schemas.responses import AssistantResponse
from app.tools.registry import registry


async def run_assistant(query: str) -> AssistantResponse:
    """Agentic Execution Loop with dynamic multi-turn tool calling, structured event logging, and context-aware error handling."""
    log_event("assistant_request_started", query_length=len(query))
    start = time.perf_counter()
    tools_used: list[str] = []

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant. When using tools that do not require parameters "
                "(like fetch_uuid or current_time), always pass an empty object {} for arguments."
            ),
        },
        {
            "role": "user",
            "content": query,
        },
    ]

    max_turns = 10
    turn = 0
    final_message = None
    finish_reason = "stop"

    while turn < max_turns:
        turn += 1
        log_event("llm_request_started", turn=turn)

        try:
            response = client.chat.completions.create(
                model=settings.model,
                messages=messages,
                tools=registry.schemas(),
                tool_choice="auto",
            )
        except Exception as e:
            elapsed_ms = round((time.perf_counter() - start) * 1000, 2)
            logger.exception("LLM API communication failed")
            log_event(
                "llm_request_failed",
                turn=turn,
                elapsed_ms=elapsed_ms,
                error_type=type(e).__name__,
                error=str(e),
            )
            raise RuntimeError(
                f"Failed to obtain response from LLM provider: {e!s}"
            ) from e

        choice = response.choices[0]
        message = choice.message
        finish_reason = choice.finish_reason

        if not message.tool_calls:
            final_message = message.content
            log_event(
                "assistant_finished", turns_taken=turn, total_tools_used=len(tools_used)
            )
            break

        messages.append(
            {
                "role": "assistant",
                "content": message.content or "",
                "tool_calls": [
                    {
                        "id": tool_call.id,
                        "type": "function",
                        "function": {
                            "name": tool_call.function.name,
                            "arguments": tool_call.function.arguments,
                        },
                    }
                    for tool_call in message.tool_calls
                ],
            }
        )

        for tool_call in message.tool_calls:
            tool_name = tool_call.function.name
            tools_used.append(tool_name)
            log_event("tool_requested", tool=tool_name, turn=turn)

            try:
                result = await registry.execute(tool_call)
            except Exception as e:
                logger.exception(
                    f"Unhandled exception during tool execution for '{tool_name}'"
                )
                log_event(
                    "tool_invocation_failed", tool=tool_name, turn=turn, error=str(e)
                )
                result = {"error": f"Failed to execute tool '{tool_name}': {e!s}"}

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_name,
                    "content": str(result),
                }
            )
    else:
        log_event("assistant_max_turns_exceeded", max_turns=max_turns)
        final_message = "Error: Maximum tool execution turns exceeded."
        finish_reason = "length"

    latency = int((time.perf_counter() - start) * 1000)

    return AssistantResponse(
        response=final_message or "Task completed successfully.",
        provider="groq",
        model=settings.model,
        tools_used=tools_used,
        latency_ms=latency,
        finish_reason=finish_reason,
    )
