
# 6.Write a program to read a file which contains only numbers.
# Display total of all numbers with maximum and minimum number.

file = open("num.txt", "r")

print(file.read())

file.seek(0)

con = file.readline()

lst = []
for line in con:
    if line.isdigit() == True:
        lst.append(int(line))

print("The Sum Of All Numbers Is",sum(lst))
print("Maximum Number Is",max(lst))
print("Minimum Number Is",min(lst))

file.close()