#map(function, (iterable or *iterables))

#map(function,list)

#iterator= map(function(),iterable)

list1=[1,2,3,4,5]
a=map(lambda num:num**2,list1)
for value in a:
    print(value, end=" ")
    
print()    
print()

list2=["10","20","30","40","50"] 
print(list2)
b=map(lambda value:int(value),list2)
list3=list(b)
print(list3)

print()    
print()

list4=[1,2,3,4,5,6,7] #
list5=[10,20,30,40,50] # lowest consider
c=map(lambda value1,value2:value1+value2,list4,list5)
list6=list(c)
print(list6)

print()    
print()

name=["nk","suresh","kishore"]
d=map(lambda s:s.upper(),name)
list7=list(d)
print(list7)
   

