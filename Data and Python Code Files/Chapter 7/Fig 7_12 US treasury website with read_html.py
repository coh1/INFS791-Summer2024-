import pandas as pd

# The following line assigns the URL of interest to a variable
us_treasury_url = "https://www.treasury.gov/resource-center/data-chart-center" \
                + "/interest-rates/pages/TextView.aspx?data=yieldYear&year=2018"

#  The following line uses the Pandas read_html function to read all
#   the HTML tables from the webpage and create a list of DataFrame objects.
tables = pd.read_html(us_treasury_url)

int_rate_table = tables[1]
print(int_rate_table.columns)

print("The first 5 rows of data are:")
print(int_rate_table.head())

print("The last 5 rows of data are:")
print(int_rate_table.tail())




