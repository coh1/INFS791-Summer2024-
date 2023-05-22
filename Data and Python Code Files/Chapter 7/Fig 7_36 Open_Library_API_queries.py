import requests

# Obtain the JSON data of records with the word "taxi" in the title
search_results = requests.get("http://openlibrary.org/search.json?title=taxi").json()

print(search_results["num_found"])

# Use exception handling to skip records with no author name
for item in search_results["docs"]:
    try:
        print(item["title_suggest"] + " by " + item["author_name"][0])
    except:
        continue

