import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset_df = pd.read_json("Trips from area 8.json")
fig = plt.figure()

# Modify the following line to create plots of fare by trip_miles , one for each payment_type
ax = sns.lmplot(x =     , y =      , col =      , data = dataset_df, ci = None)
plt.savefig("TripInfoByPaymentType.png", dpi = 300)

