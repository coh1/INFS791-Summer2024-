import requests
import pandas as pd

# Modify the string in the following line to create a REST query 
# that returns the count of licenses by driver_type
search_results = requests.get("https://data.cityofchicago.org/resource/97wa-y6ff.json?").json()

# convert the results to a data frame:
results_df = pd.DataFrame.from_records(search_results)
results_df.columns = ["driver_type", "count"]
results_df = results_df.set_index("driver_type")

# print the results data frame that we created:
print(results_df)

