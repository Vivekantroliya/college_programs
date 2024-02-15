# write  a program to enter 10 numbers and display all armstrong numbers from those numbers.

num = int(input("Enter Numbers For Check Armstrong Number : "))

sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum = sum + pow(digit,3)
    temp = temp // 10

if num == sum:
    print(num,"Is An Armstrong Number.")

else:
    print(num,"Is Not An Armstrong Number.")
