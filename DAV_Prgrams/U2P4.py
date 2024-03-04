# 4. Write a program to create a series to maintain three students’ names and SPI values.

import pandas as pd

#std_dic = {"name :" : ["Vivek","Om","Meet"], "spi :" : [9.43,7.5,8.46]}

std_dic =[9.43,7.5,8.46]

d = pd.Series(std_dic,index=["Vivek","Om","Meet"],name="Student_Data")

print(d)

print(type(d))
