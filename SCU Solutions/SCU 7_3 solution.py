from bs4 import BeautifulSoup
import urllib.request
import os
cwd = os.getcwd()

AudioBooksFile = "file:///"+cwd+"\Audiobooks.html"

Audio_Books_html = urllib.request.urlopen(AudioBooksFile)

html_to_parse = BeautifulSoup(Audio_Books_html, "html.parser")

# Modify the following line of code to create a list of audiobooks found in the webpage:
List_of_Audiobooks_found = html_to_parse.find_all("li")

Audiobookslist = []
for element in List_of_Audiobooks_found:
    Audiobookslist.append(element.text)
    
print("number of Audiobooks found: " + str(len(Audiobookslist)))

print("The first book on the list is: ", Audiobookslist[0])

