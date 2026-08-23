# def add(a,b):
#     return a+b

# class Car:
#     def __init__(self,make):
#         self.make = make

# c = Car("Toyota")
# print(c.make)

# class Animal:
#     def __init__(self,name):
#         self.name = name
    
#     def speak(self):
#         return "bark"

# class Dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed

#     def speak(self):
#         return "Woof"

# a = Dog("Shero","abc")

# print(a.speak())

# class BankAccount:
#     def __init__(self):
#         self.__balance = 0

#     @property
#     def balance(self):
#         self.__balance = 500
#         return(f"Balance = {self.__balance}")

#     @balance.setter
#     def bal(self):
#         self.__b = 900
#         return(f"Balance = {self.__b}")

# b = BankAccount()
# print(b.balance)

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         return 3.14 * self.r ** 2

# class Rectangle(Shape):
#     def __init__(self):
#         self.l=3
#         self.b=2
#     def area(self):
#         return self.l*self.b

# c = Circle(2)
# r = Rectangle()
# print(c.area())
# print(r.area())

class BankAccount:
    def __init__(self):
        self.__balance=0
    
    @property
    def balance(self):
        return f"total balance = {self.__balance}"
    
    @balance.setter
    def balance(self,amount):
        if amount<0:
            print(f"negitive number rejected")
        else:
            self.__balance = amount
            

b=BankAccount()
b.balance = 50
print(b.balance)