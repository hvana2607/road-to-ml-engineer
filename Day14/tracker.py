from expense import Expense
import json
from pathlib import Path
import os
from my_decorators import log_action,handle_errors


class ExpenseTracker():
    def __init__(self)->None:
        self.expenses:list[str|int|None]=[]
        if os.path.exists("expenses.json"):
            self.__load()
    
    @log_action
    def add(self,expense: Expense)-> None:
        self.expenses.append(expense)
        self.__save()
    
    def all(self)-> list[str|int|None]:
        return self.expenses

    def __save(self)->list[dict[str:int|str]]:
        exp_list = []
        for i in self.expenses:
            s= i.to_dict()
            exp_list.append(s)
        with open("expenses.json","w") as exp:
            json.dump(exp_list,exp,indent=4)

    def __load(self):
        with open("expenses.json","r") as exp:
            e_list=json.load(exp)

        for i in e_list:
            s=Expense.from_dict(i) 
            self.expenses.append(s)

        

# e = Expense(500,"Food", "Lunch at cafe","06/22/2026")
# e1 = Expense(1000,"Food", "Lunch at cafe","06/22/2026")
# e2= Expense(2000,"Food", "Lunch at cafe","06/22/2026")
# e3 = Expense(3000,"Food", "Lunch at cafe","06/22/2026")
# tracker = ExpenseTracker()
# tracker.add(e)
# tracker.add(e1)
# tracker.add(e2)
# tracker.add(e3)
# # #tracker.save()
# # # print(e.to_dict())
# # print(f"length of the tracker = {len(tracker.all())}")
# print(f"length of the tracker = {len(tracker.all())}")