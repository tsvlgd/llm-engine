import json
from app.llm.client import client
from app.core.config import settings
from app.llm.prompts import summary
from app.schemas.responses import SummarizeResponse


async def perform_summary(text: str) -> SummarizeResponse:
    completion = client.chat.completions.create(
        model=settings.model,
        messages=[
            {
                "role": "system",
                "content": summary,
            },
            {"role": "user", "content": text},
        ],
        response_format={"type": "json_object"},
    )
    data = json.loads(completion.choices[0].message.content)
    return SummarizeResponse(**data)
