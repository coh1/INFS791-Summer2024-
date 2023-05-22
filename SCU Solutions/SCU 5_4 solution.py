sample_file = open("samplefile.txt", mode = "r")

line_count = 0
for line in sample_file:
    line_count = line_count + 1

sample_file_info = open("samplefileinfo.txt", mode = "w")

# Add a line of Python code to write the message "There are ### lines of text
#  in the file" (where ### are the number of lines of text in the file
#  "samplefile.txt" to the file named "samplefileinfo.txt"
#  using the file object variable sample_file_info
sample_file_info.write(f"There are {line_count} lines of text in the file")

sample_file_info.close()

