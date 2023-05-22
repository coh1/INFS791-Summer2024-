import pandas as pd

survey_df = pd.read_csv("survey_subset.csv")

# modify the following line of code to print the correlation
# matrix of the survey_df dataframe (use the corr() method):
print(survey_df.corr())

