import pandas as pd
from sodapy import Socrata

# initialize the Socrata client:
client = Socrata("data.cityofchicago.org", None)

# Use the end of the URL, before the ".json"
results = 

# put the results in a dataframe & print it:
results_df = pd.DataFrame.from_records(results)
print(results_df)

