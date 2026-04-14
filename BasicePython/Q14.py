# Write program to login with OTP

import random
user = input ("Username : ")
if user == "Ranjeet123":
    
    otpNum=random.randint(1000,9999)
    otp1=print("otp number is ",otpNum)

    otp2=int(input("OTP = "))
   
    
    if otp2 == otpNum :
        print("Login Successfully!")
    else:
        print("Enter Wrong OTP")    

else:
    print("Please !! Correct your  username")    