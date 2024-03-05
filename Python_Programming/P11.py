# 11.Write a program to create function which shall accept any number
# of arguments and display total of all the numbers given as argument.

def Any(*n):
    total = sum(n)
    print("Total Of All Numbers Is",total)

Any(10,20,30,40,50)

Any(90,80,70)

Any(80,50,20,30,40)
