# 1. Write a program to create a list of names; 
# then define a function to display all the elements 
# in the received list. Call the function to execute its 
# statements and display all names in the list.

lst = ['Vivek','Om','Meet','Vinay']

def show():
    print("Names In List :")
    print("---------------")
    for i in lst:
        print(i)
show()
