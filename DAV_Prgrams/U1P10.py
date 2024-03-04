# 10. Write a program to prompt users to enter a Fibonacci sequence.

i = 0
j = 1
n = int(input("Enter A Fibonacci Sequence :"))

print("Fibonacci Sequence :",end=" ")
while i < n:
    print(i,end=" ")
    i, j = j, i + j