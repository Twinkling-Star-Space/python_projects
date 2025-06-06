

x = float(input("Enter a number x: "))
y = float(input("Enter a number y: "))

result = x + y

#round(number[, ndigits])# The round() function returns a floating point number that is a rounded version of the specified number.
# The number of decimals to use when rounding can be specified with the ndigits argument.
#big baracket implies that it is a optional argument, if not specified it will round to the nearest integer.

print(round(result, 2))  # rounding the result to 2 decimal places


#formating the output with commas
print(f"{result:,}")


# way to use fstring how many number of decimal places you want to print
print(f"{result:.2f}")  # formatting to 2 decimal places
