import pandas as pd

survey_data = pd.read_csv("survey_1000.csv")

average_hours_worked = survey_data["HRS1"].mean()
average_age = survey_data["AGE"].mean()

print(f"The average hours worked by respondent is {average_hours_worked}")
print(f"The average age is {average_age}")

