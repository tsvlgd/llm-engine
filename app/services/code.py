import json
from app.prompts import loader
from app.llm.client import client
from app.core.config import settings
from app.schemas.responses import CodeExplainResponse


async def perform_code_explanation(code: str) -> CodeExplainResponse:
    completion = client.chat.completions.create(
        model=settings.model,
        messages=[
            {"role": "system", "content": loader("explainer")},
            {"role": "user", "content": code},
        ],
        response_format={"type": "json_object"},
    )

    data = json.loads(completion.choices[0].message.content)
    return CodeExplainResponse(**data)
