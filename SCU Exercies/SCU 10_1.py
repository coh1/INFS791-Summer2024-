import pandas as pd
from sklearn.model_selection import train_test_split

model_df = pd.read_csv("GSS1993less_happy.csv")

model_y = model_df[["UNHAPPY"]]

model_x = model_df[["HEALTH", "EDUC", "TRAUMA1", "NEVER_MARRIED"]]

# Modify the following line of code so it calls train_test_split with
# a test_size of 0.2 and uses the random_state of your choosing
x_train, x_test, y_train, y_test = 

# Print the number of records in each set:
print("x_train has ", len(x_train), " records")
print("x_test has ", len(x_test), " records")
print("y_train has ", len(y_train), " records")
print("y_test has ", len(y_test), " records")

