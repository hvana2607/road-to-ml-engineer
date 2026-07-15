import csv

# def write_csv():
#     student = [
#         {"name":"Ali","Age":20,"Grade":"A"},
#         {"name":"Lax","Age":50,"Grade":"B"},
#         {"name":"Rao","Age":55,"Grade":"C"}
#     ]

#     with open("students.csv","w",newline="") as f:
#         write=csv.DictWriter(f,fieldnames=["name","Age","Grade"])
#         write.writeheader()
#         write.writerows(student)

# def read_csv():
#     with open("students.csv","r") as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             print(row["name"],row["Age"],row["Grade"])
        


# write_csv()
# read_csv()

# def write_csv_plain():
#     students = [
#         ["Ali", 20, "A"],
#         ["Lax", 50, "B"],
#         ["Rao", 55, "C"],
#     ]
#     with open("students_plain.csv", "w", newline="") as f:
#         writer = csv.writer(f)
#         writer.writerow(["name","age","grade"])      # header — ONE list
#         writer.writerows(students) 


# def read_csv_plain():
#     with open("students_plain.csv", "r") as f:
#         reader = csv.reader(f)
#         next(reader)
#         (reader)
#         for row in reader:
#             print(row[0],row[1],row[2]) 
#    # no keys here — how do you access items?



# write_csv_plain()
# read_csv_plain()


# with open("log.txt","a") as f:
#     f.write("Session on 2026-07-15: CSV revision done\n")

# with open("log.txt","r") as f:
#     for line in f:
#         print(line.strip())

student = {"name": "Ali", "marks": {"math": 90, "sci": 85}}

print(student["marks"]["sci"])

student["marks"]["eng"] = 75
print(student["marks"])

for i,j in student["marks"].items():
    print(f"{i}:{j}")