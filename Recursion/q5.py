# Count digits in a number using recursion.
res=-1
def CD(num):
    global res
    if num !=0:
        CD(num//10)
    res=res+1
    
CD(234234)    
print(res)    