import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv('taxi trips Fri 7_7_2017.csv')
date_series = data['trip_start_timestamp']
new_date = date_series.str.slice(start=11, stop = 13)
data['Hour'] = new_date.astype(float)

x_vars = data[['dropoff_centroid_latitude', 'dropoff_centroid_longitude',
          'fare', 'pickup_centroid_latitude',
          'pickup_centroid_longitude', 'Hour']].values

# Transform data using MinMaxScalar
data_transformed = MinMaxScaler().fit(x_vars).transform(x_vars)

sum_sq_dev = []

for numclusters in range(2,10):
    kmeans_model = KMeans(n_clusters = numclusters).fit(data_transformed)
    sum_sq_dev.append(kmeans_model.inertia_)
    print("numclusters: ", numclusters,
          "inertia score: ",round(kmeans_model.inertia_, 1))

plt.plot(range(2,10),sum_sq_dev, 'bx-')
plt.show()

