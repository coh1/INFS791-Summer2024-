respondent_ages = (55, 28, 24, 34, 59, 22, 19)

over30list = []
# Add a line of Python code that uses a list comprehension
#  to create a list of ages that are over 30 based on the
#  respondent_ages list
over30list = [age for age in respondent_ages if age > 30]

print("The list of ages over 30 is: ", over30list)


