import requests
def fetch_all_items():
    url = "https://api.example.com/v1/customers"
    result = []
    params = {"limit":100}
    while True:
        resp = requests.get(url,params=params)
        if resp.status_code!=200:
            print(f"status code = {resp.get("status_code")}")
            raise Exception
        
        body = resp.json()
        data = body.get("data",[])
        result.extend(data)
        if not resp.get("has_more") or not data:
            break
        params["starting_after"]=resp["data"][-1]["id"]
        
    return result