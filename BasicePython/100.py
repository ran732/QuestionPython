# Creating dictionary using dictionary comprehension
#Syntax1: {key:value for variable in iterable}

ascii_dict1={n:chr(n) for n in range(65,91)}
print(ascii_dict1)
print(ascii_dict1[65])

dict1=  {}
for i in range(65,91):
    dict1[i]=chr(i)
print(dict1)

table_dict={n:[n*i for i in range(1,11)] for n in range(1,6)}
print(table_dict)