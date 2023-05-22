list_of_entries = []

entry = input("Please enter a list value, enter 'end' to stop: ")

while entry != "end":
    list_of_entries.append(entry)
    entry = input("Please enter a list value, enter 'end' to stop: ")

print("You entered", len(list_of_entries), "values")
print("The values you entered are: ", list_of_entries)

