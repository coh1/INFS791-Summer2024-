import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset_df = pd.read_csv("taxi trips Fri 7_7_2017.csv")

trips_df = dataset_df[['pickup_community_area','dropoff_community_area']]
trips_freq = pd.crosstab(trips_df.pickup_community_area,\
     trips_df.dropoff_community_area)

# Use stack method to separate values by pickup and dropoff area pairs
trips_freq = trips_freq.stack()
print("Type of trips_freq after stack: ", type(trips_freq), "\n")
print(trips_freq.head(3), "\n")

# Reset index to move index values into a DataFrame column
trips_freq = trips_freq.reset_index()
print("Type of trips_freq after reset_index: ", type(trips_freq), "\n")
print(trips_freq.head(3), "\n")

print("columns in trips_freq before rename:")
print(trips_freq.columns)
trips_freq = trips_freq.rename(columns={0:'numtrips'})
print("columns in trips_freq after rename:")
print(trips_freq.columns, "\n")

# Filter DataFrame to only include rows with more than 20 trips
trips_freq = trips_freq.query('numtrips>20')
print("trips_freq after applying query:")
print(trips_freq.head(3), "\n")

# Transform DataFrame to a frequency table
trips_freq = trips_freq.pivot("pickup_community_area",
                          "dropoff_community_area", "numtrips")

print("trips_freq after pivot: ")
print(trips_freq.head(3))

fig = plt.figure()
ax = sns.heatmap(trips_freq)

plt.show()

