import statsmodels.formula.api as smf
import pandas as pd

model_df = pd.read_csv("GSS1993_UnhappyFinal.csv")

# Use the fit method of the statsmodels logit function to
#  construct the logistic regression model
model= smf.logit(formula="UNHAPPY ~ WIDOWED + DIVORCED + " +
                "SEPARATED + NEVER_MARRIED", data= model_df).fit()

# Print out the model summary information
print(model.summary())






