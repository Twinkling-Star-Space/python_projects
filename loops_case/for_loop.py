#using for loop to iterate over a list
# -----------------------------------------------------------------------------------
for i in [0, 2,3]:
    print("meow")

# this code will not print the desired output 



# lets find the solution to print the desired output of the user demand
x = int(input("Enter a number: "))
for i in range(x): #remember range is new keyword in python
    print("meow")



# you can use _ instead of i if you don't want to use the variable because you don't need it 




# lets try subtl way to do that
print("meow\t" * 3, end = "")  # this will print meow 3 times with a tab space
print("meow\n" * 3, end = "")




#lets take user input to how many times to  iterate
x = int(input("Enter a number: "))
if x < 0:
    print("meow\n" * (-1 * x), end = "") 
else:
    print("meow\n" * x, end = "") 



# c
while True:
    x = int(input("Enter a number: "))
    if x < 0:
        continue
    else:
        break



# or another way to do that is 
while True:
    x = int(input("Enter a number: "))
    if x > 0:
        break

for i in range(x):
    print("meow")




# using functions  to take input and validate it and then print the output
 
def main():
    number = get_number()
    out_put(number)


def get_number():
    while True:
        x = int(input("Enter a number:"))
        if x > 0:
            return x

def out_put(n):
    for _ in range(n):
        print("Meow")

main()








