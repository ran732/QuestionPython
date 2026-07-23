def partition(num,l,r):
    key = num[r]
    start = l  #pointer
    
    for i in range(l,r+1):
        if num[i]<=key:
            temp = num[i]
            num[i] = num[start]
            num[start] = temp
            start += 1
    
    return start -1        

def QuickSort(num,l,r):
    
    
    #base case
    if l>=r:
        return
    
    p = partition(num,l,r)
    
    QuickSort(num,l,p-1)
    QuickSort(num,p+1,r)
    
def sortArray(num):
    n = len(num)
    QuickSort(num,0,n-1)    
    
    return num

print(sortArray([2,4,6,7,85,5,67,4,33,24,45,4,56,56]))