import asyncio

async def fetch_data():
    print("start")
    await asyncio.sleep(2)
    return "data"

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())