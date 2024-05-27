# 6.Write a program to enter age of 50 students and
# create a histogram to display age as group of
# 0-10, 11-20, 21-30, 31-40, 41-50, 51-60, 60-120

import matplotlib.pyplot as plt
import random

lst=[]

for i in range(0,50):
    n= random.randint(0,120)
    lst.append(n)

bins = [0,10,20,30,40,50,60,120]

plt.hist(lst, bins, histtype='bar',rwidth=0.9)
plt.xlabel('Age Groups') 
plt.ylabel('Number of People') 
plt.title('Histogram') 
plt.show()
