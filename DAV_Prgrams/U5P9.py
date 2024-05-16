# 9. Python program of Line Plot with all parameters of a sample data.

import matplotlib.pyplot as plt

x = [1, 2, 2.5, 3, 6]
y = [20,30,40,50,60]

plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='^', linestyle='-')
plt.xlabel('Income in Lakhs')
plt.ylabel('Age in Years')
plt.grid(True)
plt.show()
