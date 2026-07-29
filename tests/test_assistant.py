import asyncio

from app.services.assistant import run_assistant


async def main():
    response = await run_assistant(
        "What is 28 * 5 + 10? Also explain the calculation step by step."
    )

    print(response)


asyncio.run(main())
