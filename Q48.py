list=[19, 24, 31, 43, 25, 96, 71, 83]
a=len(list)

sum=0
max=list[0]
length=0
for i in range (len(list)):
    length=length+1
    sum=sum+list[i]
    if list[i]>max:
        max=list[i]
        
    if a%2==0:
        med=(list[(a-1)//2]+list[(a//2)] ) /2
    else:
        med=(list[((a)/2)])
              
print("Sum = ",sum)    
print("Maximum = ",max)  
print("Medium = ",med)  
print("Length of list = ",a)
print("Length of list = ",length)