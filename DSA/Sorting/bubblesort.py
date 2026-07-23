num = [12,32,14,16,64,32]
num.sort()
print(num)



def BubbleSort(list1):
    n=len(list1)
    for i in range(n):
        is_swap=False
        for j in range(n-i-1):
            if list1[j]>list1[j+1]:
                temp = list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
                is_swap=True
                
        if not is_swap:
            break    
  
    return list1             

b=BubbleSort([2,5,3,9,6,4,8])
print(b)