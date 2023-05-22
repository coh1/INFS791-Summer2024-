import pandas as pd

# The following line constructs a DataFrame from a json file
trips_df = pd.read_json('Trips by pickup area.json')

print(trips_df)



