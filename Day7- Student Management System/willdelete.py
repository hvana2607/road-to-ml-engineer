# Class name: Book
# Attributes: title, price
# Instance method: to_dict() — returns a dictionary
# Classmethod: from_dict(data) — creates a Book from a dictionary


class Book:
    def __init__(self,title, price):
        self.title=title
        self.price=price
    
    def to_dict(self):
        return{
            "title":self.title,
            "price":self.price
        }
    @classmethod
    def from_dict(csl,data):
        return csl(
            title=data["title"],
            price=data["price"]
        )