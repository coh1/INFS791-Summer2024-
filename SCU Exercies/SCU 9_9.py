import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

trips_df = pd.read_json("Trips from area 8.json")

fig = plt.figure()

# Use seabron FacetGrid function to specify column to use
#   to separate charts
facet_grid = 

ax = facet_grid.map(sns.distplot, "fare")

plt.savefig("fare distribution by payment_type.png", dpi=300)


