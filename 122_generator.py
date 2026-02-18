#Generator


#yield function

def fun1():  #generator function
    yield 4  #just pause not terminate like return keyward
    yield 9
    yield 34
    yield 89
    yield 324
    
a=fun1()
v1=next(a)    
v2=next(a)    
print(v1)
print(v2)

for v in a:
    print(v,end=" ")
print()    

    
b=fun1()
list1=list(b)
print(list1)    

print("*"*50)
###########################################

def reviter(s):
    s=s[::-1]
    for x in s:
        yield x
        
list1=[10,20,30,40,50]
a=iter(list1) #predefine iterator object
for i in a:
    print(i,end=' ')  
print()         
    
b=reviter(list1)  #userdefine iterator object
for y in b:
    print(y,end=' ') 
print()      

print("*"*50)
#################################################

def primeGenerator(start,stop):
    for num in range(start,stop+1):
        c=0
        for i in range(1,num+1):
            
            if num%i ==0:
                c+=1
        if c==2:        
            yield num  
                
a=primeGenerator(1,100)   #userdefined iterator object
value1=next(a)
print(value1)
value2=next(a)
print(value2)
for v in a:
    print(v, end=" ")    
     
    
print()    
print("*"*50)   
########################################################         
                
even=(value for value in range(1,51)if value%2==0)#creating a generator iterator object using expression
for value in even:
    print(value,end=" ")                
print() 

odd=(value for value in range(1,51)if value%2!=0) 
for value in odd:
    print(value,end=" ")
print() 

list1=[10,20,30,40,50]
reviter=(value for value in list1[::-1])
for value in reviter:
    print(value,end=" ")  
print()    

list1=[1,3,6,8,9,24,56,89,34,12,11,13,16,78,49,85,76,97,37,65,45,54,34,32]
print(list1)
even=(value for value in list1 if value%2==0)
for value in even:
    print(value,end=" ")
print() 

odd=(value for value in list1 if value%2!=0)
for value in odd:
    print(value,end=" ")
print()    
  
  
print()    
print("*"*50)                