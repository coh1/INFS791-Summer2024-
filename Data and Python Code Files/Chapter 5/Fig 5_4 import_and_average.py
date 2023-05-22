file = open("numbers.txt")
total = 0
line_count = 0
for line in file:
    value = int(line)
    total = total + value
    line_count = line_count + 1
print(f"The sum is {total}, and the average is {total/line_count}")

