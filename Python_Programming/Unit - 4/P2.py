# 2.Write a program to load above excel file and display following information
# - List of students from Rajkot City
# - List of Male students
# - List of Male students from Rajkot City 
# - List of students whose age >= 20

import pandas as pd

df=pd.read_excel('stud.xlsx')

print(df[df["City"]=='Rajkot'])

print(df[df['Gender']=='Male'])

print(df.loc[(df['City']=='Rajkot') & (df['Gender']=='Male')])

print(df[df['Age']>=20])
