import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report

model_df = pd.read_csv("GSS1993less_happy.csv")
model_y = model_df[["WIDOWED"]]

model_x = model_df[["UNHAPPY","AGE","HEALTH", "RINCOM91", "EDUC", 
              "SEX","BLACK","OTHER_RACE","TRAUMA1"]]

x_train, x_test, y_train, y_test = train_test_split(model_x,
                        model_y, test_size = 0.25, random_state = 7)

print("Number test cases widowed:",sum(y_test.WIDOWED),"\n")

y_train = np.ravel(y_train)

# Construct MLP classifier
classifier = MLPClassifier(solver='lbfgs', alpha = 1,
                    hidden_layer_sizes=(2, 6),
                    random_state = 1).fit(x_train, y_train)

print("training score of NN model: ")
print(round(classifier.score(x_train, y_train),4),"\n")

print("testing score of NN model: ")
print(round(classifier.score(x_test, y_test),4),"\n")

widow_predict=classifier.predict(x_test)
print("Number of predicted widowed:",sum(widow_predict))

print(classification_report(y_test,widow_predict))

