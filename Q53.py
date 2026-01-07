# Sorting list values using Bubble Sort

n=int(input("How much num has to be inserted in the list :"))
list = []

for i in range(1,n+1):
    input_user=int(input("Bhar le kuchh v : "))
    list.append(input_user)
    
list1=list    
print(" Before Sorting = ",list1)  

for i in range(n):
    for j in range(0,n-1): # 0 1 2 3 
        if list1[j]>list1[j+1]:
            temp=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=temp
            
print("After sorting = ",list1)            
