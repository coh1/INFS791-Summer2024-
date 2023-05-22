import pandas as pd

trips_df = pd.read_json('Trips by pickup area.json')
trips_df.columns = ['Total_Trips', 'Pickup_Area']
trips_df.set_index('Pickup_Area', inplace=True)

# The following line reports Descriptive Statistics
print("\n", trips_df.describe())

# The following line prints the first five rows of data
print("\n", trips_df.head())

# The following line prints the last five rows of data
print("\n", trips_df.tail())


