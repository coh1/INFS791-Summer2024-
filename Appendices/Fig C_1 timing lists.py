import time
num_elements = 5000000   #Specify number elements to be 5 million

list_words=[]

start_time = time.time()
#create list of num_elements words
for index in range(num_elements):
    list_words.append("ABCDE")
end_time = time.time()
print("Time to create list: ", end_time - start_time)

#time to create new list with length of words
list_len = []
start_time = time.time()

for word in list_words:
    list_len.append(len(word))
end_time = time.time()
print("Time to create list of lengths with loop: ", end_time - start_time)

#time to create new list with length of words with list comprehension
list_len2 = []
start_time = time.time()

list_len2=[len(word) for word in list_words]

end_time = time.time()
print("Time to create list of lengths with comprehension: ", end_time - start_time)

if list_len == list_len2:
    print("Lists are found to be equal")

