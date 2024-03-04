# 5. Write a program to create a data frame to maintain three students’
# names associated with their grades in three courses and then add a new
# column named Mean to maintain the calculated mean mark per course.
# Display the final data frame.

import pandas as pd

std_dic = {" Names " : ["Vivek","Om","Meet"], " MERN_Grade " : ['A+','A','A'], " MEAN_Grade " : ['A','B','A+'], " Full_Stack_Grade " : ['A','B','B']}

d = pd.DataFrame(std_dic,index=[1,2,3])

print(d)

print(type(d))

Mean_Marks = [95,96,90]

d['Mean_Marks'] = Mean_Marks

print(d)
