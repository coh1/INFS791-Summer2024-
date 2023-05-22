import urllib.request
import os
cwd = os.getcwd()

webpage = urllib.request.urlopen\
    ('file:///' + cwd + '/hey_taxi_on_the_World_Wide_Web.html')

# The following loops through the lines of the webpage
#  and prints any line with the tag '<title>' in it.
for line in webpage:
    line = line.decode('utf-8')  
    if '<title>' in line:
       print(line)


