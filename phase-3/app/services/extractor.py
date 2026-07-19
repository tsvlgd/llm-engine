import json
from app.llm.prompts import loader
from app.llm.client import client
from app.core.config import settings
from app.schemas.responses import ExtractResponse


async def perform_extraction(text: str) -> ExtractResponse:
    completion = client.chat.completions.create(
        model=settings.model,
        messages=[
            {"role": "system", "content": loader("extraction")},
            {"role": "user", "content": text},
        ],
        response_format={"type": "json_object"},
    )

    data = json.loads(completion.choices[0].message.content)
    return ExtractResponse(**data)
