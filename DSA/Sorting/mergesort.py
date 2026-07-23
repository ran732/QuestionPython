def Merge(num,l,mid,r):  #o(n)
    a=[]
    b=[]
    
    for i in range(l,mid+1):
        a.append(num[i])
    for i in range(mid+1,r+1):
        b.append(num[i])
        
    i,j,k = 0,0,l #pointers  
    
    while k<=r:
        if j==len(b):  #if j is at end
            num[k]=a[i]
            i+=1
            k+=1
        elif i==len(a): # if i as at end
            num[k]=b[j]
            j+=1
            k+=1
        elif a[i]<b[j]:
            num[k]=a[i] 
            i+=1
            k+=1    
        else:
            num[k]=b[j]
            j+=1
            k+=1   
        
                

def MergeSort(num,l,r):  #n(logn)
    
    #base case
    if l>=r:
        return
    
    #recursive case
    mid=(l+r)//2
    MergeSort(num,l,mid)
    MergeSort(num,mid+1,r)
    
    Merge(num,l,mid,r)
    
def sortArray(num):
    MergeSort(num,0,len(num)-1) 
    return num   
    
    
print(sortArray([111,3,6,9,7,5,20,2]))    
    
    
    