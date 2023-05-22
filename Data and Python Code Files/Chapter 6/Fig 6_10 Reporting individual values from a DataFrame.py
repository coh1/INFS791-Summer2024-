import pandas as pd

trips_df = pd.read_json('Trips by pickup area.json')
trips_df.columns=['Total_Trips','Pickup_Area']
trips_df.set_index('Pickup_Area',inplace=True)

# The following line prints the value for row 76
print("\ntrips for pickup area 77 using index: ",trips_df.values[76])

# The following line prints the value for the row with index value 77.0
print("\ntrips for pickup area 77 using value of index: ",trips_df.loc[77.0])

# The following line prints the median value for each column in the DataFrame
print("\nmedian trips by pickup area: ",trips_df.median())

# The following line prints the maximum value for each column in the DataFrame
print("\nmax trips by pickup area: ",trips_df.max())

# The following line prints the minimum value for each column in the DataFrame
print("\nmin trips by pickup area: ",trips_df.min())


