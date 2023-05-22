import pandas as pd
import matplotlib.pyplot as plt

trips_df = pd.read_json('Trips_Fri07072017T4 trip_miles gt1.json')

fare_series = trips_df.fare
tips_series = trips_df.tips

fig = plt.figure()
# write a line to plot tips (y-axis) by fare (x-axis) on a scatterplot


plt.title("Tips by Fare")
plt.xlabel("Fares, in $")
plt.ylabel("Tips, in $")
plt.show()

