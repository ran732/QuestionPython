import re

str1="python java oracle python python java python"

str2=re.sub(r'java','jython',str1)
print(str2)


str3=re.sub(r'java','jython',str1,1)
print(str3)