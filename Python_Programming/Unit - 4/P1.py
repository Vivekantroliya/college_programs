# 1.Write a program to load above excel file and display columns
# of file and data type of each column.

import pandas as pd

df=pd.read_excel('student.xlsx')

print(df.columns.ravel())

print(df.dtypes)
