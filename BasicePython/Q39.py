# write a program to print prime numbers from 2 to 20


for num in range (2,21):
    c=0
    for i in range (2,num+1):
        if num%i==0 :
            c=c+1
    if c==1:
        print(num," Isprime ")  
            
                 
            
                               
            
            