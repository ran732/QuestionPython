
# Q2. take input till n from the user and print dict(n,n*5)

l1=[]
l2=[]
n=int(input("Enter n :"))
for i in range(1,n+1):
    l1.append(i)
    l2.append(i*5)
z=dict(zip(l1,l2))
print(z)    

# OR
dict1={}
n=int(input("Enter n :"))
for i in range(1,n+1):
    dict1[i]=i*5
print(dict1)    