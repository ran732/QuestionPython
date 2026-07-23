def SelectionSort(num):
    n= len(num)
    
    for i in range(n):
        nm = num[i]
        ind = i
        
        for j in range(i+1,n):
            if num[j]<nm:
                nm=num[j]
                ind = j
                
        temp=num[i]
        num[i]=num[ind]
        num[ind]=temp
        
    return num



print(SelectionSort([8,2,7,5,3,6,9,7]))            
print(SelectionSort([92,67,45,43,6,9,7]))            