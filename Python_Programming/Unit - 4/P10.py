# 10.Write a program to read above file and use regular expression to 
# display only those records who have mobile number with country code. 
# For example, 91-9999933333 (2 digits of country code and 10 digits of mobile)

import re
import pandas as pd
import re
 
def isValid(mobile):
    Pattern = re.compile('(0|91)?[6-9][0-9]{9}')
    return Pattern.match(mobile)

df=pd.read_excel('student.xlsx')

lst = df.Mobile.values.tolist()

list_string = map(str, lst)

la=list(list_string)

print(la)

for mobile in la:
    if (isValid(mobile)): 
        nh=int(mobile)
        print (df.loc[df['Mobile']==nh])            
    else :
        print (f"'{mobile}' is an invalid number")

