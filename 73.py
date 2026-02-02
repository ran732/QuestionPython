# Set Examination methods
A={1,2,3}
B={4,5,6,7}
C=A.isdisjoint(B)   #intersection is the empty set.
print(C)

java_students={"ramesh","rajesh","kiran"}
python_students={"nk","kishore","raman"}
res=java_students.isdisjoint(python_students)
print(res)
if res==True:
    print("no student of java is doing python")
else:
    print("some students of java are doing python")

    

A={1,2,3}
B={1,2,3,4,5}
c=A<=B
# c=A.issubset(B)  
print(c)


A={1,2,3}
B={1,2,3,4,5}
c=B>=A
# c=B.superset(A)  
print(c)
