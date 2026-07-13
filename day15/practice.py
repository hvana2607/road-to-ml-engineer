import requests

# def appbrewery()->str:
#     url ="https://bored-api.appbrewery.com/random"

#     response = requests.get(url)
#     if response.status_code != 200:
#         print("some issue in server")
#         return {}
#     data = response.json()

#     data["price"] = "Free" if data["price"] == 0.0 else "Costs money"

#     return f"""
#         Activity: {data["activity"]},
#         Type:{data["type"]},
#         Participants:{data["participants"]},
#         Price:{data["price"]}
#     """


# print(appbrewery())

def Country_Info()-> str:
    url = f"https://countriesnow.space/api/v0.1/countries/capital"

    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error {response.status_code}")
        return {}

    data=response.json()

    print(data)

Country_Info()
