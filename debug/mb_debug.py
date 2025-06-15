while True:
    try:
        x = int(input("ENTER :"))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"{x} is an integer")