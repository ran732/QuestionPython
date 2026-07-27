import re

list1=re.findall(r'python','java python oracle python .net python')
print(list1)  #left to right in list  of all matches
#['python', 'python', 'python']


list1=re.findall(r'java','java python oracle python .net python')
print(list1)


list1=re.findall(r'jython','java python oracle python .net python')
print(list1)
