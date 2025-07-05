x = input("Enter a number: ")
y = input("Enter another number: ")

if(x<y):
    print("The first number is less than the second number.")

elif(x>y):
    print("The first number is greater than the second number.")

elif(x==y):
    print("The first number is equal to the second number.")

#-------------------------------------------------------------------------------------
# if:
#elif:
#else:

# compare the two numbers and print the result
x = input("Enter a number: ")
y = input("Enter another number: ")

if x < y or x > y :
    print("x is not equal to y ")
else:
    print("x is equal to y")

#-------------------------------------------------------------------

# the above code can be simplifies to :
x = input("Enter a number: ")
y = input("Enter another number: ")

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

#--------------------------------------------------------------

# the above code can be simplified to:
x = input("Enter a number: ")
y = input("Enter another number: ")
print("x is not equal to y" if x != y else "x is equal to y")


# the above code can be simplified to:
x = input("Enter a number: ")
y = input("Enter another number: ")
print(f"x is {'not ' if x != y else ''}equal to y")

#------------------------------------------------------------------


