import asyncio
from src.completion_handler import papermc_runner, arclight_powered_runner
from src.utils import cfg

async def main():
    coroutine_list = [papermc_runner, arclight_powered_runner]
    if cfg.get("fast_loading"):
        tasks = [asyncio.create_task(coroutine()) for coroutine in coroutine_list]
        for task in tasks:
            await task
    else:
        for coroutine in coroutine_list:
            await coroutine()


if __name__ == "__main__":
    asyncio.run(main())
