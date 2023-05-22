import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

gss_1993_df = pd.read_csv("GSS1993_UNHAPPY_recoded.csv")

fig = plt.figure()

# Use the seaborn countplot to chart the number of widowed responses 
#  for each health category
ax = sns.countplot(x="WIDOWED", hue="HEALTH", data=gss_1993_df)

plt.savefig("Counts of health responses by widowed.png", dpi=300)


