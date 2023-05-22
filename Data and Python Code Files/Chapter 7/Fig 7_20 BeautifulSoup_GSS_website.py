from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

# Assign the URL of interest to a variable
life_sat_url = "https://gssdataexplorer.norc.org/" \
     + "trends/Gender%20&%20Marriage?measure=happy&" \
	 + "print=true&response=Very+happy&breakdown=Total&table=true"

# Use the urlopen function to open the webpage
life_sat_html = urllib.request.urlopen(life_sat_url)

# Create the BeautifulSoup object 
html_to_parse = BeautifulSoup(life_sat_html, "html.parser")

# Create a list of tables 
tables_found = html_to_parse.find_all("table")
print("number of tables found: " + str(len(tables_found)))

# Create list of all the <th> tags in the second table that belong to the “nb” class
list_of_th_elements = tables_found[1].find_all("th", class_="nb")
yrs_list = []
for element in list_of_th_elements:
    yrs_list.append(element.text)

# Create list of just the div elements within the <td> tags
#  that belong to the “val” class
data_values_list = tables_found[1].find_all("td")
pct_values = []
for row in data_values_list:
    pct_value = row.find("div", class_="val")
    pct_values.append(pct_value.text)

# Create a DataFrame that combines the “years” list and the “percent values” list
pct_vhappy_by_yr = pd.DataFrame(list(zip(yrs_list, pct_values)))

# Change the column headings to more descriptive names
pct_vhappy_by_yr.columns = ["year", "pct_very_happy"]
print(pct_vhappy_by_yr.head(), "\n")

# Assign the “year” column to be the index of the table 
pct_vhappy_by_yr = pct_vhappy_by_yr.set_index("year")
print(pct_vhappy_by_yr.head(), "\n")

print("before conversion, dtypes:  ",pct_vhappy_by_yr.dtypes, "\n")

# Convert the DataFrame to a float type
pct_vhappy_by_yr = pct_vhappy_by_yr.astype(float)
print("after conversion, dtypes:  ",pct_vhappy_by_yr.dtypes, "\n")
print(round(pct_vhappy_by_yr.describe(), 2))

