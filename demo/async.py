import asyncio

async def call_api(name):
    print(f"Starting {name}")
    await asyncio.sleep(2)
    print(f"Finished {name}")

async def main():
    await asyncio.gather(
        call_api("A"),
        call_api("B"),
        call_api("C")
    )

asyncio.run(main())