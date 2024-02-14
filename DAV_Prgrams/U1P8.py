# 8. Write a program to prompt users to enter an age; then check 
# whether each person is a child, a teenager, an adult, or a senior. 
# Display a proper message.

Age = float(input("Enter Your Age : "))

if Age>=0 and Age<=3 :
    print("You Are Toddler.")

elif Age>=4 and Age<=12 :
    print("You Are Child.")

elif Age>=13 and Age<=17 :
    print("You Are Teenager.")

elif Age>=18 and Age<=54 :
    print("You Are Adult.")

elif Age>=55 :
    print("You Are Senior.")

else :
    print("Invalid Age Entered...")
