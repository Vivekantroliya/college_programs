# 10. Write a program in python to find factorial of user entered number. (Use recursive Function)

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)

n = int(input("Enter A Number For Factorial :"))

print("Factorial Of",n,"Is",factorial(n))
