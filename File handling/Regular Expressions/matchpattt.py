import re 

m=re.match(r'py','python')
print(m)
# <re.Match object; span=(0, 2), match='py'>


m=re.match(r'jy','python')
print(m)
#None

m=re.match(r'py','PYTHON',re.IGNORECASE)
print(m)
#<re.Match object; span=(0, 2), match='PY'>

