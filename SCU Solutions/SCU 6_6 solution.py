import pandas as pd

survey_df = pd.read_csv("survey_df_cleaned.csv")

# Modify the following line of code after the equals sign to make the column
# dummy_is_nineties have a value of True when YEAR is in the 1990s (and False otherwise):
survey_df["dummy_is_nineties"] = (survey_df["YEAR"] >= 1990) & (survey_df["YEAR"] <= 1999)

# converts our True/False flag to an integer (1 or 0)
survey_df["dummy_is_nineties"] = survey_df["dummy_is_nineties"].astype(int)

# write to a new csv file:
survey_df.to_csv("survey_df_cleaned_with_dummy_variable.csv", index=False)

