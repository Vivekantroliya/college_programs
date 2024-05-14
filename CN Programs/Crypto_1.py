# 1. Write a program that contains a string with a value "Vivek".
# The program should XoR each character in this string with 0
# and display the result.

string = "Vivek"
result = ""
for char in string:
    #XoR the character with 0
    xor_char = chr(ord(char) ^ 0)
    result += xor_char
print(result)
