from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass    

class CardPayment(Payment):
    def pay(self,amount):
        print(f"Paid ₹{amount} via Card")

class UPIPayment(Payment):
    def pay(self,amount):
        print(f"Paid ₹{amount} via UPI")

class CashPayment(Payment):
    def pay(self,amount):
        print(f"Paid ₹{amount} in Cash")


payment_method =[CardPayment(), UPIPayment(), CashPayment() ]
for method in payment_method:
    method.pay(1000)


from abc import ABC,abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self,message):
        pass

class EmailNotification(Notification):
    def send(self,message):
        print(f"Email sent: {message}")

class SMSNotification(Notification):
    def send(self,message):
        print(f"SMS sent: {message}")

class PushNotification(Notification):
    def send(self,message):
        print(f"Push sent: {message}")

notification_methods = [EmailNotification(), SMSNotification(), PushNotification()]
for method in notification_methods:
    method.send("hello all")

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeeter(self):
        pass    

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def perimeeter(self):
        return 2 * 3.14 * self.radius
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeeter(self):
        return 2 * (self.length + self.width)
    
class Triangle(Shape):
    def __init__(self,side1,side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
    def perimeeter(self):
        return self.side1 + self.side2 + self.side3


shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]
for s in shapes:
    print(f"Area: {s.area():.2f}, Perimeter: {s.perimeeter():.2f}")