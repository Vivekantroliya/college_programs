# 2. Write a program to read text file data and 
# create a dictionary of all keywords in the text file. 
# The program should count how many times each word is repeated 
# inside the text file and then find the keyword with a highest repeated number.
# The program should display both the keywords dictionary and the most repeated word.

file = open("abc.txt",'r')

data = file.read()

print(data)

count = 0

for i in data:
    if i == 'Apple':
        count += 1

print(count)
