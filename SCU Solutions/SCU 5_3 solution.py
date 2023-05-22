import pandas as pd

# read the same file as SCU 5_2, but using Pandas instead:
with open("SCU 5_2.csv") as file:
    file_df = pd.read_csv(file, delimiter = ",")

print(file_df)

