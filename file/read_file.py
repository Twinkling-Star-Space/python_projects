'''
with open("names.txt", "r") as my_file:
    lines = my_file.readlines()

for line in lines:
    print("hello, ", line, end ="")

#-----------------------------------------------



with open("names.txt", "r") as file:
    for line in file:
        print("hello, ",line.rstrip())


#-----------------------------------------------

'''

names = []

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")


#-------------------------------------------------
