from typing import Any
from aiohttp import ClientSession


async def get_proxy() -> str | None:
    from urllib.request import getproxies

    try:
        proxy = getproxies()["http"]
    except KeyError:
        proxy = None
    del getproxies
    return proxy


async def get_json(link: str) -> Any:
    trust_env = not bool(isinstance(await get_proxy(), str))
    async with ClientSession(
        trust_env=trust_env,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        },
    ) as session:
        async with session.get(link) as response:
            return await response.json()
