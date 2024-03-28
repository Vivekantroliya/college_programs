# 2.Write a program to execute user defined exception in python.

class InvalidAge(Exception):
   message = "You Are Not Eligible For Voting."
   pass
   
try:
   age = int(input("Enter Your Age : "))
   if age < 18 :
      raise InvalidAge
except InvalidAge as e:
   print(e.message)
else:
   print("You Are Eligible For Voting.")