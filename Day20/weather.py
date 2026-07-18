import aiohttp
import asyncio
import time

async def fetch_weather(session,url,params):
    
    async with session.get(url,params=params) as response:
        data = await response.json()
        return data
    
url = "https://api.open-meteo.com/v1/forecast"

List_of_params=[
    {"latitude": 17.4, "longitude": 78.6, "current_weather": "true"},
    {"latitude": 28.6, "longitude": 77.2, "current_weather": "true"},
    {"latitude": 19.1, "longitude": 72.9, "current_weather": "true"}
]

list_of_city = ["Hyderabad","Delhi","Mumbai"]
async def main():
    async with aiohttp.ClientSession() as session:
        task = [fetch_weather(session,url,params) for params in List_of_params]
        result = await asyncio.gather(*task)
        # print(result[0])
        for i in range(0,3):
            # print(list_of_city[i],":",result[i]["latitude"],",",result[i]["longitude"])
            print(list_of_city[i]," : ",result[i]["current_weather"]["temperature"] , result[i]["current_weather_units"]["temperature"])
        return result

asyncio.run(main())