import pandas as pd
import matplotlib.pyplot as plt

# Import Axes3D model
from mpl_toolkits.mplot3d import Axes3D

trips_df = pd.read_json('Trips from area 8.json')

trip_miles_gt_1 = \
     trips_df[['trip_miles', 'fare', \
     'dropoff_community_area']]. \
     query('trip_miles > 1')
fare_series = trip_miles_gt_1.fare
trip_miles = trip_miles_gt_1.trip_miles
dropoff_area = trip_miles_gt_1.dropoff_community_area

fig = plt.figure()

# Use projection parameter for 3 dimensionial plot
ax = fig.add_subplot(111, projection = '3d')

ax.scatter(dropoff_area,trip_miles,
           fare_series, c = 'b', marker = '.')

plt.title('Fares by Taxi Trip Miles and drop off area')

ax.set_xlabel('Dropoff Area')
ax.set_ylabel('Trip Miles')
ax.set_zlabel('Fares')

plt.show()


