import pandas as pd
import matplotlib.pyplot as plt

# Modify the following line to use the seaborn style
plt.style.use(       )

trips_df = pd.read_json('Trips from area 8.json')

trip_miles_gt_0 = trips_df[['trip_miles', 'fare']].query('trip_miles > 0')
fare_series = trip_miles_gt_0.fare
trip_miles = trip_miles_gt_0.trip_miles

fig = plt.figure()
plt.plot(trip_miles, fare_series, marker = 'o', linestyle = "none",
              label = "Taxi Fare", alpha = 0.3)
plt.title('Fares by Taxi Trip Miles')
plt.xlabel('Miles')
plt.ylabel('Dollars')
plt.legend()
plt.savefig("Figure SCU 9_5.png", dpi = 300)


