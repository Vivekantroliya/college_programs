# 2. Load the well-known Iris data set, which lists measurements 
# of petals and sepals of three iris species.
# Then plot the correlations between each pair using the .pairplot() method.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("iris.csv")
sns.pairplot(df, hue ='class')
plt.show()

