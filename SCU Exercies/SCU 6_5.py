import pandas as pd

survey_df = pd.read_csv("survey_df_less_columns.csv")

# Modify the following line of code to remove SIBS values of -1, 98, and 99,
# and HRS1 values of -1
survey_df_cleaned = survey_df.loc[]

# The following line writes the cleaned data to .csv file:
survey_df_cleaned.to_csv("survey_df_cleaned.csv", index=False)

