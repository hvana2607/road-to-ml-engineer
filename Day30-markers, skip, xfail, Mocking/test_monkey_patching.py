import requests

def fake_get(url):
    class FakeResponse:
        def json(self):
            return {"price":100}
    return FakeResponse()

def get_price_from_api():
    data = requests.get(...).json()["price"]
    return data

def test_get_price(monkeypatch):
    monkeypatch.setattr("requests.get",fake_get)
    result = get_price_from_api()
    assert result ==100