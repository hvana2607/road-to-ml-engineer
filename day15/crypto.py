import requests
def get_crypto_prices(coins:list[str])->None:
    url = "https://api.coingecko.com/api/v3/simple/price"

    params={
        "ids": ",".join(coins),   # "bitcoin,ethereum,solana"
        "vs_currencies": "usd,inr"
    }

    response = requests.get(url,params=params)
    response.raise_for_status()

    data = response.json()

    for coin,prices in data.items():
         print(f"{coin.upper()}: ${prices['usd']:,} USD | ₹{prices['inr']:,} INR")

get_crypto_prices(["bitcoin", "ethereum", "solana"])