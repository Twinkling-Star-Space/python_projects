def main():
    x = int(input("enter a number x: "))
    z = square(x)
    print(f"the square of {x} is : {z}")

def square(n):
    return n**2
#after return statement the code will not execute, it will return the value to the caller of the function.
    return n * n  # this is also a way to write the function

    return pow(n, 2) # this is also a way to write the function, pow is a built-in function that takes two arguments, the base and the exponent.

main()

