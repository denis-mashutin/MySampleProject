import asyncio


async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')


async def foo(y):
    return y + 1
