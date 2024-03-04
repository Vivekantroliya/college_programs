# 6.Write a program in python to swap two variables without using temporary variable.

No1 = int(input("Enter First Number For Swap :"))
print("Entered First Number :",No1)

No2 = int(input("Enter Second Number For Swap :"))
print("Entered Second Number :",No2)

print("Number Swapped.")
No1 = No1+No2
No2 = No1-No2
No1 = No1-No2

print("First Number After Swapping :",No1)
print("Second Number After Swapping :",No2)
