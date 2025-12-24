# Write a program to find max of two numbers

n1 = eval(input("Enter num1 : "))
n2 = eval(input("Enter num2 : "))
n3 = eval(input("Enter num3 : "))

if (n1>=n2 & n1>=n3) :
    print(n1," is largest")
    
elif (n2>=n1 & n2>=n3)  :
    print(n2," is largest")
    
else :
    print(n3," is largest")    
      

