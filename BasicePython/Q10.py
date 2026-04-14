# Write a program to check input number is 3 digit or not

num = int(input("Enter a number "))
if 1<=num/100 <10 :
    print(num,"is a 3-digits number")
else:    
    print(num,"is not a 3-digits number")