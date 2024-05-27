# 9.Write a program to read above file and use regular expression
# in order to display records who has valid emails.

import re
import pandas as pd

def emailcheck(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    if re.match(regex, email):
        return True
    else:
        return False
    
df=pd.read_excel('stud.xlsx')
lst = df.Email.values.tolist()
for email in lst:
    if emailcheck(email):
        print(df[df['Email']==email])
    else:
        print(f"'{email}' is an invalid email address.")
