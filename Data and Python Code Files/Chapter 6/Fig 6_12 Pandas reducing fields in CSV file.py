import pandas as pd
gss_df = pd.read_csv('GSS1993.csv')
print(gss_df.describe(),"\n")
# The following line creates a DataFrame with a subset of fields
gss_subset_df = gss_df[['HAPPY','AGE','HEALTH',
                        'RINCOM91','EDUC', 'SEX',
                        'RACE', 'TRAUMA1', 'MARITAL']]
print(gss_subset_df.describe(),"\n")

print(gss_subset_df.head())
# The following line saves the new DataFrame to a CSV file
gss_subset_df.to_csv('GSS1993_9Fields.csv', index=False)



