import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

gss_1993_df = pd.read_csv("GSS1993_UNHAPPY_recoded.csv")

fig = plt.figure()

# Use seaborn distplot function to plot distribution of ages
ax = sns.distplot(gss_1993_df.AGE)
plt.savefig("Age distribution.png", dpi=300)


