# Write a program to find sum of digits of input number


user=int(input("Enter any number : "))
sum=0

if user==0:
    print("Sum of digit is 0")  
else:
    while user>0:
      DigitSum =user%10     # last digit                    
      sum=sum+DigitSum     # add digit
      user =user//10       # remove last digit
     
    
    print("Sum of digits is ",sum)    