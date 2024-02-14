# 2. Write a Python script to prompt users to enter the first and last 
# values and generate some random values between the two 
# entered values.

import random

No1 = int(input("Enter First Number : "))
No2 = int(input("Enter Last Number : "))

No3 = random.randint(No1,No2)

print("Random Value Between ",No1," And ",No2," Is ",No3,".")