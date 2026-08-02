import httpx
import asyncio


async def test_streaming():
    timeout = httpx.Timeout(60.0, connect=10.0)
    url = "http://127.0.0.1:8000/stream"
    async with httpx.AsyncClient(timeout=timeout) as client:
        # We use a stream context here
        async with client.stream(
            "POST", url, json={"query": "Tell me a long story"}
        ) as response:
            async for chunk in response.aiter_text():
                print(chunk, end="", flush=True)


if __name__ == "__main__":
    asyncio.run(test_streaming())
