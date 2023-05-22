import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

model_df = pd.read_csv("GSS1993less_happy.csv")
model_y = model_df[["UNHAPPY"]]
model_x = model_df[["WIDOWED", "DIVORCED",
              "SEPARATED", "NEVER_MARRIED"]]
x_train, x_test, y_train, y_test = train_test_split(model_x,
                        model_y, test_size=0.25, random_state = 7)

# Convert DataFrame to one-dimensional array
y_train = np.ravel(y_train)

# Construct logistic regression classifier
log_reg_classifier = LogisticRegression(solver='lbfgs').fit(x_train, y_train)

print("training score of logistic regression model: ")
print(round(log_reg_classifier.score(x_train, y_train),4),"\n")

print("testing score of logistic regression model: ")
print(round(log_reg_classifier.score(x_test, y_test),4),"\n")

# Construct list of predictions
unhappy_predict=log_reg_classifier.predict(x_test)
print("Predictions based on test data:")
print(unhappy_predict)
print("Number predicted to be unhappy:", sum(unhappy_predict))

