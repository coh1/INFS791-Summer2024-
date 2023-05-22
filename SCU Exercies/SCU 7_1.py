import urllib.request
# Modify the following line to use the urllib module to print the 
# title element from the https://data.cityofchicago.org/ webpage:
webpage = 

# iterate through each line in the webpage and search for the <title>:
for line in webpage:
    line = line.decode('utf-8')

    # Modify the following line to specify critera
    if '' in line:
        print(line)

