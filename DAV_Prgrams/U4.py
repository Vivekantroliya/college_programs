import numpy as np
import pandas as pd
from IPython.display import display

# 1. Create a DataFrame called df from the following tabular data dictionary
# that has these index labels: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j'].

Data = {"Animal" : ['Cat','Cat','Snake','Dog','Dog','Cat','Snake','Cat','Dog','Dog'],
             "Age" : [2.5,3.0,0.5,np.nan,5.0,2.0,4.5,np.nan,7,3],
             "Priority" : ['Yes','Yes','No','Yes','No','No','No','Yes','No','No'],
             "Visits" : [1,3,2,3,2,3,1,1,2,1]}

Labels = ['a','b','c','d','e','f','g','h','i','j']

print("\n------------------Create DataFrame From Dictionary------------------\n")

DF = pd.DataFrame(Data,index=Labels)

display(DF)

# 2. Display a summary of the data frame’s basic information.

print("\n------------------Basic Information Of DataFrame------------------\n")

print(DF.info())

# 3. Return the first three rows of the data frame df.

print("\n------------------Display First Three Rows------------------\n")

print(DF.head(3))

# 4. Select just the animal and age columns from the data frame df.

print("\n------------------Display 'Animal' And 'Age' Columns------------------\n")

print(DF[["Animal","Age"]])

# 5. Count the visit priority per animal.

print("\n------------------Count The Visit Priority Per Animal------------------\n")

Grp = DF.groupby("Priority")

for i in Grp:
    print(i)

# 6. Find the mean of the animals’ ages.

print("\n------------------Mean Of Animals' Ages------------------\n")

print("Mean Of Age Is :",DF["Age"].mean())

# 7. Display a summary of the data set.

print("\n------------------Display A Summary Of DataFrame------------------\n")

print(DF.describe())

# 8. Return the first three rows of the data frame df.

print("\n------------------Using iloc Display First Three Rows------------------\n")

print(DF.iloc[:3])

# 9. Extract first and last column in one table.

print("\n------------------Display First And Last Column------------------\n")

print(DF.iloc[ : ,[0,-1]])

# 10. Observe output of ndim(),shape().

print("\n------------------Output Of 'ndim' For Number Of Dimension------------------\n")

print(DF.ndim)

print("\n------------------Output Of 'shape' For Rows And Columns------------------\n")

print(DF.shape)

