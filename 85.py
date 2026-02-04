#wQ3.ap to add the values in given dictionary

d1={1:2,2:90,3:50}

dict1={}
dict1.setdefault(1,2)
dict1.setdefault(2,90)
dict1.setdefault(3,50)

dict1=dict1.values()

sssum=0
for i in dict1:
    sssum +=i

print(sssum)

dict1=sum(dict1)   #builtin sum
print(dict1)