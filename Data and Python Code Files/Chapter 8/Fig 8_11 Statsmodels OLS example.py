import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

trips_df = pd.read_json('JSON pickup area 8 and trip seconds more than 0.json')

new_trips_df=trips_df[['fare','trip_miles','trip_seconds']].copy()

# Perform a multiple regression using the ols function
model = smf.ols("""fare ~ trip_miles + trip_seconds""", data=new_trips_df).fit()

# Report results for model using summary method
print("\nModel summary: ", model.summary())

