# This program checks if a number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#  The above code can be simplified using a single if-else structure
print("Even" if num % 2 == 0 else "Odd")



# print the even numbers only
number = int(input("Enter a number: "))

for i in range(1, number):
    if i % 2 == 0:
        print(i, end="  ")


# the more descriptive version
# This program prints all even numbers from 1 to a given number (exclusive)
number = int(input("Enter a number: "))
count = 0
for i in range(1, number):
    if i % 2 == 0:
        print(i, end="  ")
        count += 1

print(f"\nTotal even numbers found is {count} in the range of 1 to {number}")


# using functions

def parity(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

number = int(input("Enter your number ( to check either an odd or an even): "))
parity(number)




# creating my own function to print even or odd numbers

def main():
    number = int(input("Enter a number: "))

    if is_even(number):
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
main()


# pythonic expression 

def main():
    number = int(input("Enter a number: "))
    print(f"{number} is {'Even' if is_even(number) else 'Odd'}")

def is_even(num):
    return num % 2 == 0

# also return TRUE if num % 2 == 0 else False
main()


# use of match-case statement to check names and print their houses
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
        print("who?")

