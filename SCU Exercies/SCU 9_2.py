import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

trips_df = pd.read_json('Trips from area 8.json')

# pull the tips and payment_type columns:
trips_df = trips_df[[]]

trips_df = trips_df.dropna()
trips_df = trips_df.astype({'tips' : float})
trips_df = trips_df.set_index('payment_type')

# make a groupby object that sums tips by payment_type
tips_by_payment_method = trips_df.groupby()

x_labels = pd.Series(tips_by_payment_method.index.values)
y_values = pd.Series(tips_by_payment_method['tips'].values)

bars = np.array(range(len(x_labels)))

plt.xticks(bars, x_labels)

# write a line that will add the bars to the graph:

# this code formats the plot:
plt.title('Taxi Tips by Payment Type')
plt.xlabel('Payment Type')
plt.ylabel('Tips in $')
plt.show()

