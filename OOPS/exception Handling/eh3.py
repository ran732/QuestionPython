# Write a program to divide two numbers


try:
    n1=int(input("Enter first number "))
    n2=int(input("Enter second number "))
    n3=n1/n2
    print(f'{n1}/{n2}={n3:.2f}')
    
except ValueError:
    print("Input value must be integerType ")

except ZeroDivisionError:
    print("Cannot devided by zero")    