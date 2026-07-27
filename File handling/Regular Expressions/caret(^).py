import re

m=re.search(r'^py','python')
print(m)


#find name begins with r

names=['ramesh','rajesh','rakesh','nk','kishore']
for name in names:
    m=re.search(r'^r',name)
    if m:
      print(name)
      
      
 
str1='''python is easy
python is high level
python is object oriented
jython is python implementation'''
list1=re.findall(r'^py',str1,re.MULTILINE)
print(list1)
      