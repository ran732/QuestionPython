# ✅ Definition

# A perfect number is a number whose sum of all proper divisors (excluding the number itself) is equal to the number.

# Write a program to find an input number is perfect number or not

num=int(input("enter any number "))

sum=0

for i in range (1,num,1) :
    if num%i==0 :
        sum=sum+i
    
if sum ==num :    
  print("Perfect Number")
else:
  print(" Not Perfect Number")    
        
