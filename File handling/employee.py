# Write a program to create employee.txt file and store employee details

import sys

try:
    f=open("employee.txt","a")
    while True:
        empno=int(input("Enter enployee no : "))
        empname=input("Enter enployee name : ")
        sal=float(input("Enter salary : "))
        print(empno,empname,sal,sep=" ",file=f)  #file= f meaning writing stuff inside file and if not then it will be in only console
        ans=input("Add another employee? ")
        if ans =="no":
            break
        
        
except:
    t=sys.exc_info()             
    print(t[0])
finally:
    f.close()        