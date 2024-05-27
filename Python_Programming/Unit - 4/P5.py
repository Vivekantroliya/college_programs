# 5.Write a program to enter the name of 5 companies and
# its employee size and display as bar graph.

import matplotlib.pyplot as plt
import numpy as np
 
x = np.array(['Tata','Wipro','Infotech','Fintech Globe','Microsoft'])  
y = np.array([60,25,35,20,40])

plt.bar(x,y)
plt.xlabel("Companies")
plt.ylabel("Employee in Thousand")
plt.show()
