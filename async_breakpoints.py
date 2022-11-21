import asyncio


async def foo(y):
    return y + 1 # breakpoint


asyncio.run(foo(1))


