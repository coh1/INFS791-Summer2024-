import statsmodels.formula.api as smf
import pandas as pd

model_df = pd.read_csv("GSS1993_UnhappyFinal.csv")

model= smf.logit(formula="UNHAPPY ~ WIDOWED + DIVORCED + SEPARATED " +
                "+ NEVER_MARRIED + AGE + HEALTH + RINCOM91 + EDUC " +
                "+ MALE + BLACK + OTHER_RACE + TRAUMA1", data= model_df).fit()

print(model.summary())






