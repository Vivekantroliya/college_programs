# 9. Write a program to create a function which accepts 2 numbers
# and one arithmetic operator. Return the answer accordingly.

def Arithmetic(No1,No2,Ope):
    if Ope=="+":
        Result = No1+No2
    elif Ope=="-":
        Result = No1-No2
    elif Ope=="*":
        Result = No1*No2
    elif Ope=="/":
        Result = No1/No2
    else :  
        print("Invalid Operator Entered...")
    print(No1,Ope,No2,"=",Result)

No1 = float(input("Enter First Number : "))
No2 = float(input("Enter Second Number : "))
Ope = input("Enter Any Arithmetic Operator Out Of + - * / : ")

Arithmetic(No1,No2,Ope)
