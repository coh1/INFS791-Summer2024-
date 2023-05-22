import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

trips_df = pd.read_json('TaxiTripsWithYearCoding.json')

new_trips_df = trips_df[['fare','trip_miles','trip_seconds', 'Pre2016']].copy()
# Modify the following line to specify a multiple regression model that estimates
#  the fare using the independent variables trip_miles, trip_seconds and Pre2016
model = smf.ols("""fare ~ trip_miles + trip_seconds + Pre2016""", data=new_trips_df).fit()

print("\nModel summary: ", model.summary())

