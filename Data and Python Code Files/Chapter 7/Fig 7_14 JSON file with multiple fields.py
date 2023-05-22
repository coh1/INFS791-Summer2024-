import pandas as pd

TripsDF = pd.read_json('JSON pickup area 8 and trip seconds more than 0.json')

NewTripsDF=TripsDF[['fare','trip_miles','trip_seconds']].copy()
print("\n",NewTripsDF.describe())
print("\n",NewTripsDF.columns)
print("\n",NewTripsDF.corr())





