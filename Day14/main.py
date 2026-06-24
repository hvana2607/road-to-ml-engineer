from expense import Expense
from tracker import ExpenseTracker
import datetime
print(f"""
        1. Add expense  
        2. View all  
        3. Exit
""")

tracker = ExpenseTracker()
while True:
    a = int(input("Select 1 ,2 or 3:"))
    if a==1:
        amount = int(input("Enter amount: "))
        category=input("Enter category: ")
        description=input("Enter description: ")
        date=input("Enter date: ")
        e = Expense(amount,category,description,date)
            # e1 = Expense(1000,"Food", "Lunch at cafe","06/22/2026")
            # e2= Expense(2000,"Food", "Lunch at cafe","06/22/2026")
            # e3 = Expense(3000,"Food", "Lunch at cafe","06/22/2026")
        tracker.add(e)
    elif a==2:
        for e in tracker.all():
            print(e.amount, e.category, e.description, e.date)
    elif a==3:
        break
