# the think you need to know is if you use if-else statement then you are mutually
#  exclusive but if you use only if statement then you are not mutually exclusive



score = int(input("ENTER YOUR SCORE:"))

if score >= 90 and score <= 100:
    print(" You got A+")
elif score >=80 and score < 90:
    print("You got A")
elif score >= 70 and score < 80:
    print("You got B+")
elif score >= 60 and score < 70:
    print("You got B")
elif score >= 50 and score < 60:
    print("You got C+")
else:
    print("you got C")

# The above code can be simplified using a single if-elif-else structure
score = int(input("ENTER YOUR SCORE:"))

if 90 <= score  <= 100:
    print(" You got A+")
elif 80 <= score < 90:
    print("You got A")
elif 70 <= score < 80:
    print("You got B+")
elif 60 <= score < 70:
    print("You got B")
elif 50 <= score < 60:
    print("You got C+")
else:
    print("you got C")


# The above code can be simplified using a single if-elif-else structure
score = int(input("ENTER YOUR SCORE:"))

if 90 <= score:
    print(" You got A+")
elif 80 <= score:
    print("You got A")
elif 70 <= score:
    print("You got B+")
elif 60 <= score:
    print("You got B")
elif 50 <= score:
    print("You got C+")
else:
    print("You got C")




# The above code can be simplified using a dictionary to map scores to grades
score = int(input("ENTER YOUR SCORE:"))
grades = {
    (90, 100): "A+",
    (80, 90): "A",
    (70, 80): "B+",
    (60, 70): "B",
    (50, 60): "C+",
    (0, 50): "C"
}

for (range, grade) in grades.items():
    if score >= range[0] and score < range[1]:
        print(f"You got {grade}")
        break



# The above code can be further simplified using a function
def get_grade(score):
    if score >= 90 and score <= 100:
        return "A+"
    elif score >= 80 and score < 90:
        return "A"
    elif score >= 70 and score < 80:
        return "B+"
    elif score >= 60 and score < 70:
        return "B"
    elif score >= 50 and score < 60:
        return "C+"
    else:
        return "C"
    
score = int(input("ENTER YOUR SCORE:"))
print(f"You got {get_grade(score)}")

# The above code can be further simplified using a single if-elif-else structure in the function
def get_grade(score):
    if 90 <= score <= 100:
        return "A+"
    elif 80 <= score < 90:
        return "A"
    elif 70 <= score < 80:
        return "B+"
    elif 60 <= score < 70:
        return "B"
    elif 50 <= score < 60:
        return "C+"
    else:
        return "C"
    
score = int(input("ENTER YOUR SCORE:"))
print(f"You got {get_grade(score)}")


# The above code can be further simplified using a dictionary and a function
def get_grade(score):
    grades = {
        (90, 100): "A+",
        (80, 90): "A",
        (70, 80): "B+",
        (60, 70): "B",
        (50, 60): "C+",
        (0, 50): "C"
    }
    
    for (range, grade) in grades.items():
        if score >= range[0] and score < range[1]:
            return grade    
        
score = int(input("ENTER YOUR SCORE:"))
print(f"You got {get_grade(score)}")



# The above code can be further simplified using a dictionary and a function with a single return statement
def main():
    score = int(input("ENTER YOUR SCORE:"))
    print(f"You got {get_grade(score)}")

def get_grade(score):
    grades = {
        (90, 100): "A+",
        (80, 90): "A",
        (70, 80): "B+",
        (60, 70): "B",
        (50, 60): "C+",
        (0, 50): "C"
    }
    
    for (range, grade) in grades.items():
        if score >= range[0] and score < range[1]:
            return grade    
        
main()

