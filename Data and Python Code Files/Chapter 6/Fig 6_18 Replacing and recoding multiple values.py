import pandas as pd
gss_df = pd.read_csv('GSS1993_UnhappyRecoded.csv')
gss_df.loc[gss_df.AGE == 99,'AGE'] = 46.04
print("mean of AGE: ", round(gss_df['AGE'].mean(),3))
print("Before replacing HEALTH values")
print(gss_df.HEALTH.value_counts(sort=False))

# The following line replaces multiple values in one step
gss_df.loc[(gss_df.HEALTH >= 8) | (gss_df.HEALTH == 0),'HEALTH'] = 2
print("after replacing values")
print(gss_df.HEALTH.value_counts(sort=False))

# The following line recodes multiple values in one step
gss_df.HEALTH.replace(to_replace=[1, 2, 3, 4], value=[4, 3, 2, 1], inplace=True)
print("after recoding values")
print(gss_df.HEALTH.value_counts(sort=False))
print("mean of HEALTH: ", round(gss_df['HEALTH'].mean(),3))

gss_df.to_csv('GSS1993_HealthRecoded.csv', index=False)



