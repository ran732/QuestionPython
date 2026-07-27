import re 

list1=re.findall(r'.','python')
print(list1)



list2=re.findall(r'.','python\nlanguage')
print(list2)



list3=re.findall(r'.','python\nlanguage',re.DOTALL)
print(list3)


list4=re.findall(r'p..','python pypy jython rpython programming')
print(list4)


list5=re.findall(r'p.t','python programming pot')
print(list5)


list6=re.findall(r'...','python programming language')
print(list6)

