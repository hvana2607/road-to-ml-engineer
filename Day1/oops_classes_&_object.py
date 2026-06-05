class students:
    def __init__(self,name,age,rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

    def display(self):
        return(f"""
        Name: {self.name}
        Age: {self.age}
        Roll No: {self.rollno}
        """)

s1 = students("Alice", 20, 101)
s2 = students("Bob", 22, 102)
s3 = students("Charlie", 21, 103)
s4 = students("David", 23, 104)
s5 = students("Eve", 19, 105)

list1 = []
list1=list1.append(s1.display()).append(s2.display()).append(s3.display()).append(s4.display()).append(s5.display())

print(list1)