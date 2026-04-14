
# demo=input()
# tuple=(demo.split())
# print(tuple)



# Write a program to add two numbers
# input format
#10 20


# n=(input("Enter two num : "))
# n1,n2=n.split()
# print(type(n1))
# sum=int(n1)+int(n2)
# print("Sum = ",sum)


     #Using map function for the split
# n1,n2=map(int,input("Enter two num : ").split())
# print("Sum = ",n1+n2)


list=['12','34',45,62]
a,s,d,f=list
print(a,s,d,f,type(a),type(s),type(d),type(f))




list=[12,45,62]
a,s,d=list
print(a,s,d,type(a),type(s),type(d))

x,y,z=map(int,list)
print(x,y,z,type(x),type(y),type(z))

q,w,e=map(float,list)
print(q,w,e,type(q),type(w),type(e))

list2=["java","python","oracle"]
a,b,c=map(str.upper,list2)
print(a,b,c)



