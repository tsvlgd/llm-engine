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
            "role": "user",
            "content": query,
        }
    ]

    # First LLM call
    response = client.chat.completions.create(
        model=settings.model,
        messages=messages,
        tools=TOOLS,
    )

    message = response.choices[0].message

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

    messages.append(message)

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
