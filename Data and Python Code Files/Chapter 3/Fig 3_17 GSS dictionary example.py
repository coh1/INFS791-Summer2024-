# This Python code creates a dictionary with three entries
survey_dictionary = {"survey_count": 1000,
                     "2014_takers": 43,
                     "2016_takers": 52}

print("There are ",len(survey_dictionary)," respondents")
print("The largest dictionary key is : ", max(survey_dictionary))
print("The smallest dictionary key is : ", min(survey_dictionary))

print("The value corresponding to the largest key is: ",
      survey_dictionary[max(survey_dictionary)])

print("The value corresponding to the smallest key is: ",
      survey_dictionary[min(survey_dictionary)])

