import csv

total_hours = 0.0
total_age = 0.0
line_number = 0

with open('survey_1000.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for line in csv_reader:
        
        if line_number > 0:
            hours_worked = float(line[3])
            age = float(line[90])
            total_hours += hours_worked
            total_age += age

        line_number += 1

average_hours_worked = round(total_hours/(line_number-1), 3)
average_age = round(total_age/(line_number-1), 3)

print(f"The average hours worked by respondent is {average_hours_worked}")
print(f"The average age is {average_age}")

