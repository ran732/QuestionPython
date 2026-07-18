n1=int(input("Enter First Number "))
n2=int(input("Enter Second Number "))

try:
    n3=n1/n2
    print(n1,n2,n3)
    
except ZeroDivisionError:
    print("Cannot devide by zero")    