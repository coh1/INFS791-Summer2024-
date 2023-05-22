# First assign trip cost components to string variables
fare = "$5.25"
tip = "$2.00"
extras = "$1.00"

# The next use slicing to remove "$" from each string
fare = fare[1:]
tip = tip[1:]
extras = extras[1:]

# now add up float values and assign to trip_total variable
trip_total = float(fare) + float(tip) + float(extras)
print ("The total trip cost is: ", "$" + str(trip_total))


