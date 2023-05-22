import pandas as pd
from scipy import stats

trips_df = pd.read_json('JSON pickup area 8 and trip seconds more than 0.json')

new_trips_df=trips_df[['fare','trip_miles','trip_seconds']].copy()

# Calculate the correlation coefficient between the fare data and the trip miles
print("\nPearsons r: ",\
      stats.pearsonr(new_trips_df['trip_miles'],new_trips_df['fare']))

# Perform a linear regression using the linregress function
slope, intercept, r_value, p_value, std_err = \
       stats.linregress(new_trips_df['trip_miles'],new_trips_df['fare'])

# Report results for slope, intercept, R value, p Value and Standard Error
print("\nslope: ",round(slope,3), "\nintercept: ", round(intercept,3),\
      "\nr_value: ",round(r_value,3), "\np_value: ",format(p_value,'.3e'),\
      "\nstd_err: ",round(std_err,3))

# Report results for skewness of variables
print("\nSkew for FareData: ",round(stats.skew(new_trips_df['fare']),3))
print("\nSkew for Trip_miles: ",round(stats.skew(new_trips_df['trip_miles']),3))

