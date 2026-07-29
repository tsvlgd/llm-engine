import json
from app.llm.client import client
from app.prompts import loader
from app.core.config import settings
from app.schemas.requests import SQLRequest
from app.schemas.responses import SQLResponse


async def perform_sql_generation(request: SQLRequest) -> SQLResponse:
    system_prompt = f"{loader('sql_generator')}\n\nSchema: {request.schema_context}"
    completion = client.chat.completions.create(
        model=settings.model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": request.question},
        ],
        response_format={"type": "json_object"},
    )
    data = json.loads(completion.choices[0].message.content)
    return SQLResponse(**data)
