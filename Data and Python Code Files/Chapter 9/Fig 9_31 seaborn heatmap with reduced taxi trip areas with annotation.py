import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset_df = pd.read_csv("taxi trips Fri 7_7_2017.csv")

trips_df = dataset_df[['pickup_community_area','dropoff_community_area']]

# Create crosstab, apply stack method, reset index and rename column
trips_freq = pd.crosstab(trips_df.pickup_community_area,\
     trips_df.dropoff_community_area).stack().\
     reset_index().rename(columns={0:'numtrips'})

trips_freq = trips_freq.query('numtrips>20')
trips_freq = trips_freq.pivot("pickup_community_area",
     "dropoff_community_area", "numtrips")

# Replace missing values with zeros
trips_freq = trips_freq.replace(np.nan, 0)
trips_freq = trips_freq.astype(int)

fig = plt.figure()

# Show integer values on heatmap
ax = sns.heatmap(trips_freq, annot=True, fmt="d")
plt.show()


