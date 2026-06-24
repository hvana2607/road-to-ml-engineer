class Expense:
    def __init__(self,amount:int,category:str,description:str,date:str)-> None:
        self.amount = amount
        self.category = category
        self.description=description
        self.date= date

    def to_dict(self)-> dict[str:int|str]:
        return {
            "Amount" : self.amount,
            "Category": self.category,
            "Description": self.description,
            "Date":self.date
        }
    
    @classmethod
    def from_dict(cls,data)->"Expense":
        return cls(
            amount=data["Amount"],
            category=data["Category"],
            description=data["Description"],
            date=data["Date"]


        )

# #e = Expense(1000,"Food", "Lunch at cafe","06/22/2026")
# e1=e.from_dict(e.to_dict())
# print(e1.amount,e1.category,e1.description,e1.date)
