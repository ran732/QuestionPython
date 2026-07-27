import re

m= re.search(r'python','this is python language.')
print(m)
#<re.Match object; span=(8, 14), match='python'>


m=re.search(r'python','python is easy, python simple')
print(m)
#<re.Match object; span=(0, 6), match='python'>


m=re.search(r'python','java is language')
print(m)
#None
