taxi_ride_info = ["da7a61d7910", 600, 0.1, "$11.25", "$2.45", "$1.00", "$14.70", 10, "Credit Card"]
loop_counter = 0

for taxi_val in taxi_ride_info:
    loop_counter = loop_counter + 1
    if type(taxi_val) is str:
        print("loop counter: ", loop_counter,"taxi variable: ", taxi_val)
    elif type(taxi_val) is bool:
        break
    else:
        continue
else:
    print("loop counter: ", loop_counter, "At end of for loop")

