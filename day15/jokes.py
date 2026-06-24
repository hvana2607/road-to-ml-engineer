import requests

def get_joke()-> str:
    url ="https://v2.jokeapi.dev/joke/Any"

    params={
        "type":"twopart",
        "blacklistFlags":"nsfw,racist,sexist"
    }

    response = requests.get(url,params)
    data=response.json()

    if data["error"]:
        return "could not fetch a joke"
    
    return f"Setup: {data['setup']}\nPunchline: {data['delivery']}"


for i in range(3):
    print(get_joke())