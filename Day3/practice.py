# # """class Patient:
# #     def __init__(self ,name,age,diagnosis):
# #         self.name=name
# #         self._age= age
# #         self.__diagnosis=diagnosis


# #     def get_diagnosis(self):
# #         return self._Patient__diagnosis
    

# #     def update_diagnosis(self,new_diagnosis):
# #         self._Patient__diagnosis = new_diagnosis
# #         return f"diagnosis updated for {self.name}"
    
# #     def get_age(self):
# #         return self._age
    
# #     def update_age(self,new_age):
# #         if 0<new_age<120:
# #             self._age=new_age
# #         else:
# #             return f"invalid age!"
    
# #     def summary(self):
# #         return f"Patient Name: {self.name} | Age: {self.get_age()} | Diagnosis: {self.get_diagnosis()}"
    

# # p = Patient("Alice", 30, "Flu")

# # # Public access
# # print(p.name)           # Alice
# # p.name = "Alice Smith"  # works fine

# # # Protected — works but signals "don't touch"
# # print(p._age)           # 30  ← accessible but bad practice

# # # Private — blocked!
# # #print(p.__diagnosis)    # ❌ AttributeError

# # # Controlled access via methods
# # print(p.get_diagnosis()) # Flu
# # print(p.get_age())       # 30

# # p.update_diagnosis("Cold")  # Diagnosis updated for Alice Smith
# # p.update_age(31)            # works fine
# # p.update_age(-5)            # Invalid age!

# # print(p.summary())


# # """


class BankAccount:
    def __init__(self, owner , balance):
        self.owner=owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Invalid amount!")
        else:
            self.__balance = amount
    
    def deposit(self,amount):
        self.__balance = self.__balance + amount
        print(f"Deposited ₹{amount}. New balance: {self.__balance}")
    
    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance = self.__balance - amount
            print(f"New balance: {self.__balance}")


acc = BankAccount("Alice", 1000)
print(acc.owner)        # Alice
print(acc.balance)      # 1000

acc.balance=500
print(acc.balance)      # 500

acc.deposit(2000)           # Deposited ₹2000. New balance: 3000
acc.withdraw(500)           # New balance: 2500
acc.withdraw(15000)          # Insufficient funds!



class Temperature:
    
    def __init__(self, celsius):
        self.__celsius = celsius
    
    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            print("Temperature cannot be below absolute zero!")
        else:
            self.__celsius = value
    
    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32
    

t = Temperature(100)
print(t.celsius)        # 25
print(t.fahrenheit)     # 77.
    
t.celsius = 0
print(t.fahrenheit)
    
t.celsius = -300 
print(t.celsius)   # Temperature cannot be below absolute zero!  



import hashlib

class User:
    
    def __init__(self,username,password):
        self.username = username
        self.__password = self.__hash_password(password)

    def __hash_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self,password):
        if self.__hash_password(password) == self.__password:
            return True
        else:            
            return False       

user = User("alice", "password123")

print(user.username)  # alice
print(user.check_password("password123"))  # True

print(user.check_password("mypassword123")) # True
print(user.check_password("wrongpass"))     # False
print(user.check_password("MyPassword123"))