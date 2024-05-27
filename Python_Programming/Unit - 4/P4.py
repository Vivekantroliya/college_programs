# 4.Write a program to enter the profit of 5 years
# and display the profit as line graph.

import matplotlib.pyplot as plt
import numpy as np
 
x = np.array([1, 2, 3, 4,5])  
y = np.array([20,25,15,20,40])
 
plt.plot(x, y)  
plt.xlabel("Years")
plt.ylabel("Profit in Percantage")
plt.show() 
