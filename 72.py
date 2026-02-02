A={10,40,50,20,30}
B={40,20,50,60}
C=A.union(B)
D=A.intersection(B)
E=A.difference(B)
F=A.symmetric_difference(B)
print(A,B,C,D,E,F,sep="\n")

X={1,2,3}
Y={1,2,3,4}
Z={1,2,3,5,6,7}
P=X|Y|Z
Q=X&Y&Z
print(X,Y,Z,P,Q,sep="\n")

s1=set("ABC")
s2=set("ABCD")
s3=s1|s2
s4=s1&s2
s5=s1-s2
s6=s1^s2
print(s1,s2,s3,s4,s5,s6,sep="\n")

# Sets Operation

A=set()
A.add(10)
A.add(20)
A.add(30)
A.add(40)
A.add(50)
print(A)

A.remove(10)
A.remove(20)
A.remove(30)
print(A)

A.discard(30)  #Remove element elem from the set if it is present.
A.discard(40)
print(A)

B=set(range(10,60,10)) 
value=B.pop()   #Remove and return an arbitrary element from the set. Raises KeyError if the set is empty.
print(value)
print(B)

B.clear()
print(B)

A={10,11,12}
A.update({40,50})
print(A)

s1={1,2,3,4,5}
s2={3,4,5,6,7,8,9}
s1 |= s2
# s1.update(s2)
print(s1)


s1={1,2,3,4,5}
s2={3,4,5,6,7,8,9}
s1 &= s2
# s1.intersection_update(s2)
print(s1)

s1={1,2,3,4,5}
s2={1,2,3,6,7}
s1 -= s2
# s1.difference_update(s2)
print(s1)

s1={1,2,3,4,5}
s2={1,2,3,6,7}
s1 ^= s2
# s1.symmetric_difference_update(s2)
print(s1)

