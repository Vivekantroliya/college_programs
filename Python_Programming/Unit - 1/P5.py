# 5.Write A Program To Enter 10 Numbers And Display Largest Odd Number From The Entered Number.

lst=[]
for i in range(0,10):
    n = int(input("Enter Numbers : "))
    lst.append(n)

print(lst)

for j in lst:
    if j%2==0:
        lst.remove(j)

print(max(lst))
        



