# 7.Write a program to copy a text file using file handling mechanism.

file1 = open("file1.txt", "r")

file2 = open("file2.txt", "w")

file2.write(file1.read())

print("File1 Is Copied Successfully Into File2.")

file1.close()

file2.close()