# The next two lines create a list and a string
list = ['a', 'ab', 'b', 'bc', 'c', 125, True, False, 125, 128]
string = 'This string has 35 characters in it'

# The following lines of code print the length of the sequences
print("length of list: ", len(list))
print("length of string: ", len(string))

# The following lines of code count how many times character "a" is in each
print("number of times 'a' in list: ", list.count('a'))
print("number of times 'a' in string: ", string.count('a'))

# The following lines of code determine if character "e" is in each
print("'e' is in list: ", 'e' in list)
print("'e' is in string: ", 'e' in string)

# The following lines of code print slice of elements in each
print("slice of 3rd to 7th elements of list: ", list[2:7])
print("slice of 3rd to 7th elements of string: ", string[2:7])

