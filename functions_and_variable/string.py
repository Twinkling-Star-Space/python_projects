# Example of using str in Python

# Creating strings
greeting = "Hello, World!"
name = str("Alice")

# String concatenation
message = greeting + " My name is " + name + "."

# String methods
upper_message = message.upper()
lower_message = message.lower()
title_message = message.title()

# String formatting
age = 25
formatted = f"{name} is {age} years old."

# Printing results
print("Original message:", message)
print("Uppercase:", upper_message)
print("Lowercase:", lower_message)
print("Title case:", title_message)
print("Formatted string:", formatted)

# way to print data by correcting the input of user 

name = input("Enter your name: ")
name = name.lower().strip()# Remove leading and trailing spaces and convert to lowercase
print("Hello,", name)



name = name.capitalize()  # Capitalize the first letter
print("Hello, "+name)


# if you want to print the name in title case
name = name.title()  # Capitalize the first letter of each word
print("Hello, " + name)


#we can some of all those codes written above in two lines
name = input("Enter your name: ").strip().title()  # Remove spaces and capitalize
print("Hello,", name)

