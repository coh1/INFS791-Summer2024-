from statistics import *

# The next line creates a list of taxi fares
taxi_fare_info=[10.20, 11.50, 3.25, 22.5, 16.25, 9,   \
              12.05, 8.85, 13.5, 7.75, 6.75, 13.75, \
              11.05, 12.85, 12.25, 6.05, 8.85, 6.25,\
              16.65, 13.05, 6.25, 7.85, 14.75, 7.25,\
              10.75, 15.25, 10.25, 13.25, 6.5, 7.75,\
              12.75, 8, 6.75, 3.25, 7.05, 6.65, 5.05]
# The following lines of code compute various statistics.
print("mean value: ", round(mean(taxi_fare_info), 2))
print("median value: ", median(taxi_fare_info))

# The following is exception handling for StatisticsError
try:
    print("mode value: ", mode(taxi_fare_info))
except StatisticsError:
    print("** Data does not have a unique mode **")
print("sample standard deviation: ", \
      round(stdev(taxi_fare_info), 2))
print("population standard deviation: ", \
      round(pstdev(taxi_fare_info), 2))

