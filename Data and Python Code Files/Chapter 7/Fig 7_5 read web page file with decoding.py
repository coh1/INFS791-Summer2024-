import urllib.request
import os
cwd = os.getcwd()

webpage = urllib.request.urlopen\
    ('file:///' + cwd + '/hey_taxi_on_the_World_Wide_Web.html')

# The following line reads and prints the decoded html file
print(webpage.read().decode('utf-8'))

