# 6.Define A Procedure Histogram() That Takes A List Of Integers And Prints A Histogarm To The Screen.
# For Example, Histogram([4,9,7]) Should Print The Following :
# ****
# *********
# *******

def Histogram(n):
    lst=[]
    for i in range(0,n):
        m = int(input("Enter Numbers For Histogram : "))
        lst.append(m)

    print("Histogram",lst)

    for j in lst:
        print("* "*j)

a = int(input("Enter How Many Lines Of Histogram You Want : "))
Histogram(a)
        
