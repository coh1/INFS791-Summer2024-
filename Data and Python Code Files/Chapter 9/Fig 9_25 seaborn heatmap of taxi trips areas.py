import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset_df = pd.read_csv("taxi trips Fri 7_7_2017.csv")

trips_df = dataset_df[['pickup_community_area','dropoff_community_area']]

# Create frequency table using crosstabs function
trips_freq = pd.crosstab(trips_df.pickup_community_area,\
     trips_df.dropoff_community_area)
print("After crosstab, type of trips_freq: ", type(trips_freq))
print(trips_freq.head(10), "\n")

fig = plt.figure()

# Create heatmap from frequency table (in DataFrame)
ax = sns.heatmap(trips_freq)

plt.show()

