import numpy as np

# The next line creates a list of tuples that are percentiles
# and Household Incomes at the specified percentiles
hh_income = [(10, 14629), (20, 25600), (30, 37002),
            (40, 50000), (50, 63179), (60, 79542),
            (70, 100162), (80, 130000), (90, 184292)]

hh_income_array = np.array(hh_income)
# Modify the following lines to report the dimensions of the
# ndarray and the number of elements in it
print("dimensions of household income array: ", hh_income_array.shape)
print("number of elements in household income array: ", hh_income_array.size)

