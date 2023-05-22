import csv

total = 0.00
minimum = 10000
maximum = 0
line_number = 0

with open('taxi_1000.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for line in csv_reader:
        
        if line_number > 0:
            fare = float(line[10])
            total = total + fare
            trip_miles = float(line[5])
            trip_total = float(line[14])
            if (trip_total < minimum) and (trip_total > 0):
                minimum = trip_total
            if trip_miles > maximum:
                maximum = trip_miles

        line_number += 1

print(f"The total fare is {total}, and the average is {total/(line_number - 1)}")
print(f"The lowest total fare that was > $0 was {minimum}")
print(f"The maximum trip distance was {maximum}")

