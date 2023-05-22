import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

gss_1993_df = pd.read_csv("GSS1993_UNHAPPY_recoded.csv")

fig = plt.figure()

# Use seaborn FacetGrid function to specify column to use
#   to separate charts
FacGr = sns.FacetGrid(gss_1993_df, col="HEALTH")

# Plot distribution of ages for each Health value
ax = FacGr.map(sns.distplot, "AGE")

plt.savefig("Age distribution by health.png", dpi=300)


