import csv

# read from the SCU 5_2.csv file using csv_reader from the csv module
# and print all the lines
with open("SCU 5_2.csv") as file:
    csv_reader = csv.reader(file, delimiter = ",")
    for line in csv_reader:
        print(line)

