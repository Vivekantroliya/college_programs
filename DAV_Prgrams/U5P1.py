#1. Create 300 random temperature readings for sixcities over 
# a season and then plot the generated datausing Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt
import random

temp1 = list(random.sample(range(0,100), 50))
temp2 = list(random.sample(range(0,100), 50))
temp3 = list(random.sample(range(0,100), 50))
temp4 = list(random.sample(range(0,100), 50))
temp5 = list(random.sample(range(0,100), 50))
temp6 = list(random.sample(range(0,100), 50))

Cities={'Mumbai':temp1,'Hydrabad':temp2,'Pune':temp3,'Shimla':temp4,'Delhi':temp5,'Banglore':temp6}
df=pd.DataFrame(Cities)
df.plot(kind='line')
plt.legend(loc="upper right",fontsize=5)
plt.show()
