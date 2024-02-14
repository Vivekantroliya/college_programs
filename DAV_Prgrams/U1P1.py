# 1. Write a Python script to prompt users to enter two values; 
# then perform the basic arithmetical operations of addition, 
# subtraction, multiplication and division on the values.

No1 = float(input("Enter First Number : "))
No2 = float(input("Enter Second Number : "))
Ope = input("Enter Any Arithmetic Operator Out Of + - * / : ")

if Ope=="+":
    Result = No1+No2
    print(No1,Ope,No2,"=",Result)
elif Ope=="-":
    Result = No1-No2
    print(No1,Ope,No2,"=",Result)
elif Ope=="*":
    Result = No1*No2
    print(No1,Ope,No2,"=",Result)
elif Ope=="/":
    Result = No1/No2
    print(No1,Ope,No2,"=",Result)
else :
    print("Invalid Operator Entered...")


