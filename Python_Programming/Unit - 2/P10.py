# 10.Write a program to zip and unzip particular files.

import zipfile
import shutil
import os

def DeleteFile(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print("File Deleted Successfully.")
    else:
        print("File Does Not Exist.")

def zip(file_name,zip_file):
    with zipfile.ZipFile(zip_file,'w') as zip_file:
        zip_file.write(file_name)
    zip_file.close()

def unzip(zip_file):
    with zipfile.ZipFile(zip_file,'r') as zip_file:
        zip_file.extractall()
    zip_file.close()

def zip_shutil(file_name):
    f_name = file_name.replace('.txt','')
    shutil.make_archive(f_name,'zip','C:/Users/HP NoteBook/Desktop/GitHub/college_programs/Python_Programming/Unit - 2')
    print("File Zipped Successfully.")

def unzip_shutil(file_name):
    shutil.unpack_archive(file_name)
    print("File Unzipped Successfully.")

file_name = input("Enter Text File Name You Want To Perform Operations :")
zip_file = input("Enter Zip File Name You Want To Perform Operations :")

while True:
    print("---------------------------------------------------------")
    print("Press 1 For Zip File Using zipfile Module")
    print("Press 2 For Unzip File Using zipfile Module")
    print("Press 3 For Delete Particuler Text File")
    print("Press 4 For Delete Particuler Zip File")
    print("Press 5 For Zip File Using shutil Module")
    print("Press 6 For Unzip File Using shutil Module")
    print("Press 7 For Exit")
    choice=input("Enter Your Choice :")
    print("---------------------------------------------------------")

    if choice == "1":
        zip(file_name,zip_file)
    elif choice == "2":
        unzip(zip_file)
    elif choice == "3":
        DeleteFile(file_name)
    elif choice == "4":
        DeleteFile(zip_file)
    elif choice == "5":
        zip_shutil(file_name)
    elif choice == "6":
        unzip_shutil(zip_file)
    elif choice == "7":
        break
    else:   
        print("Entered Choice Is Invalid.")
