def hello(to):
    #here def is defining a function
    #hello with small parenthesis is the name of the function and behaves like a function
    #colon represents that it keeps the code attuned for indentation.

    print(f"hello! {to}")

name = input("Enter your name: ")
hello(name)



#here we can modify the function to print the information without using input function and also print the data using input function
def hello(to="World"):
    print(f"hello! {to}")

name = input("Enter your name: ")
hello(name)





# to write code in sequential order we use

def main():
    name = input("Enter your name: ")
    hello(name)

def hello(to):
    print(f"hello! {to}")

main()