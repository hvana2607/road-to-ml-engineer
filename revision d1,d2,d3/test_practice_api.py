import requests

def get_user_name(user_id):
    url = f"https://api.example.com/users/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data=response.json()
        return data["name"]
    else:
        raise Exception(f"Response status code is {response.status_code}")

def fake_get(url):
    class FakeResponse:
        def __init__(self):
            self.status_code = 200
        def json(self):
            return {"name": "Hari","status_code":200}
    return FakeResponse()

def test_get_user_name(monkeypatch):
    monkeypatch.setattr("requests.get",fake_get)
    result=get_user_name(5)
    assert result == "Hari"
    


