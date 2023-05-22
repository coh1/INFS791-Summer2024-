import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

data = pd.read_csv('taxi trips Fri 7_7_2017.csv')
date_series = data['trip_start_timestamp']
new_date = date_series.str.slice(start=11, stop = 13)
data['Hour'] = new_date.astype(float)

x_vars = data[['dropoff_centroid_latitude','dropoff_centroid_longitude',
             'fare','pickup_centroid_latitude',
             'pickup_centroid_longitude','Hour']].values

data_transformed = MinMaxScaler().fit(x_vars).transform(x_vars)

# Use 5 clusters using the kmeans clustering method
kmeans_model = KMeans(n_clusters = 5).fit(data_transformed)

print("cluster centers: ")
print(kmeans_model.cluster_centers_,"\n")

data['cluster'] = kmeans_model.labels_

cluster0 = data.query("cluster==0")
cluster1 = data.query("cluster==1")
cluster2 = data.query("cluster==2")

print("cluster 0 fare statistics:")
print(cluster0[['fare','Hour']].describe(),"\n")

print("cluster 1 fare statistics:")
print(cluster1[['fare','Hour']].describe(),"\n")

print("cluster 2 fare statistics:")
print(cluster2[['fare','Hour']].describe())

data.to_csv("output_org_vals.csv", encoding='utf-8', index=False)

