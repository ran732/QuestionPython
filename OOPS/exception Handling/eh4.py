# Write a program to divide two numbers
import sys

try:
    n1=int(input("Enter first number "))
    n2=int(input("Enter second number "))
    n3=n1/n2
    print(f'{n1}/{n2}={n3:.2f}')
    
except:
    t=sys.exc_info()
    print(t[1])
    

   