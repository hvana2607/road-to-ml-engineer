from crypto import get_crypto_prices
from jokes import get_joke
from weather import get_weather 




result = get_weather("Hyderabad", 17.385, 78.4867)
result1 = get_weather("Mumbai", 19.0760, 72.8777)
result2 = get_weather("Delhi", 28.6139, 77.2090)
print(result)
print(result1)
print(result2)

get_crypto_prices(["bitcoin", "ethereum", "solana"])

for i in range(3):
    print(get_joke())