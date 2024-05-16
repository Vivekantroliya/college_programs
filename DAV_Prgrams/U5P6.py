# 6. Python program of Barplot with all parameters of a sample data.

import numpy as np
import matplotlib.pyplot as plt

subject = ['C', 'C++', 'Java','Python']
value=[20,25,23,30]

plt.figure(figsize = (5, 5))
barChart=plt.bar(subject, value)
barChart[0].set_color("Cyan")
barChart[1].set_color("greenyellow")
barChart[2].set_color("purple")
barChart[3].set_color("tomato")
plt.xlabel("subject offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different subjects")
plt.show()
