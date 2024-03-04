# 4. Write a Python program to prompt users to enter a Celsius 
# value; then convert Celsius to Fahrenheit, where T(°F) = T(°C) x 
# 1.8 + 32. Display the result.

temp_c = float(input("Enter Temperature in Celsius :"))

temp_f = temp_c * 1.8 + 32

print("Temperature in Fahrenheit Is",temp_f)