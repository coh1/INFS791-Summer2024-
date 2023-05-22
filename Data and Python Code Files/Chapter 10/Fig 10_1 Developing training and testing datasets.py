import pandas as pd
from sklearn.model_selection import train_test_split

model_df = pd.read_csv("GSS1993less_happy.csv")

model_y = model_df[["UNHAPPY"]]
print("Descriptive Statistics for entire dataset:")
print(model_y.describe(),"\n")

model_x = model_df[["WIDOWED", "DIVORCED",
              "SEPARATED"]]

# Divide data into testing and training datasets
x_train, x_test, y_train, y_test = train_test_split(model_x,
                        model_y, test_size=0.25, random_state = 7)

print("Descriptive Statistics for training dataset:")
print(y_train.describe(),"\n")
print("Number training cases unhappy:",sum(y_train.UNHAPPY),"\n")

print("Descriptive Statistics for testing dataset:")
print(y_test.describe(),"\n")
print("Number test cases unhappy:",sum(y_test.UNHAPPY),"\n")

