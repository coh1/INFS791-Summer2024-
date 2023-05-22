import pandas as pd
gss_df = pd.read_csv('GSS1993_HealthRecoded.csv')
print("before recoding, marital values:")
print(gss_df.MARITAL.value_counts(sort=False),"\n")

# The following line replaces numeric code responses with category labels
gss_df.MARITAL.replace(to_replace=[1, 2, 3, 4, 5, 9],
                       value=["MARRIED","WIDOWED", "DIVORCED",
                              "SEPARATED","NEVER_MARRIED",
                              "MARRIED"], inplace=True)
print("after recoding, marital values:")
print(gss_df.MARITAL.value_counts(sort=False),"\n")
print(gss_df.head(),"\n")

# The following line creates a Pandas Series object from the MARITAL column
mar_series = gss_df.MARITAL

# The following line creates a new DataFrame with columns corresponding
#  to each category value in the Series
mar_dummies = pd.get_dummies(mar_series,columns=['MARITAL'])

print("after get_dummies, new mar_dummies DF:")
print(mar_dummies.head(),"\n")

# The following lines add the dummy columns of interest to the DataFrame
gss_df['DIVORCED'] = mar_dummies.DIVORCED
gss_df['WIDOWED'] = mar_dummies.WIDOWED
gss_df['SEPARATED'] = mar_dummies.SEPARATED
gss_df['NEVER_MARRIED'] = mar_dummies.NEVER_MARRIED

# The following line drops the original MARITAL column from the DataFrame
gss_df = gss_df.drop(columns=['MARITAL'])
print("columns: ",gss_df.columns,"\n")
print("after adding dummy fields to gss_df:")
print(gss_df.head())

gss_df.to_csv('GSS1993_HealthAndMaritalRecoded.csv', index=False)



