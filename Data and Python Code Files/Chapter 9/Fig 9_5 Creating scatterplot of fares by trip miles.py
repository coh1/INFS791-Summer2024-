import pandas as pd
import matplotlib.pyplot as plt

trips_df = pd.read_json('Trips from area 8.json')

trip_miles_gt_0 = trips_df[['trip_miles','fare']].query('trip_miles > 0')

# Create series for each of the two columns to use in scatterplot
fare_series = trip_miles_gt_0.fare
trip_miles = trip_miles_gt_0.trip_miles

fig = plt.figure()

# Specify marker and line style (here, none) to use
plt.plot(trip_miles,fare_series,marker=".",linestyle="none")
plt.title('Fares by Taxi Trip Miles')
plt.xlabel('Miles')
plt.ylabel('Dollars')

# Save figure to a file
plt.savefig("Figure 9_5.png",dpi=300)

