# Write program to login with OTP

import random
user = input ("Username : ")
if user == "Ranjeet123":
    
    otpNum=random.randint(1000,9999)
    otp=print("otp number is ",otpNum)

    input("OTP = ")
   
    
    if otp == otpNum :
        print("Login Successfully!")
    else:
        print("Enter Wrong OTP")    

else:
    print("Please !! Correct your  username")    