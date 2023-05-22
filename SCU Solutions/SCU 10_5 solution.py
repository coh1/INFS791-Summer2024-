import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

data = pd.read_csv('GSS1993less_happy.csv')

# cluster on the AGE, HEALTH, RINCOM91, EDUC, and SEX variables
x_vars = data[['AGE', 'HEALTH', 'RINCOM91', 'EDUC', 'SEX']].values

data_transformed = MinMaxScaler().fit(x_vars).transform(x_vars)

data_transformed = MinMaxScaler().fit(x_vars).transform(x_vars)

# set the n_clusters parameter to the optimal number you determined in SCU 10.4:
kmeans_model = KMeans(n_clusters = 6).fit(data_transformed)

print("cluster centers: ")
print(kmeans_model.cluster_centers_,"\n")

data['cluster'] = kmeans_model.labels_

# The loop should run as many iterations
# as your optimal number of clusters::
for i in range(6):
    this_cluster = data.query(f"cluster=={i}")
    print("cluster ", i, " age statistics:")
    print(this_cluster[['AGE','EDUC']].describe(),"\n")

data.to_csv("output_org_vals.csv", encoding='utf-8', index=False)

