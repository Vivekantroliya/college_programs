import pandas as pd
#dropna
# Load the Excel file
df = pd.read_excel('student_records.xlsx')

newdf = df.dropna()
print(newdf)

#fillna

df = pd.read_excel('student_records.xlsx')
newf=df.fillna(1111)
print(newf)
#output
#       RollNo    Name   Gender                 E-Mail     MobileNo.     Age               City
# 20     121      Dhruv   1111                   1111     1.111000e+03     1111.0               1111
