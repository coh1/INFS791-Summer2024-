import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv('GSS1993less_happy.csv')

# Modify the following to cluster on the AGE, HEALTH, RINCOM91, EDUC, and SEX variables
x_vars = data[[           ]].values

data_transformed = MinMaxScaler().fit(x_vars).transform(x_vars)

sum_sq_dev = []

for numclusters in range(2, 10):
    kmeans_model = KMeans(n_clusters=numclusters).fit(data_transformed)
    sum_sq_dev.append(kmeans_model.inertia_)
    print("numclusters: ", numclusters,
          "inertia score: ", round(kmeans_model.inertia_,1))

plt.plot(range(2, 10),sum_sq_dev, 'bx-')
plt.show()

