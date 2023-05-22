import statsmodels.formula.api as smf
import pandas as pd

model_df = pd.read_csv("GSS1993_HealthDummy.csv")

# Modify the following line to specify a logistic regression model that estimates
# the likelihood of a respondent being healthy (variable HEALTHY = 1).
model= smf.logit(formula="                     ", data= model_df).fit()

print(model.summary())






