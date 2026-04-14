# Write a program to generate first 10 prime numbers


    
s=0
num=1
while True:
    count=0
    for i in range (1,num+1):
        if num%i==0:
            count=count+1
        if count>2:
            break    
    if count==2:
        print(num)
        s=s+1
    if s==10:
        break   
        
        
    num=num+1      
        
    
    
        