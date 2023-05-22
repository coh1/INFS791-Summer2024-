# Add a line of Python code to associate the file "samplefile.txt"
#  with a file object variable named sample_file in order to read from the file
sample_file = open("samplefile.txt", mode = "r")

line_count = 0
for line in sample_file:
    line_count = line_count + 1

print(f"There are {line_count} lines of text in the file")

