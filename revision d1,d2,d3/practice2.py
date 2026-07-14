# class User:
#     count = 1
#     def __init__(self,email):
#         self.email = email
    
#     @property
#     def email(self):
#         return self.__email
    
    
#     @email.setter
#     def email(self,value):
#         print(f"{User.count}>>> SETTER WAS CALLED") 
#         if "@" not in value or "." not in value:
#             raise ValueError("Invalid Email")
#         else:
#             self.__email = value
#         User.count += 1
    

# if __name__ == "__main__":
#     u = User("ravi@test.com")
#     print(u.email)              # ravi@test.com

#     u.email = "new@mail.org"
#     print(u.email)              # new@mail.org

#     try:
#         u.email = "not-an-email"
#     except ValueError as e:
#         print("Blocked:", e)    # Blocked: Invalid email

#     print(u.email)              # still new@mail.org — old value untouched

#     try:
#         u2 = User("bad")        # constructor must also reject
#     except ValueError as e:
#         print("Blocked in init:", e)

# nums = [3, 8, 12, 5, 20, 7, 16, 1]
# words = ["api", "json", "python", "ai", "langchain", "web"]

# r = [n**2 for n in nums if n%2==0]
# print(r)

# r =[w.upper() for w in words if len(w) >3 ]
# print(r)


# r = {w:len(w) for w in words}
# print(r)


# r = {n:n*2 for n in nums if n > 6}
# print(r)


# total = sum(n ** 2 for n in nums)
# print(total)

import json

config = {"app_name": "MyAI", "version": 1.0, "debug": True, "max_tokens": 500}

def save_config(config, path):
    with open(path, "w") as f:           # "w" = write mode ("r" = read mode)
        json.dump(config, f, indent=2)

    

def load_config(path):
    with open(path, "r") as f:
        data = json.load(f) 
    return data

if __name__ == "__main__":
    save_config(config, "config.json")
    loaded = load_config("config.json")
    print(loaded)
    assert loaded == config
    print("Round-trip OK")