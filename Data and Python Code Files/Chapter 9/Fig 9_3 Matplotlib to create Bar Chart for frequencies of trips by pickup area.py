import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

trips_df = pd.read_json('Trips_Fri07072017T4 trip_miles gt1.json')
trips_df = trips_df[['fare','pickup_community_area']]

# Eliminate any rows with missing values
trips_df = trips_df.dropna()

# Change data type of pickup_community_area to integer
trips_df = trips_df.astype({'pickup_community_area':int})

trips_df = trips_df.set_index('pickup_community_area')

# Create DataFrame groupby object with count of pickups by area
pickups = trips_df.groupby('pickup_community_area').count()

x_labels = pd.Series(pickups.index.values)
y_values = pd.Series(pickups['fare'].values)

# Create an array of the number of categories to use in the histogram
bars = np.array(range(len(x_labels)))

# Use xticks method to specify actual values of pickup locations
plt.xticks(bars, x_labels)

plt.bar(bars, y_values)

plt.title('Taxi Trip Pickup Areas')
plt.xlabel('Pickup Community Area')
plt.ylabel('Frequency')
plt.show()

