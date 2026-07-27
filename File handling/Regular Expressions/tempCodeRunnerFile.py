import re

str1="ab a abb abbb"
list1=re.findall(r'ab?',str1)
print(list1)
#['ab', 'a', 'ab', 'ab']
