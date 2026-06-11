class Student:
    def __init__(self,name, age, grade, subjects):
        self.name=name
        self.age=age
        self.grade=grade
        self.subjects=subjects

    def to_dict(self):
        return{
            "name": self.name,
            "age": self.age,
            "grade":self.grade,
            "subjects":self.subjects
        }
    
    @classmethod
    def from_dict(cls,data):
        return cls(
            name=data["name"],
            age=data["age"],
            grade=data["grade"],
            subjects=data["subjects"]
        )
    

# s = Student("Harika",24,90,['Maths','English','Hindi'])
# print(s.to_dict())

# d = {"name":"Harika","age":20,"grade":90,"subjects":["Maths","English","Hindi"]}
# d1=Student.from_dict(d)
# print(d1.name)