# 3. Write a program to compare tuples of integers and tuples of strings.

tpl_int = (1,2,3,4,5)
print("First Tuple :",tpl_int)

tpl_str = ("A","B","C","D","E")
print("Second Tuple :",tpl_str)

if (tpl_int == tpl_str)==0:
    print("Both Tuple Are Different.")
else:
    print("Both Tuple Are Same.")
