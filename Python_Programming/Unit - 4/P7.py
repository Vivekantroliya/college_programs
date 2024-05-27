# 7.Write a program to read above excel file and how many
# male and female students are there using bar graph.

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel('student.xlsx')

Male=df['Gender'].value_counts()['Male']
Female=df['Gender'].value_counts()['Female']

data = {'Male':Male, 'Female':Female}
courses = list(data.keys())
values = list(data.values())

plt.bar(courses,values,color ='orange', width = 0.4)
plt.xlabel("Gender")
plt.ylabel("Ratio of Male-Female")
plt.show()
