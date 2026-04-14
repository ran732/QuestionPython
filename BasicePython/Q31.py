# Write a program to find input number is prime or not

num = int (input("Enter a number "))

c=0
for i in range (1,num+1):
    if num%i==0 :
        c=c+1
if c==2 :
    print("Prime Number")   
else :
    print("Not a prime number")         