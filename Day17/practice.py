import requests

def fetch_all_users(url):
    result = []
    offset = 0
    limit= 50
    while True:
        resp = requests.get(url,params={"limit":50,"offset":offset}).json()
        result.extend(resp["users"])
        if offset >= resp["total"]:
            break
        offset += limit
    return result


def fetch_all_users(url):
    result = []
    params={"limit":50}
    while True:
        resp = requests.get(url,params = params).json()
        result.extend(resp["user"])
        params["starting_after"]=resp["user"][-1]["id"]
        if not resp.get("has_more"):
            break
    return result
