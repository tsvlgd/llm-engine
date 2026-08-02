import asyncio
import urllib.parse

import httpx

WEATHER_SCHEMA = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Fetch current weather conditions and temperature for a given city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The name of the city (e.g., 'London', 'Tokyo', 'San Francisco').",
                }
            },
            "required": ["city"],
        },
    },
}


async def get_weather(city: str) -> str:
    headers = {"User-Agent": "AI-Workbench/1.0"}
    max_retries = 3
    timeout = 5.0
    backoff_factor = 1.0

    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={urllib.parse.quote(city)}&count=1&language=en&format=json"
    geo_data = None
    # retry mechanism
    for attempt in range(max_retries):
        async with httpx.AsyncClient(timeout=timeout) as client:
            try:
                response = await client.get(geo_url, headers=headers)
                response.raise_for_status()
                geo_data = response.json()
                break
            except (httpx.RequestError, httpx.HTTPStatusError):
                if attempt == max_retries - 1:  # giving up
                    return f"Error: Network failure while fetching forecast for '{city_name}' after {max_retries} attempts."
                await asyncio.sleep(backoff_factor * (2**attempt))

    location = geo_data["results"][0]
    lat = location["latitude"]
    lon = location["longitude"]
    city_name = location["name"]
    country = location.get("country", "")

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    weather_data = None
    async with httpx.AsyncClient(timeout=timeout) as client:
        for attempt in range(max_retries):
            try:
                response = await client.get(weather_url)
                response.raise_for_status()
                weather_data = response.json()
                break
            except (httpx.RequestError, httpx.HTTPStatusError):
                if attempt == max_retries - 1:
                    return f"Error: Network failure while fetching forecast for '{city_name}' after {max_retries} attempts."

                await asyncio.sleep(backoff_factor * (2**attempt))

    current = weather_data.get("current_weather", {})
    temp_c = current.get("temperature")
    windspeed = current.get("windspeed")
    weather_code = current.get("weathercode")
    weather_conditions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Foggy",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        80: "Rain showers",
        95: "Thunderstorm",
    }
    condition = weather_conditions.get(weather_code, "Unknown")
    return f"Weather in {city_name}, {country}: {temp_c}°C, {condition}, Wind speed: {windspeed} km/h"
