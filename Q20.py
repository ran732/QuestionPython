# Write a program to count how many even and odd digits & Their Sum exists within input number

num = int(input("Enter a number : "))
EvenDigit =0
countEven=0

OddDigit =0
countOdd=0

if num == 0 :
    print("Neither Even nor Odd")
    
else :
    
    while num>0 :
        
       Digit=num%10 
    
       if Digit%2==  0:
           EvenDigit=EvenDigit+Digit
           countEven +=1
           num=num//10
        
           
       else:
           OddDigit =OddDigit +Digit
           countOdd +=1
           num=num//10
           
    print("Number of Odd Digits are ",countOdd)
    print("Sum of Odd Digits are ",OddDigit)
    
    print("Number of Even Digits are ",countEven)
    print("Sum of Even Digits are ",EvenDigit)
        