#get(key[, default])

d1={1:10,2:20,3:30,4:40,5:50}
print(d1[1])
print(d1[4])
# print(d1[6])    #Error

print(d1.get(1))
print(d1.get(2))
print(d1.get(4))
print(d1.get(5))
print(d1.get(6))     #None
print(d1.get(6,899))     #Default



#setdefault(key[, default])
d1={1:10,2:20,3:30}
print(d1)
print(d1.get(1))
print(d1.get(3))
print(d1.get(4))

print(d1.setdefault(4))
print(d1)

print(d1.setdefault(5,55))
print(d1)