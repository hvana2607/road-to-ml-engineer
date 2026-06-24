import requests

def get_weather(city:str,lat:float,lon:float)-> dict:
    urls= "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude" : lat,
        "longitude":lon,
        "current": "temperature_2m,wind_speed_10m,weathercode",
        "timezone":"auto" 
                 }
    
    response = requests.get(urls,params=params)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return {}
    
    data = response.json()
    current = data["current"]

    return{
        "city":city,
        "temperature_C":current["temperature_2m"],
        "wind_speed_kmh":current["wind_speed_10m"]
                    }

result = get_weather("Hyderabad", 17.385, 78.4867)
result1 = get_weather("Mumbai", 19.0760, 72.8777)
result2 = get_weather("Delhi", 28.6139, 77.2090)
print(result)
print(result1)
print(result2)