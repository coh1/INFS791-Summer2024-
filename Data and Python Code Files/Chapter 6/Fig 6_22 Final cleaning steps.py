import pandas as pd
gss_df = pd.read_csv('GSS1993_HealthAndMaritalRecoded.csv')

# The next line replaces multiple values in RINCOM91 column
gss_df.RINCOM91.replace(to_replace=[0,22,98,99],
                        value=[12.33,12.33,12.33,12.33],inplace=True)

gss_df.EDUC.replace(to_replace=98, value=13.05, inplace=True)

gss_df.SEX.replace(to_replace=2, value=0, inplace=True)
gss_df.rename(columns={"SEX": "MALE"}, inplace=True)

gss_df.RACE.replace(to_replace=[1, 2, 3],
                       value=["WHITE","BLACK", "OTHER_RACE"],
                              inplace=True)

race_series=gss_df.RACE
# The next line creates dummy variables for RACE category
race_dummies = pd.get_dummies(race_series,columns=['RACE'])
gss_df['BLACK'] = race_dummies.BLACK
gss_df['OTHER_RACE'] = race_dummies.OTHER_RACE
gss_df=gss_df.drop(columns=['RACE'])

gss_df.TRAUMA1.replace(to_replace=[-1,2,3,9],
                        value=[0,1,1,0],inplace=True)
print("after recoding values")
print("mean of RINCOM91: ", round(gss_df['RINCOM91'].mean(),3))
print("mean of EDUC: ", round(gss_df['EDUC'].mean(),3))
print("mean of MALE: ", round(gss_df['MALE'].mean(),3))
print("mean of BLACK: ", round(gss_df['BLACK'].mean(),3))
print("mean of OTHER_RACE: ", round(gss_df['OTHER_RACE'].mean(),3))
print("mean of TRAUMA1: ", round(gss_df['TRAUMA1'].mean(),3))

gss_df.to_csv('GSS1993_UnhappyFinal.csv', index=False)

