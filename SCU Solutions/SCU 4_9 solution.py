# Add exception handling to report an error message
#  to the user if they don't enter a number (i.e. if they enter "ten")

try:
    value_entered = int(input("Please enter a number: "))
    print("The number you entered was: ", str(value_entered))
except ValueError:
    print("The value you entered was not a number")


