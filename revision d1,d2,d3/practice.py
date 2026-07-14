
# # class InvalidAmountError(Exception):
# #     pass

# # class BankAccount:
# #     def __init__(self,owner_name,opening_balance=0):
# #         self.owner_name=owner_name
# #         self.__balance=opening_balance
    
    
# #     @property
# #     def balance(self):
# #         return self.__balance
    
 
# #     def deposit(self,amount):
# #         if amount < 0:
# #             raise InvalidAmountError("Deposit must be positive")
# #         else:
# #             self.__balance = self.__balance + amount

# #         return f"Account of {self.owner_name}:${self.__balance}"

   
# #     def withdraw(self,amount):
# #         if amount > self.balance:
# #             raise InvalidAmountError(f"amount sgould be less then {self.balance}")
# #         else:
# #             self.__balance = self.__balance - amount

# #         return f"Account of {self.owner_name}:${self.__balance}"
    

# # acc = BankAccount("Asha", 1000)
# # acc.deposit(500)
# # print(acc.balance)

# # class circle:
# #     def __init__(self,radius):
# #         self.__radius = radius

# #     @property
# #     def area(self):
# #         return 3.14*(self.__radius**2)
    
# # c=circle(5)
# # print(c.area)

# class user:
#     def __init__(self,email):
#         self.__email = email

#     @property
#     def email(self):
#         return self.__email
    
#     @email.setter
#     def email(self,value):
#         if "@" not in value:                      # 1. guard the door
#             raise ValueError(f"Invalid email: {value}")
#         self.__email = value 

# u = user("asha@gmail.com")
# print(u.email)               # asha@gmail.com
# u.email = "asha@yahoo.com"
# print(u.email)               # asha@yahoo.com  ← MUST actually change now

# try:
#     u.email = "not-an-email"
# except ValueError as e:
#     print(f"Blocked: {e}")   # Blocked: Invalid email: not-an-email

# try:
#     u2 = user("garbage")
# except ValueError as e:
#     print(f"Blocked: {e}")   # even the constructor is guarded



import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        elapsed = time.time()-start
        print(f"{func.__name__} took {elapsed :.2f} sec")
        return result
    return wrapper

@timer
def slow_add(a,b):
    time.sleep(1)
    return a+b

r = slow_add(2,3)
print(r)
