import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

model_df = pd.read_csv("taxi_df_cleaned_with_dummies.csv")

# modify the following two lines of code so that
# Tipgt5 is modeled as a function of Fare, Trip Miles, and CreditCard
model_y = model_df[[     ]]
model_x = model_df[[     ]]

x_train, x_test, y_train, y_test = train_test_split(model_x, model_y, test_size=0.25, random_state = 30)

y_train = np.ravel(y_train)
log_reg_classifier = LogisticRegression(solver='lbfgs').fit(x_train, y_train)

print("training score of logistic regression model: ")
print(round(log_reg_classifier.score(x_train, y_train), 4), "\n")

print("testing score of logistic regression model: ")
print(round(log_reg_classifier.score(x_test, y_test), 4), "\n")

high_tipper = log_reg_classifier.predict(x_test)
print("Predictions based on test data: ")
print(high_tipper)
print("Number predicted to be a high tipper: ", sum(high_tipper))

