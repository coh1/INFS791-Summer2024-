import pandas as pd

trips_df = pd.read_json('Trips by pickup area.json')
# The next line changes the DataFrame column names
trips_df.columns=['Total_Trips','Pickup_Area']

# The next line changes the DataFrame index 
trips_df.set_index('Pickup_Area',inplace=True)

print("\n",trips_df)



