# Sum of First N Numbers
def sum(num):
    if num==0:
        return 0
    else:
        return num + sum(num-1)
   
Summation=sum(10) 
print(Summation)  
    