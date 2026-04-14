f1=frozenset()    #immutable type
print(f1)

f2=frozenset({10,11,12,13,14,15})
print(type(f2))
print(f2)

f3=frozenset(range(10,60,10))
print(f3)

f4=frozenset({"NIT"})
print(f4)

f4=frozenset("JAVA")
print(f4)


f5=frozenset([10,20,30,40,50])
print(f5)