# This Python code creates a tuple with seven different ages
respondent_ages = (55, 28, 24, 34, 59, 22, 19)

under40_list1 = []
for age in respondent_ages:
    if age < 40:
        under40_list1.append(age)

under40_list2 = [age for age in respondent_ages if age < 40]

if under40_list1 == under40_list2:
    print("The two lists are equal")
    print("number of items in each list: ",
          len(under40_list1), "and", len(under40_list2))

