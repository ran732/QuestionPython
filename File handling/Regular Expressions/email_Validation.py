# email-id validation
# naresh@nareshit.com
# a123@nareshit.com


import re

email=input("Enter your email : ")

m=re.fullmatch(r'[a-zA-Z]{1}[a-zA-Z0-9]*@[a-z]+\.[a-z]{2,3}',email)
if m:
    print("Valid email")
else:
    print("Invalid email")

