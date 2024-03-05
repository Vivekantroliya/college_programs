# 2.write a program to input 2 numbers  and one arithmetic Operator.perform Operations as per arithmetic Operator which is given as input.

No1 = int(input("Enter First Number : "))
No2 = int(input("Enter Second Number : "))
Ope = input("Enter Arithmetic Operator Out Of + - * / : ")
          
if Ope == "+":
    Result = No1+No2
    
elif Ope == "-":
    Result = No1-No2
    
elif Ope == "*":
    Result = No1*No2
    
elif Ope == "/":
    Result = No1/No2
    
else:
    print("Invalid Operator...")

print(No1,Ope,No2,"=",Result)


