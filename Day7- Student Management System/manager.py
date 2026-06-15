from student import Student

import json

class StudentManager():
    def __init__(self,):
        self.students =[]
        self.load_from_file()
        
    def add_student(self,students_p):
        self.students.append(students_p)

    def delete_student(self,students_p):
        for r in self.students:
            if r.name == students_p:
                self.students.remove(r)

    
    def search_student(self,students_p):
        for r in self.students:
            if r.name == students_p:
                return r

    def update_student(self,students_p,updated_grade):
        for r in self.students:
            if r.name == students_p:
                r.grade = updated_grade

    def save_to_file(self):
        data=[s.to_dict() for s in self.students]
        with open("student_data.json","w") as f:
            json.dump(data,f,indent=4)
        
    def load_from_file(self):
        try:
            with open("student_data.json","r") as f:
                self.students = [Student.from_dict(d) for d in json.load(f)]
        except FileNotFoundError:
            self.students = []