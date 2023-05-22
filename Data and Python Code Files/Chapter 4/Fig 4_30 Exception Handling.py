first_value = input("please enter a number between 1 and 100: ")
second_value = input("please enter another number between 1 and 100: ")

try:
    first_value = float(first_value)
    second_value = float(second_value)
    result = first_value/second_value
    print(str(first_value) + " divided by " + str(second_value) + " is " + str(result))
except ValueError:
    print("A value that you entered was not a valid number")
except ZeroDivisionError:
    print("The second number you entered was 0 which is not allowed")




