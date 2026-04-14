# write a program to generate even numbers between m,n

m=int(input("enter value of m ")) 
n=int(input("enter value of n ")) 


if m%2==0 and n%2==0 :
    for i in range (m,n+1,2) :
        print(i)
elif m%2==0 and n%2!=0 :
    for i in range (m,n,2) :
        print(i)  
elif m%2!=0 and n%2==0 :
    for i in range (m+1,n+1,2) :
        print(i)              
else:
    for i in range (m+1,n,2) :
        print(i)
            
    