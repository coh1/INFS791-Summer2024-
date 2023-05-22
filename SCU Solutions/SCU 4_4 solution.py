value_entered = input("please enter a number less than 100: ")

if int(value_entered) > 50:
    print("The value entered is greater than 50.")
    # note this logic block could be rewritten to avoid
    # nested if statements. However, sometimes nesting is 
    # necessary.
    if int(value_entered) < 75:
        print("the value entered is also less than 75")
else:
    print("The value entered is less than or equal to 50.")



