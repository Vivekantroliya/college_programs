# 7.Write a program which will allow user to enter 10 numbers
# and display largest odd number from them.
# It will display appropriate message in case if no odd number is found.

lst = []
for i in range(10):
    lst.append(int(input("Enter A Number :")))
print(lst)

lst_odd = []
lst_even = []

for i in lst:
    if i%2==0:
        lst_even.append(i)
    else :
        lst_odd.append(i)

if len(lst_odd) == 0:
    print("Odd Number Does Not Exist.")
else:
    print("Your Entered Odd Numbers :",lst_odd)
    print("Largest Odd Number Is",max(lst_odd))