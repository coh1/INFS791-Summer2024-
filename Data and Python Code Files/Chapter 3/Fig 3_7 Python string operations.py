# First create a Python string variable with "Hey, Taxi!" message
str_message = "Hey, Taxi!"

# The next line demonstrates how slicing of a string object works
print ("The second to seventh characters are ", str_message[1:7])

# The following line of code displays the values of the results
new_string = "Hey," + "Taxi!"
print ("The string resulting from concatenating the two parts is: ", new_string)

corrected_string = new_string[0:4] + " " + new_string[4:]
print ("The corrected string with a blank in the middle is: ", corrected_string)


