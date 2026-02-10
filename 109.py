#sorting of a list using function

def sortData(a,reversed=False):
    if reversed:
        for i in range(len(a)):
            for j in range(len(a)-1):
                if a[j]<a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]
    else:
        for i in range(len(a)):
            for i in range(len(a)-1):
                if a[i]>a[i+1]:
                    a[i+1],a[i]=a[i],a[i+1]
                    
list1=[2,34,5,6,78,8,82]      
print("Before Sorting ",list1)
sortData(list1) 
print("Ascending Order ",list1)
sortData(list1,reversed=True)             
print("Descending Order ",list1)             
                
                        