import xlrd
import pandas as pd
from IPython.display import display

# Write a Python script to read the data in an Excel file named
# movies.xls and save this data in a DataFrame called Movies.
# Perform the following steps:

# 1. Read the contents of the second sheet that is named 2000s in the Excel
# file (movies.xls) and store this content in a DataFrame called Second_Sheet.

print("\n------------------Read Data From Excel File------------------\n")

Movies = pd.read_excel('movies.xls',sheet_name='2000s')

print(Movies)

print("\n------------------Print Column Name------------------\n")

print(Movies.columns)

# 2. Write the code needed to show the first seven rows from
# the data frame Second_sheet using an appropriate method.

print("\n------------------Display First Seven Rows------------------\n")

print(Movies.head(7))

# 3. Write the code needed to show the last five rows using an appropriate method.

print("\n------------------Display Last Five Rows------------------\n")

print(Movies.tail())

# 4. Use a suitable command to show only one column that is named Budget.

print("\n------------------Show Only One Column Named 'Budget'-----------------\n")

print(Movies["Budget"])

# 5. Use a suitable command to show the total rows in the first sheet that is called 1900s.

print("\n-----------------Display Numbers Of Rows In First_Sheet Named '1900s'-----------------\n")

First_Sheet = pd.read_excel("movies.xls",sheet_name="1900s")

print(First_Sheet.shape)

print("Number Of Rows Are",First_Sheet.shape[0])

print("Number Of Columns Are",First_Sheet.shape[1])

# 6. Use a suitable command to show the maximum value stored in the Budget column.

print("\n-----------------Maximum Value In 'Budget' Column-----------------\n")

print(Movies['Budget'].max())

# 7. Use a suitable command to show the minimum value stored in the Budget column.

print("\n-----------------Minimum Value In 'Budget' Column-----------------\n")

print(Movies['Budget'].min())

# 8. Write a single command to show the details
# (count, min, max, mean, std, 25%, 50%, 75%)
# about the column User Votes.

print("\n-----------------Count,Min,Max,Std,25%,50%,75% Of User Votes-----------------\n")

print(Movies['User Votes'].describe())

# 9. Use a suitable conditional statement that stores the rows in which the country
# name is USA and the Duration value is less than 50 in a data frame named USA50.
# Show the values in DataFrame USA50.

print("\n-----------------Data Of 'Country' USA And 'Duration' Less Than 50-----------------\n")

USA50 = Movies[(Movies['Country']=='USA') & (Movies['Duration']<50)]

print(USA50)

# 10. Using a suitable command, create a calculated column named Avg Reviews
# in Second_sheet by adding Reviews by Users and Reviews by Critics and divide it by 2.
# Display the first five rows of the Second_sheet after creating the previous calculated column.

print("\n-----------------Create Avg Reviews Columns Of Users And Critics-----------------\n")

Movies['Avg Review'] = (Movies['Reviews by Users']+Movies['Reviews by Crtiics'])/2

print(Movies)

# 11. Using a suitable command, sort the Country values in ascending order
# (smallest to largest) and Avg_reviews in descending order (largest to smallest).

print("\n-----------------Sorted Country Values In Ascending Order-----------------\n")

Sort_Country = Movies.sort_values(by='Country', ascending=True)

print(Sort_Country.head())

print("\n-----------------Sorted Avg_Reviews In Descending Order-----------------\n")

Sort_Avg_Review = Movies.sort_values(by='Avg Review', ascending=False)

print(Sort_Avg_Review.tail())
