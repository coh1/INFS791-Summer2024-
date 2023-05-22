import pandas as pd

# Modify the following line to read the JSON file
# "Taxi_Trips.json" into a DataFrame
results_df = pd.read_json("Taxi_Trips.json")

print(results_df)

