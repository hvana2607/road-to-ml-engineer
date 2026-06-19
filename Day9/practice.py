# import os
# class FileReadError(Exception):
#     def __init__(self,message,filepath):
#         super().__init__(message)
#         self.filepath = filepath
    
# def read_file(path):
#     try:
#         with open(path,"r") as f:
#             content = f.read()
#     except FileReadError:
#         raise FileReadError(f"file not found error {path}\n")
#     except PermissionError as e:
#         raise FileReadError(f"access denied for {path}")
#     else:
#         return content
#     finally:
#         with open("read_log.txt","a") as log:
#             log.write(f"attempted tp read {path}\n")


# try:
#     print(read_file("notice.txt"))
# except FileReadError as e:
#     print(e,"path : |",e.filepath)

# try:
#     print(read_file("missing_file.txt"))
# except FileReadError as e:
#     print(e,"path : |",e.filepath)

# try:
#     print(read_file(" "))
# except FileReadError as e:
#     print(e,"path : |",e.filepath)

##############################################################
# import random

# class APITimeoutError(Exception):
#     pass
# class RateLimitError(Exception):
#     pass

# def fake_api_call():
#     outcome = random.choice(["Success","APITimeout","RateLimit"])
#     if outcome == "APITimeout":
#         raise APITimeoutError("API time out error")
#     elif outcome == "RateLimit":
#         raise RateLimitError("Rate limit error")
#     else:
#         return f"Data transfered successfully"

# def call_with_retry(max_retries=3):
#     for attempt in range(1,max_retries):
#         try:
#             result = fake_api_call()
#             print(f"attempt {attempt}")
#             return result
#         except APITimeoutError as e:
#             print(f"API time out error {e} and attepmt {attempt}.. Retrying")
#         except RateLimitError as e:
#             print(f"Rate limit error {e} and attepmt {attempt}.. Stopping")
#             return None
#     return None


# call_with_retry()

# class BankError(Exception):
#     pass
# class InsufficientFundsError(BankError):
#     pass
# class InvalidAmountError(BankError):
#     pass
# class AccountLockedError(BankError):
#     pass

# class BankAccount():
#     def __init__(self,balance,locked=False):
#         self.balance = balance
#         self.locked = locked
#         self.log = []

#     def deposit(self,amount):
#         if self.locked:
#             raise AccountLockedError("Account is locked")
#         if amount <=0:
#             raise InvalidAmountError("Invalid Amount. Amount should be grater then Zero")
        
#         self.balance += amount
#         self.log.append(f"amount credited {amount} to account now new balance {self.balance} ")

#     def withdraw(self,amount):
#         if self.locked:
#             raise AccountLockedError("Account is locked")
#         if amount <=0:
#             raise InvalidAmountError("Invalid Amount. Amount should be grater then Zero")
#         if amount > self.balance:
#             raise  InsufficientFundsError(f"Insufficient Funds Error, You balance is {self.balance}")
        
#         self.balance -= amount
#         self.log.append(f"amount withdrawal {amount} to account now new balance {self.balance} ")

# account = BankAccount(balance=500)

# transaction = {
#     ("deposit", 200),
#     ("withdraw", 100),
#     ("withdraw", 700),   # will fail — insufficient funds
#     ("deposit", -50),    # will fail — invalid amount
#     ("withdraw", 50),
# }

# for action,amount in transaction:
#     try:
#         if action == "deposit":
#             account.deposit(amount)
#         elif action == "withdraw":
#             account.withdraw(amount)
#         print(f"OK: {action}{amount}")
#     except InsufficientFundsError as e:
#         print(f"{e}")
#     except InvalidAmountError as e:
#         print(f"{e}")
#     except AccountLockedError as e:
#         print(f"{e}")


# for entry in account.log:
#     print("",entry)


# def safe_divide(a, b):
#     result = None
#     try:
#         result = a / b
#     except ValueError as e:
#         print("Value error:", e)
#     except ZeroDivisionError as e:
#         print("Cannot divide by zero")
#     except Exception as e:
#         print("Unexpected error:", e)
#     return result

# print(safe_divide(10, 0))

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Age should be integer")
    if age < 0:
        raise ValueError(f"Age can't be -ve")
    return age


print(validate_age("twenty"))
