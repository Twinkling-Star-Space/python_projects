
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")


#--------------------------------------------

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")


#--------------------------------------------
student_s =[]

with open("students.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        student_s.append(f"{name} is in {house}")

for student in sorted(student_s):
    print(student)

#---------------------------------------------------

student_s =[]

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = { "name": name, "house" : house}
        student_s.append(student)

def get_name(student):
    return student['name']

       
for student in sorted(student_s, key = get_name):
    print(f"{student['name']} is in {student['house']}")

#----------------------------------------------------------


student_s =[]

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = { "name": name, "house" : house}
        student_s.append(student)

       
for student in sorted(student_s, key = lambda student : student["name"]):
    print(f"{student['name']} is in {student['house']}")

#-----------------------------------------------------------------------

# -
import csv
student_s = []


with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        student_s.append({"name":name, "home":home})

for student in sorted(student_s, key = lambda student:student["name"]):
    print(f"{student['name']} is in {student['home']}")

#-------------------------------------------------------------------------------------