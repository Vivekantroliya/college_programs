# 7.Write A Program To Perform Various Operation On List Using Menu.

lst = [1,2,3,4,5,6]

while True:
    print("---------------------------------------------------------")
    print("Press 1 For Append 90 Into The List.")
    print("Press 2 For Insert 100 At First In List.")
    print("Press 3 For Remove 100 From List.")
    print("Press 4 For Pop Last Element(90) From List.")
    print("Press 5 For Length Of List.")
    print("Press 6 For Largest Element Of List.")
    print("Press 7 For Smallest Element Of List.")
    print("Press 8 For Reverse The List.")
    print("Press 9 For Sort The List.")
    choice=input("Enter Your Choice :")
    print("---------------------------------------------------------")
    
    if choice=="1":
        lst.append(90)
        print("After Appending :",lst)

    elif choice=="2":
        lst.insert(0,100)
        print("After Inserting :",lst)

    elif choice=="3":
        lst.remove(100)
        print ("After Removing :",lst)

    elif choice=="4":
        lst.pop()
        print("After Popping Element :",lst)

    elif choice=="5":
        print("Length Of The List Is",len(lst))

    elif choice=="6":
        print("Largest Element Of The List Is",max(lst))

    elif choice=="7":
        print("Smallest Element Of The List Is",min(lst))
             
    elif choice=="8":
        lst.reverse()
        print("Reverse List :",lst)
        
    elif choice=="9":
        lst.sort()
        print("Sorted List :",lst)
            
    else:
        print("Sorry,You Entered Wrong Choice...")

    print("---------------------------------------------------------")
