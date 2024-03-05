# 12.Write a program to display the use of local, global and nonlocal variables.

# Local Variable

def local():
    message = 'I Am Local Variable.'
    print("Local Variable 'message' :",message)
local()

try:
    print(message)
except NameError as e :
    print("After Calling 'message' Variable Outside The Function Error :",e)
    
# Global Variable

str1 = "Global"

def global_var():
    str1 = "Local"
    print("Local Variable 'str1' :",str1)
global_var()

print("Global Variable 'str1' :",str1)

# Nonlocal Variable

def outer():
    msg = "Hello"
    print("Outer Function Variable:",msg)
    def inner():
        nonlocal msg
        msg = "Hii"
        print("Inner Function Variable:",msg)
    inner()
    print("After Use Of 'nonlocal' Keyword Outer Function Variable:",msg) 

outer()
