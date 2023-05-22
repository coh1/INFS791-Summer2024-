import pandas as pd
gss_df = pd.read_csv('GSS1993_9Fields.csv')
print("Before removing non-responses, rows: ", gss_df['HAPPY'].count())

# The following line removes all records where HAPPY > 3
gss_df = gss_df[gss_df.HAPPY <= 3]
print("after removing non-responses, rows: ", gss_df['HAPPY'].count())

gss_df.to_csv('GSS1993_HappyReponse.csv', index=False)





