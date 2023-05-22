# The next line creates an empty list
taxi_ride_info = []

# The following lines of code add values to a list.
taxi_ride_info.append("da7a62fce04")
taxi_ride_info.append(180)
taxi_ride_info.append(1.1)
taxi_ride_info.append(True)

taxi_ride_info.insert(2, True)  # This line adds a new value to the list at the third location

# The following line of code displays the values of the list objects
print("After appending 4 items and inserting item with True value: ", taxi_ride_info)

# The following line removes the first item that has the value True from the list
taxi_ride_info.remove(True)

# The following line of code displays the values of the list objects
print("After removing item with True value: ", taxi_ride_info)

# The following line of code removes the last item from the list and assigns it to a variable
item_removed = taxi_ride_info.pop()

# The following line of code displays the values of the list objects and item removed
print("After using the pop method, List: ", taxi_ride_info, "Item removed: ", item_removed)



