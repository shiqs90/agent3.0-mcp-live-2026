import asyncio

async def task(name):
    print(f"{name}: start")
    await asyncio.sleep(2)
    print(f"{name}: done")

async def main():
    await asyncio.gather(
        task("A"),
        task("B"),
        task("C"),
    )

asyncio.run(main())