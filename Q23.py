# Write a program to find input number is palindrome or not

num=int(input("Enter any number "))
num1=num
Pdrome=0

while num1>0 :
    r=num1 % 10 
    Pdrome=Pdrome*10 + r
    num1=num1//10
    
if Pdrome== num :
    print("Palindrome")
else :
    print("Not Palindrome")    