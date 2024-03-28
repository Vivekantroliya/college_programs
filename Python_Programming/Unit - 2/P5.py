# 5.Write a program to read a file and display its contents.
# At the end it shall also display no. of words available in file.

file = open("abc.txt", "r")

print(file.read())

file.seek(0)

abc = file.read().split()

print("Word Count In File Is",len(abc))

file.close()