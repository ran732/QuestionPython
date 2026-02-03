# Using iterator
# iter()

dict1={1:10,2:20,3:30,4:40,5:50}
a=iter(dict1)
k1=next(a)
print(k1)
k2=next(a)
print(k2)
k3=next(a)
print(k3)

v1=dict1[k1]
v2=dict1[k2]
v3=dict1[k3]
print(v1,v2,v3)
for k in a:
    print(k,dict1[k])
    
    
    