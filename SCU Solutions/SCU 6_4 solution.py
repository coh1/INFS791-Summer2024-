import pandas as pd

results_df = pd.read_json("Taxi_Trips.json")

# Insert two lines below to print summary statistics about 
# the results_df dataframe,as well as the median.
print(results_df.describe())
print("The median value is: ", results_df.median())

