import pandas as pd

# Import Socrata module from the sodapy package
from sodapy import Socrata

# Initialize a Socrata object using the URL of the API
client = Socrata("data.cityofchicago.org", None)

# Use Socrata object get method with a limit of 500 records
results = client.get("rr23-ymwb", limit=500)

# Construct a DataFrame from the retrieved records
results_df = pd.DataFrame.from_records(results)
print("taxi API results: ")
print(results_df.head())

# Construct DataFrame from the vehicle number and fuel source fields
vehicles_and_fuel_sources = results_df[["public_vehicle_number", \
                                        "vehicle_fuel_source"]]
print("vehicles and fuel sources: ")
print(vehicles_and_fuel_sources.head(10),"\n")

# Group recors by fuel source
vehicles_by_fuel_type = vehicles_and_fuel_sources.groupby\
                        (by="vehicle_fuel_source")
print(vehicles_by_fuel_type.count())

results_df.to_csv("taxi_results.csv")

