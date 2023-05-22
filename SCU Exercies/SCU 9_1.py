import pandas as pd
import matplotlib.pyplot as plt

trips_df = pd.read_json('Trips from area 8.json')

trip_miles_series = trips_df.trip_miles

fig = plt.figure()

# Insert a line to create a histogram of the trip_miles data


plt.title('Distribution of Trip Miles')
plt.xlabel('Trip Miles')
plt.ylabel('Frequency')

plt.show()

