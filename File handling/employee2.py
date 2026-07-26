# Write a program to read employees data from employee.txt

import sys

try:
    f= open('employee.txt','r')
    tot=0
    while True:
        s=f.readline()
        if s=='':
            break
        list1=s.split()
        sal=float(list1[2])
        tot=tot+sal
        print(s,end='')
    print("Total Salaries paid to employees ",tot)   
except:
    t=sys.exc_info()
    print(t[0])   
finally:   
    f.close()        