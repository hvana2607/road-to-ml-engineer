"""class student:
    def __init__(self, name, grade, score):
        self.name = name
        self.grade = grade
        self.score = score
    

    def __str__(self):
        return f"Student:{self.name}| {self.grade}| {self.score}"
    def __repr__(self):
        return f"Student(name={self.name!r}, grade={self.grade!r}, score={self.score!r})"
    def is_passed(self):
        if self.score >= 40:
            return True
        else:   
            return False
s = student("Alice", "A", 85)
print(s)
print(repr(s))
print(s.is_passed())

students =[student("Alice", "A", 85), student("Bob", "B", 35), student("Charlie", "C", 50)]
for s in students:
    print(s)
    print(repr(s))
    print(f"Passed: {s.is_passed()}")


"""

"""Animal:

__init__ → name, age
__str__ → "Name: [name] | Age: [age]"
__repr__ → "Animal(name=[name!r], age=[age!r])"

Pet (inherits Animal):

__init__ → name, age, owner
__str__ → extend parent: add "| Owner: [owner]"
__repr__ → "Pet(name=[name!r], age=[age!r], owner=[owner!r])"

Dog (inherits Pet):

__init__ → name, age, owner, breed
__str__ → extend parent: add "| Breed: [breed]"
__repr__ → "Dog(name=[name!r], age=[age!r], owner=[owner!r], breed=[breed!r])"""


class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return (f"Name:{self.name} | Age:{self.age}")
    
    def __repr__(self):
        return(f"Animal(name={self.name!r}, age ={self.age!r})")
    
class Pet(Animal):
    def __init__(self,name,age,owner):
        super().__init__(name,age)
        self.owner=owner
    def __str__(self):
        return (super().__str__()+f"| Owner:{self.owner}")
    def __repr__(self):
        return (super().__repr__() + f", owner={self.owner!r})")
    
class Dog(Pet):
    def __init__(self,name,age,owner,breed):
        super().__init__(name, age, owner)
        self.breed=breed
    def __str__(self):
        return (super().__str__()+f"| Breed:{self.breed}")
    def __repr__(self):
        return (super().__repr__() + f", breed={self.breed!r})")
    

d = Dog("Bruno", 3, "Alice", "Labrador")

print(f"printing d: {d}")

print(repr(d))
