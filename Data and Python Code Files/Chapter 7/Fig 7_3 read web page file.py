import urllib.request
import os
cwd = os.getcwd()

# The following line uses the urlopen function to open the webpage
webpage = urllib.request.urlopen\
    ('file:///' + cwd + '/hey_taxi_on_the_World_Wide_Web.html')

# The following line reads the first 60 characters from the html file
print(webpage.read(60))

