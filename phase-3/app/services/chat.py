from app.llm.client import client
from app.core.config import settings
from app.schemas.responses import ChatResponse


async def generate_stream(query: str):
    completion = client.chat.completions.create(
        model=settings.model,
        messages=[{"role": "user", "content": query}],
        stream=True,
    )
    for chunk in completion:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content


async def generate_message(query: str) -> ChatResponse:
    completion = client.chat.completions.create(
        model=settings.model,
        messages=[
            # This system prompt satisfies the Groq requirement
            {
                "role": "system",
                "content": "You are a helpful assistant. Output your response as a valid JSON object. always with the dict key: answer",
            },
            {"role": "user", "content": query},
        ],
        stream=False,
    )

    full_text = completion.choices[0].message.content

    return {"answer": full_text, "model": settings.model}
