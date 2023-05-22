import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

model_df = pd.read_csv("GSS1993less_happy.csv")
model_y = model_df[["WIDOWED"]]
model_x = model_df[["UNHAPPY","AGE","HEALTH", "RINCOM91", "EDUC", 
              "SEX","BLACK","OTHER_RACE","TRAUMA1"]]
x_train, x_test, y_train, y_test = train_test_split(model_x,
                        model_y, test_size=0.25, random_state = 7)
print("Number training cases widowed:",sum(y_train.WIDOWED),"\n")
print("Number test cases widowed:",sum(y_test.WIDOWED),"\n")

y_train = np.ravel(y_train)

# Construct logistic regression classifier using up to 1000 iterations
log_reg_classifier = LogisticRegression(solver='lbfgs',
                            max_iter=1000).fit(x_train, y_train)

print("training score of logistic regression model: ",
      round(log_reg_classifier.score(x_train, y_train),4),"\n")

print("testing score of logistic regression model: ",
      round(log_reg_classifier.score(x_test, y_test),4),"\n")

widow_predict=log_reg_classifier.predict(x_test)
print("Predictions based on test data:")
print(widow_predict,"\n")
print("Number of predicted widowed:",sum(widow_predict))

# Print out classification report
print(classification_report(y_test,widow_predict))

