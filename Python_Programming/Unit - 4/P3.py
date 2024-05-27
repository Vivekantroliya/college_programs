# 3.Write a program to load above excel file and use
# dropna() and fillna() functions separately.

import pandas as pd

df=pd.read_excel('student.xlsx')
print(df)

df['Gender'].fillna('Male',inplace=True)
print(df)

df=pd.read_excel('stud.xlsx')
new =df.dropna()
print(new)
