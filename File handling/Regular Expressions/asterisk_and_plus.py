# finding all the names whose name starts with r and end with n
import re

names=['ramesh','kishore','rajesh','rakesh','nk','harsha','raman','ranmp']
for name in names:
    m=re.findall(r'^r.+n$',name)
    #m=re.findall(r'^r.*n$',name)
    if m:
        print(name)



str1="ab a abb abbb"
m=re.findall(r'ab+',str1)
print(m)
#['ab', 'abb', 'abbb']

list1=re.findall(r'ab*',str1)
print(list1)
#['ab', 'a', 'abb', 'abbb']
