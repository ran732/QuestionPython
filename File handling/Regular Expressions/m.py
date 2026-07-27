import re

str1="ab a abb abbb"
list1=re.findall(r'ab{2}',str1)
list2=re.findall(r'ab{3}',str1)
list3=re.findall(r'ab{5}',str1)
print(list1)
print(list2)
print(list3)

print()
print()

list1=re.findall(r'ab{1,}',str1)
list2=re.findall(r'ab{2,3}',str1)
list3=re.findall(r'ab{4,5}',str1)
print(list1)
print(list2)
print(list3)

