# 8. Write a Python program to perform following operation on given string input:
# a) Count Number of Vowel in given string
# b) Count Length of string (do not use Len ())
# c) Reverse string
# d) Find and replace operation
# e) check whether string entered is a palindrome or not

string = input("Enter A String :")

count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

for i in string.lower():
    if i == 'a':
        count_a += 1
    if i == 'e':
        count_e += 1
    if i == 'i':
        count_i += 1
    if i == 'o':
        count_o += 1
    if i == 'u':
        count_u += 1

print("Vowel 'a' Is Repeated",count_a,"Times.")
print("Vowel 'e' Is Repeated",count_e,"Times.")
print("Vowel 'i' Is Repeated",count_i,"Times.")
print("Vowel 'o' Is Repeated",count_o,"Times.")
print("Vowel 'u' Is Repeated",count_u,"Times.")

count = 0

for i in string:
    if i in string:
        count += 1
print("Length Of Word Is",count)

print("Reverse String : ",end="")
for i in string[::-1]:
    print(i,end="")

print()
print("'i' Is Found At",string.find("i"))

print("'i' Is Replaced With 'a' And New String Is",string.replace('i','a'))

if string == string[::-1]:
    print(string,"Is Palindrome.")
else:
    print(string,"Is Not Palindrome.")
