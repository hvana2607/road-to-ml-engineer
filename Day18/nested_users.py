import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()

# print(type(users), len(users))
# print(users[0].keys())
# print(users[0]["address"].keys())
# print(users[2]["address"]["geo"]["lat"])          # your expression — what prints?
# print(type(users[2]["address"]["geo"]["lat"]))

# print(users[0]["adress"]["geo"]["lat"])
# print(users[0].get("adress").get("geo"))

# print(users[0].get("adress"))
# print(users[0].get("adress", {}).get("geo"))

flattened = [
    (
        user["name"],                              # name
        user["address"]["city"],                   # city
        float(user["address"]["geo"]["lat"]),     # lat — why float()? you know why
        float(user["address"]["geo"]["lng"]),                             # lng — full chain yourself
    )
    for user in users
]

for row in flattened:
    print(row)