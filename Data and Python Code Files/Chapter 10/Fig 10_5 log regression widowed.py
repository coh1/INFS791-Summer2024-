import pandas as pd
import statsmodels.formula.api as sm

model_df = pd.read_csv("GSS1993less_happy.csv")

model= sm.logit(formula="WIDOWED~ UNHAPPY " +
                "+ AGE + HEALTH + RINCOM91 + EDUC " +
                "+ SEX + BLACK + OTHER_RACE + TRAUMA1",
                data= model_df).fit()
print(model.summary())

