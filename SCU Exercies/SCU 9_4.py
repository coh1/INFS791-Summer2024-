import pandas as pd
import matplotlib.pyplot as plt

trips_df = pd.read_json('Trips from area 8.json')

trip_miles_gt_0 = trips_df[['trip_miles', 'fare']].query('trip_miles > 0')
fare_series = trip_miles_gt_0.fare
trip_miles = trip_miles_gt_0.trip_miles

fig = plt.figure()

# Modify the following line of code to use a cyan colored triangle down marker
#   with a transparency value of 0.2
plt.plot(trip_miles,fare_series, marker = "o", linestyle = "none", color = 'g',
         label = "Taxi Fare", alpha = 0.3)
plt.title('Fares by Taxi Trip Miles')
plt.xlabel('Miles')
plt.ylabel('Dollars')
plt.legend()
plt.savefig("Figure for SCU 9_4.png", dpi = 300)

