import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset_df = pd.read_csv("AnscombeData.csv")
fig = plt.figure()

# Use seaborn lmplot to create multiple plots, one for each dataset
ax = sns.lmplot(x = 'x', y = "y", col = "DataSet", data = dataset_df, ci = None)
plt.savefig("AnscombeDataCharted.png", dpi = 300)

