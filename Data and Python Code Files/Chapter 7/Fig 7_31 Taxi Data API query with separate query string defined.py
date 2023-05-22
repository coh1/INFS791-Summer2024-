import requests
import pandas as pd

# Specify REST query string using URL and criteria
query_string = "https://data.cityofchicago.org/resource/wrvz-psew.json?"+\
    "$select=pickup_community_area,count(trip_seconds)&"+\
    "$group=pickup_community_area"

# Obtain the JSON data using the REST query
search_results = requests.get(query_string).json()

# Construct a Pandas DataFrame from the records 
results_df = pd.DataFrame.from_records(search_results)

# Change the names of the columns to be “number_of_trips” and “pickup_area”.
results_df.columns = ["number_of_trips", "pickup_area"]

results_df = results_df.set_index("pickup_area")

# Change the data type of the DataFrame to be float 
results_df = results_df.astype(float)
print(results_df.head(10))
print(results_df.describe())

