import pandas as pd

survey_data = pd.read_csv("survey_1000.csv")

average_hours_worked = survey_data["HRS1"].mean()
average_age = survey_data["AGE"].mean()

output_summary_file = open("results.txt", "w")
output_summary_file.write(f"Average hours worked: {average_hours_worked}")
output_summary_file.write("\n")
output_summary_file.write(f"Average age: {average_age}")
output_summary_file.close()

survey_hrs1_gt_0 = survey_data.query('HRS1 > 0')
print("The count of hours worked greater than 0 is: ",
      survey_hrs1_gt_0['HRS1'].count())
survey_hrs1_gt_0.to_csv("survey_hrs1_gt_0.csv")

