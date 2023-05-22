import pandas as pd

results_df = pd.read_json("Trips from area 8.json")

print("Original set of columns: ",results_df.columns)
# Insert a line of Python code replace the results_df DataFrame with a
#  DataFrame that just has two columns "trip_miles" and "trip_seconds"
results_df = results_df[['trip_miles', 'trip_seconds']]

print("After reducing columns: ",results_df.columns)

