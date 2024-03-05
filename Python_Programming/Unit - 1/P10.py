# 10.Write a program to create 4 lambda functions which
# shall accept 2 numbers and one arithmetic operator.
# As per arithmetic operator related lambda functions shall be invoked.

Sum = lambda No1,No2 :No1+No2
Sub = lambda No1,No2 :No1-No2
Multi = lambda No1,No2 :No1*No2
Div = lambda No1,No2 :No1/No2

No1 = float(input("Enter First Number : "))
No2 = float(input("Enter Second Number : "))
Ope = input("Enter Any Arithmetic Operator Out Of + - * / : ")

if Ope=="+":
    Result = Sum(No1,No2)
elif Ope=="-":
    Result = Sub(No1,No2)
elif Ope=="*":
    Result = Multi(No1,No2)
elif Ope=="/":
    Result = Div(No1,No2)
else :
    print("Invalid Operator Entered...")

print(No1,Ope,No2,"=",Result)


