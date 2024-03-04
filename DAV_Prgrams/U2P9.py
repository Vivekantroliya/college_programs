# 9. Write a program in python to find factorial of user entered number.

n = int(input("Enter A Number For Factorial :"))
n1=n
f = 1
while n>0:
    f = f*n
    n = n-1
print("Factorial Of",n1,"Is",f)


