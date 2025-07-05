
# this is one of the concept of printing the corresponding values
name = input("enter a name from harry potter:")

if name == "Harry" or name == "Hormione" or name == "Ron":
    print("Griffindor")

elif name == "Draco":
    print("Slytherin")

else:
    print("Who?")

#-------------------------------------------------------------------------------------
# the concept of match

name = input("Enter a name: ")

match name:
    case "Harry":
        print("Griffindor") 
    case "Hormione":
        print("Griffindor")
    case "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case default:
        #or we can use case _: 
        print("who?")

#-------------------------------------------------------------------------------------
# or the more succinc way to write the above code

name = input("Enter a name: ")

match name:
    case 'Harry' | 'Hormione' | 'Ron':
        print("Griffindor")
    case 'Draco':
        print("Slytherin")
    case _:
        print("who?")


#-------------------------------------------------------------------------------------

