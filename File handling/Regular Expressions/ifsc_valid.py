import re

ifsc_code=input("Enter IFSC code :")
m=re.fullmatch(r'[a-zA-Z]{4}[0-9]{7}',ifsc_code)
if m:
    print("Valid ifcs code")
else:
    print("Invalid ifsc code")    