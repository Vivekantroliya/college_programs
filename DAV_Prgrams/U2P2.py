# 2. Write a program to read text file data and 
# create a dictionary of all keywords in the text file. 
# The program should count how many times each word is repeated 
# inside the text file and then find the keyword with a highest repeated number.
# The program should display both the keywords dictionary and the most repeated word.

from collections import Counter

file = open("abc.txt",'w+')

file.write("I Am Vivek \nI Am Student Of Marwadi University")

file.seek(0)

text = file.read()

print("File Read...")
print(text)

data = text.split()

# Create a dictionary of words and their counts using the Counter function
count = Counter(data)

# Find the word with the highest count
Common = count.most_common(1)[0][0]

# Print the dictionary of words and their counts
print("All Words And Their Counts :",count)

# Print the most common word
print("Most Common Word In File :",Common)

file.close()
