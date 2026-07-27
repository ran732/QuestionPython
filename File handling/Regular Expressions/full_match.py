import re 

m=re.fullmatch(r'python','python')
print(m)
# <re.Match object; span=(0, 6), match='python'>


m=re.fullmatch(r'python','python jython')  #must be full match of all string
print(m) #None
