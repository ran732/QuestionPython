import re


names=['naresh','ramesh','kishore','rajesh','kiran','raman','suresh']

for name in names:
    m=re.fullmatch(r'^[rk].*',name) #start with r or k
    if m:
        print(name)
        
        
print("=================================")
for name in names:
    m=re.fullmatch(r'^[rk].*[hn]$',name)
    if m:
        print(name)        