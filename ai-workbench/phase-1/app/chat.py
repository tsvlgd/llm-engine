from groq import Groq
from app.core.config import settings

client = Groq(api_key=settings.groq_api_key)

async def generate_stream(query: str):
    completion = client.chat.completions.create(
        model=settings.model,
        messages=[{"role": "user", "content": query}],
        stream=True,
    )
    for chunk in completion:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content

async def generate_message(query: str):
    completion = client.chat.completions.create(
        model=settings.model,
        messages=[{"role":"user", "content": query}],
        stream=False
    )
    full_text = completion.choices[0].message.content
    return {
        "answer": full_text,
        "model": settings.model
        }     