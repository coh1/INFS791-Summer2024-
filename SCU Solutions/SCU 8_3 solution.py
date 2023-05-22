import pandas as pd
from scipy import stats

trips_df = pd.read_json('TaxiTripsWithTips.json')

new_trips_df = trips_df[['fare','tips']].copy()

# Modify the following line of code to perform a linear regression
# with dependent variable tips and independent variable fare
slope, intercept, r_value, p_value, std_err = \
       stats.linregress(new_trips_df['fare'],new_trips_df['tips'])

print("\nslope: ",round(slope,3), "\nintercept: ", round(intercept,3),\
      "\nr_value: ",round(r_value,3), "\np_value: ",format(p_value,'.2e'),\
      "\nstd_err: ",round(std_err,3))

