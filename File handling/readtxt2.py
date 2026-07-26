# Write a program to count vowels in createtxt.txt
import sys
try:
    f=open("createtxt.txt",'r')
    c=0
    while True:
       s=f.read(1)
       
       if s=="":
           break
       if s in "aeiouAEIOU":
           c+=1
    print(f'Count of vowels are {c}')
except:
    t=sys.exc_info()
    print(t[0])   
finally:   
    f.close()           