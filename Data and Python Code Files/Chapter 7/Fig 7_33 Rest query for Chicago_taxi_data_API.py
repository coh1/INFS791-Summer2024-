import pandas as pd
from sodapy import Socrata

# Initialize a Socrata object using the URL of the API
client = Socrata("data.cityofchicago.org", None)

# Use Socrata object get method with additional criteria to filter records
results = client.get("wrvz-psew",
               where="trip_miles > 1 and fare > 0 and"
                     + " trip_start_timestamp between '2017-07-07T00:00:00'"
                     + " and '2017-07-07T05:59:00'"
                     + " and pickup_community_area between '0' and '78'"
                     + " and dropoff_community_area between '0' and '78'")

# Construct a DataFrame from the results
results_df = pd.DataFrame.from_records(results)            
print(results_df.head())
print(results_df.describe())

