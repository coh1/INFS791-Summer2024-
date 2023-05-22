import pandas as pd

# read the table at the following URL:
trips_update_url = "http://dev.cityofchicago.org/open%20data/data%20portal/2019/07/01/taxi-dataset-relaunch.html"

# use the Pandas module to read the HTML of the page:
tables = 

# The webpage has two tables. Read the first table into update_table object:
update_table = 

# The following prints out table information
print(update_table.columns)
print("The first five rows of data are:")
print(update_table.head())
print("The last five rows of data are:")
print(update_table.tail())
print("Summary statistics of the dataset are:")
print(update_table.describe())

