try:
    print("Inside try block")
    n1=int(input("Enter first number :"))
    n2=int(input("Enter second number :"))
    n3=n1/n2
    print(n1,n2,n3)
except ZeroDivisionError:
    print("Inside except block")
finally:
    print("inside finally block")
    
print("Continue...........")            