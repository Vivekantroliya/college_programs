# 5.Create a Temperature class. Create 2 methods
# named convertFarenheit() and convertCelsius().

class temperature:
    def __init__(self,temp):
        self.temp=temp
    def convertFarenheit(self):
        result = float((self.temp*9/5)+32)
        return result
    def convertCelsius(self):
        result = float((self.temp-32)*5/9)
        return result
    
input_temp1 = float(input("Input temp in celsius :"))
temp1 = temperature(input_temp1)
print(temp1.convertFarenheit())

input_temp2 = float(input("Input temp in Farenheit :"))
temp2 = temperature(input_temp2)
print(temp2.convertCelsius())
