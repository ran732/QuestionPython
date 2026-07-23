def InsertionSort(num):
    n=len(num)
    
    for i in range(n):
        key = num[i]
        j=i-1
        
        while j>=0 and num[j]>key:
            num[j+1]=num[j]
            j -= 1
            
        num[j+1]=key
            
    return num

p=InsertionSort([13,4,34,45,2,1])     
print(p)   
            
print(InsertionSort([5, 2, 4, 6, 1, 3]))            
            
    