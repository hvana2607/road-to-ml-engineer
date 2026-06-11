from manager import StudentManager
from student import Student

manager = StudentManager()
while True:
    print(f"""
                    1. Add student
                    2. View all students
                    3. Search student
                    4. Delete student
                    5. Update student
                    0. Exit
                """)
    s=input("Choose: ")

    if s =="1":
        add_name = input("Name: ")
        add_age = int(input("Age:"))
        add_grade= int(input("Grade: "))
        add_subjects=[]
        a=input("subjects: ")
        add_subjects.append(a)
        add_s=Student(add_name,add_age,add_grade,add_subjects)
        manager.add_student(add_s)
        manager.save_to_file()
    elif s=="2":
        result= [a.to_dict() for a in manager.students]
        print(result)
    elif s=="3":
        s_name = input("Please enter sudent name: ")
        result= manager.search_student(s_name)
        print(result.to_dict())
    elif s=="4":
        d_name = input("Please enter sudent name you want to delete: ")
        manager.delete_student(d_name)
        print("student deleted")
        manager.save_to_file()
    elif s=="5":
        s_name = input("Please enter sudent name you want to update: ")
        update_grade =int(input("Please enter updated grade: "))
        result= manager.update_student(s_name, update_grade)
        print("student updated")
        manager.save_to_file()
    elif s=="6":
        result= [a.name for a in manager.students if a.grade>=80]
        print(result)
        dict_result = {a.name:a.grade for a in manager.students}
        print(dict_result)
        print(f"Average grade = {int(sum([a.grade for a in manager.students])/len([a.grade for a in manager.students]))}")
    elif s=="0":
        manager.save_to_file()
        break
        
