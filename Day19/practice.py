import requests

# try:
#     requests.get("https://this-site-does-not-exist-abc123.com")
# except requests.exceptions.ConnectionError as e:
#     print("Could not connect.") 

# url = "https://httpbin.org/delay/10"

# try:
#     requests.get(url,timeout=5)
# except requests.exceptions.Timeout as e:
#     print("Request timed out.")

# try:
#     r=requests.get("https://httpbin.org/status/404")
#     r.raise_for_status()
# except requests.exceptions.HTTPError as e:
#     print("HTTP error:",e.response.status_code)

# def safe_get(url):
#     try:
#         r = requests.get(url,timeout=5)
#         print(f"{r.status_code} -----> Status code")
#         r.raise_for_status()
#         if r.status_code == 200:
#             data = r.json()
#             return data
#         else:
#             return None
       
#     except requests.exceptions.Timeout as e:
#         print("RequestTimed out")
#     except requests.exceptions.ConnectionError as e:
#         print("connection error")
#     except requests.exceptions.HTTPError as e:
#         print(f" Http Error. Error code {r.status_code}")
#     except requests.exceptions.RequestException as e:
#         print("Request failed")

    
    
# if __name__ == "__main__":
#     u = safe_get("https://jsonplaceholder.typicode.com/invalid-path")
#     print(u)
#     u1 = safe_get("https://jsonplaceholder.typicode.com/posts/1")
#     print(u1)
#     u2=safe_get("https://httpbin.org/delay/10")
#     print(u2)
#     u3=safe_get("https://this-site-does-not-exist-abc123.com")
#     print(u3)
import time

def safe_get_retry(url,retry=4):
    for attempts in range(1,retry+1):
        try:
            r = requests.get(url,timeout=3)
            r.raise_for_status()
            print("status code ==== ",r.status_code)
            data=r.json()
            return data
        except requests.exceptions.Timeout as e:
            print("Request Time Out")
            print(f"Attempts{attempts} failed : {e}")
            time.sleep(2**attempts)
    print("All retries failed")
    return None
if __name__ == "__main__":
   u=  safe_get_retry("https://jsonplaceholder.typicode.com/posts/1")
   print(u)
   u1=  safe_get_retry("https://httpbin.org/delay/10")
   print(u1)