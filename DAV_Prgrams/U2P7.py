# 7.Write a program which will allow user to enter 10 numbers
# and display largest odd number from them.
# It will display appropriate message in case if no odd number is found.

lst = []

for i in range(10):
    lst.append(int(input("Enter A Number :")))
print(lst)

for i in lst:
    if i%2==0:
        lst.remove(i)

print("Your Entered Odd Numbers :",lst)
print("Largest Odd Number Is",max(lst))
