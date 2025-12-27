# Write a program to find input number is armstrong or not (3digit number)

num=int(input("Enter any number "))

armsstrong=num/100
if  1<=armsstrong<10 :
    print("Input number is armstrong")
else :
    print("Input number is not armstrong")    