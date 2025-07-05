

name = input("Enter ? ")


my_file = open("names.txt", "a")

my_file.write(f"{name}\n")

my_file.close()


#----------------------------------------------------

name = input("Enter ? ")

with open("names.txt", "a") as my_file:
    my_file.write(f"{name}\n")

#------------------------------------------------------

