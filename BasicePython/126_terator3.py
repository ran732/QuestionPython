# Making oour own loop

L=[10,20,30,40]  #iterable

def mera_for_loop(iterable):
    iterator = iter(iterable)
    try :
       while True:
         print(next(iterator))
    except StopIteration:
        print("End here")     

mera_for_loop(L)    

print()
########################################################################


#what is the biggest advantage of iterator
#it saves memory.



import sys #cheak memory consumption

L = [1,2,3,4,5,6,7,8,9,10]
for i in L:
    print(i**2, end=" ")
print()     
print("L : ",sys.getsizeof(L))
    
    
print() 
print() 
print() 


a=range(1,3)    
for i in a   :
    print(i**2 , end=" ")
print()    
print("L : ",sys.getsizeof(a))    #48 always