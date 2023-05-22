import pandas as pd
gss_df = pd.read_csv('GSS1993_HappyReponse.csv')

print("before recoding: ")
print(gss_df.head())

# The following lines recode the HAPPY column values to be 0 if
#  the response was less than 3 and to be 1 if the response was 3
gss_df.loc[gss_df.HAPPY < 3, 'HAPPY'] = 0
gss_df.loc[gss_df.HAPPY == 3, 'HAPPY'] = 1

# The following line renames the HAPPY column to be UNHAPPY
gss_df.rename(columns={"HAPPY": "UNHAPPY"}, inplace=True)
print("after recoding: ")
print(gss_df.head())

print("mean of UNHAPPY: ", round(gss_df['UNHAPPY'].mean(),3))

gss_df.to_csv('GSS1993_UnhappyRecoded.csv', index=False)



