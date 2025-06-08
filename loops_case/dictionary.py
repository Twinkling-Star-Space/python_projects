
#coding using dictionary in the python:
students = {
    "Ram" : "Dhanusha",
    "Rohan" : "Birendra bazaar",
    "Rajesh" : "Simradhi"
}
print(students["Ram"])
print(students["Rohan"])
print(students["Rajesh"])



#can we use loop print each corresponding values
students = {
    "Ram" : "Dhanusha",
    "Rohan" : "Birendra bazaar",
    "Rajesh" : "Simradhi"
}

for student in students:
    print(student+":"+students[student])

   #   print(student, students[student], sep = ":")




#combination of list and dictionaries

students = [
    { "Name":"Diplal", "Age" : "12"},
    { "Nmae":"Rohan", "Age" : "16"},
    {"Name": " Ryan", "Age" : "20"}
]

for student in students:
    print(students[student])



