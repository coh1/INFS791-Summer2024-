# This Python code asks user to enter a password and then uses
# a while loop to check if the password satisfies several criteria
 
valid_password = False
number_attempts = 0

password_entered = input("Please enter a password that: " \
    + "\n - is at least 8 characters long" \
    + "\n - has at least one capital letter" \
    + "\n - has at least one non-alphanumeric symbol: ")

while not valid_password:
    number_attempts = number_attempts + 1

    if len(password_entered)< 8:
        print("\npasssword must be at least 8 characters long")
    elif password_entered.isalpha():
        print("\npassword must have at least one non-alphanumeric symbol")
    elif password_entered.islower(): 
        print("\npassword must have at least one capital letter") 
    else:
        valid_password = True
        continue

    if number_attempts > 3:
        print("\nToo many incorrect attempts!")
        break

    password_entered = input("\nPlease enter another password that" \
        + "\n - is at least 8 characters long" \
        + "\n - has at least one capital letter" \
        + "\n - has at least one non-alphanumeric symbol: ")

else:
    print("A valid password has been entered")


