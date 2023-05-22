import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report

model_df = pd.read_csv("GSS1993less_happy.csv")

model_y = model_df[["HEALTH"]]
model_x = model_df[["EDUC", "SEX", "TRAUMA1", "WIDOWED"]]

x_train, x_test, y_train, y_test = train_test_split(model_x, model_y,
                                                    test_size=0.25, random_state = 15)
y_train = np.ravel(y_train)

# create an MLPClassifier with 'lbfgs' solver
# experiment with alpha, hidden_layer_sizes, and random_state
# and see how the results change
classifier = MLPClassifier(solver = 'lbfgs', alpha = 1, hidden_layer_sizes = (2, 3),
                           random_state = 25).fit(x_train, y_train)

print("training score of logistic regression model: ")
print(round(classifier.score(x_train, y_train), 4), "\n")

print("testing score of logistic regression model: ")
print(round(classifier.score(x_test, y_test), 4), "\n")

health_predict = classifier.predict(x_test)
print("Predictions based on test data: ")
print(health_predict)

print(classification_report(y_test, health_predict))

