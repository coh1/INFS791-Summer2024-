import pandas as pd

# Import the pyplot module from the matplotlib package
import matplotlib.pyplot as plt

trips_df = pd.read_json('Trips from area 8.json')

# Create a series from the fare column
fareseries = trips_df.fare

# Construct a matplotlib figure
fig = plt.figure()

# Create a histogram of the fare data
plt.hist(fareseries)

# Modify title and axis labels
plt.title('Distribution of fares')
plt.xlabel('Dollars')
plt.ylabel('Frequency')

# Display chart
plt.show()

