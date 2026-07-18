import asyncio
import aiohttp

async def hello():
    print("start")
    await asyncio.sleep(2)
    print("End")


asyncio.run(hello())

async def task(name):
    print(f"{name} start")
    await asyncio.sleep(2)
    print(f"{name}end")
async def main():
    await asyncio.gather(task("A"),task("B"))

asyncio.run(main())

async def fetch_one():
    url = "https://api.github.com"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(response.status)
            data = await response.json()
            print(type(data))

asyncio.run(fetch_one())

import asyncio
import aiohttp
import time


async def fetch(session , url):
    async with session.get(url) as response:
        return response.status
    
urls =[
    "https://api.github.com",
    "https://httpbin.org/get",
    "https://api.agify.io?name=hari",
    "https://catfact.ninja/fact",
    "https://official-joke-api.appspot.com/random_joke",
]

async def main():
    async with aiohttp.ClientSession()as session:
        tasks = [fetch(session,url) for url in urls]
        results = await asyncio.gather(*tasks)
        print(results)


start = time.perf_counter()
asyncio.run(main())
print(f"async took {time.perf_counter()-start:.2f} sec")

import requests

start = time.perf_counter()
list_sc = []
for url in urls:
    r = requests.get(url)
    list_sc.append(r.status_code)

print(f"{list_sc} ---> list of status code sync")
print(f"sync took {time.perf_counter() - start:.2f} sec")



