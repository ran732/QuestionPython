import re


name = input("Enter name : ")
m=re.fullmatch(r'[A-Z][a-z]{3,20}',name)
if m:
    print(f'{name} valid')
else:
    print(f'{name} is invalid')    