# import requests
# def fetch_all_items():
#     url = "https://api.example.com/v1/customers"
#     result = []
#     params = {"limit":100}
#     while True:
#         resp = requests.get(url,params=params)
#         if resp.status_code!=200:
#             print(f"status code = {resp.get("status_code")}")
#             raise Exception
        
#         body = resp.json()
#         data = body.get("data",[])
#         result.extend(data)
#         if not resp.get("has_more") or not data:
#             break
#         params["starting_after"]=resp["data"][-1]["id"]
        
#     return result


# import requests

# url = "https://jsonplaceholder.typicode.com/posts/99999"

# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()          # parse the body into Python objects
#     print(type(data))      # predict this BEFORE running
#     print(data["title"])    # print just the "title" field
# else:
#     print(f"Request failed: {response.status_code}")


# import requests

# url = "https://jsonplaceholder.typicode.com/posts/99999"

# response = requests.get(url)
# print(response.status_code)
# print(repr(response.text))

# data = response.json()
# print(type(data),data)

# import requests

# url = "https://jsonplaceholder.typicode.com/posts"

# params = {"userId" : 1}          # filter to userId 1

# response = requests.get(url, params=params)

# print(response.url)                # PREDICT this output before running

# if response.status_code == 200:
#     data = response.json()
#     print(type(data))              # PREDICT: dict or list? WHY?
#     print(len(data))
#     print(data)         # title of the first post
# else:
#     print(f"Request failed: {response.status_code}")


# import requests

# url = "https://jsonplaceholder.typicode.com/posts"

# new_post = {
#     "title": "Day 18 complete",
#     "body" : "Learned requests + JSON parsing",
#     "userId": 1

# }

# response = requests.post(url,json=new_post)

# print(response.status_code)
# data=response.json()
# print(data)

# import requests

# url = "https://httpbin.org/headers"

# headers = {
#     "User-Agent": "day18-student-script",
#     "Authorization": "Bearer fake-token-123"  
# }

# response = requests.get(url, headers=headers)

# print(response.status_code)
# print(response.json())

