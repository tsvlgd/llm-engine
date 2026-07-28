import json
import time

from app.core.config import settings
from app.llm.client import client
from app.schemas.responses import AssistantResponse
from app.schemas.tools import TOOLS
from app.tools.registry import registry


async def run_assistant(query: str) -> AssistantResponse:
    start = time.perf_counter()

    tools_used: list[str] = []

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. When using tools that do not require parameters (like fetch_uuid or current_time), always pass an empty object {} for arguments.",
        },
        {
            "role": "user",
            "content": query,
        },
    ]

    # First LLM call
    try:
        response = client.chat.completions.create(
            model=settings.model,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
        )
        message = response.choices[0].message
    except Exception as e:
        if hasattr(e, "body"):
            raise e

    # No tool required
    if not message.tool_calls:
        latency = int((time.perf_counter() - start) * 1000)

        return AssistantResponse(
            response=message.content,
            provider="groq",
            model=settings.model,
            tools_used=[],
            latency_ms=latency,
            finish_reason=response.choices[0].finish_reason,
        )
    messages.append(
        {
            "role": "assistant",
            "content": message.content,
            "tool_calls": [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {
                        "name": tc.function.name,
                        "arguments": tc.function.arguments,
                    },
                }
                for tc in message.tool_calls
            ],
        }
    )

    # Execute every tool
    for tool_call in message.tool_calls:
        tools_used.append(tool_call.function.name)
        result = registry.execute(tool_call)

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": tool_call.function.name,
                "content": str(result),
            }
        )

    # Final LLM response
    final = client.chat.completions.create(
        model=settings.model,
        messages=messages,
    )

    latency = int((time.perf_counter() - start) * 1000)

    return AssistantResponse(
        response=final.choices[0].message.content,
        provider="groq",
        model=settings.model,
        tools_used=tools_used,
        latency_ms=latency,
        finish_reason=final.choices[0].finish_reason,
    )
