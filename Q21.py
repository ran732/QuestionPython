# Write a program to find input number is armstrong or not (3digit number)


# # 3 Digit Number or not


num=int(input("Enter any number "))

# armsstrong=num/100
# if  1<=armsstrong<10 :
#     print("Input number is 3 Digit Number ")
# else :
#     print("Input number is not 3 Digit Number")    




# ✅ Definition (Simple)     armstrong or not

# A number is called an Armstrong number if the sum of each digit raised to the power of total digits is equal to the number itself.
Armstrong =0
if num>0 :
    r=num%10
    Armstrong= Armstrong+r**3
    num=num//10
    print("Input number is armstrong")
    
else:
    print("Input number is not armstrong")
    
        
    
    