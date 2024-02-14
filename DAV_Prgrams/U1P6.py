# 6. Write a program to prompt users to enter a value;then check 
# whether the entered value is positive or negative value and 
# display a proper message.

No1 = float(input("Enter A Number : "))

if No1<0:print(No1," Is A Negative Number.")

elif No1>0:print(No1,"Is A Positive Number.")
    
else:print("Number Is Zero(0).")
