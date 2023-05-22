import numpy as np

# The next line creates a list of taxi fares
taxi_fare_info=[10.20, 11.50, 3.25, 22.5, 16.25, 9,   \
              12.05, 8.85, 13.5, 7.75, 6.75, 13.75, \
              11.05, 12.85, 12.25, 6.05, 8.85, 6.25,\
              16.65, 13.05, 6.25, 7.85, 14.75, 7.25,\
              10.75, 15.25, 10.25, 13.25, 6.5, 7.75,\
              12.75, 8, 6.75, 3.25, 7.05, 6.65, 5.05]
# The following line of code creates an ndarray named taxi_fare_array.
taxi_fare_array = np.array(taxi_fare_info)
print("data type of the elements : ",taxi_fare_array.dtype)
print("number of dimensions : ",taxi_fare_array.ndim)
print("dimensions : ",taxi_fare_array.shape)
print("number of elements : ", taxi_fare_array.size)

