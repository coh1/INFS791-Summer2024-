import pandas as pd

trips_df = pd.read_json('JSON pickup area 8 and trip seconds more than 0.json')

new_trips_df=trips_df[['fare','trip_miles','trip_seconds']].copy()
print("\n",new_trips_df.describe())
print("\n",new_trips_df.columns)

# The following line prints the correlation matrix
print("\n",new_trips_df.corr())





