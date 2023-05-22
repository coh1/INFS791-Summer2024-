value_entered = input("please enter a number between 1 and 100: ")

if int(value_entered) < 50:
    print("You entered a value less than 50")
    if int(value_entered)< 40:
        print("You entered a value less than 40")
else:
    print("You entered a value greater than or equal to 50")

print("The value that you entered was: ", value_entered)

