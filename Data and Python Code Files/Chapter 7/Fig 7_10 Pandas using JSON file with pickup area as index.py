import pandas as pd
import numpy as np

TripsDF = pd.read_json('Trips by pickup area.json')
TripsDF.columns=['Total_Trips','Pickup_Area']

TripsDF.set_index('Pickup_Area',inplace=True)
TripsDF.index = pd.Series(TripsDF.index).replace(np.nan,'Unspecified')
print("\n",TripsDF.describe())
print("\n",TripsDF)

print("\ntrips for pickup area 77 using index: ",TripsDF.values[76])
print("\ntrips for pickup area 77 using value of index: ",TripsDF.loc[77.0])
print("\nmedian trips by pickup area: ",TripsDF.median())
print("\nmax trips by pickup area: ",TripsDF.max())
print("\nmin trips by pickup area: ",TripsDF.min())


