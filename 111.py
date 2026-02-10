#Function with variable length arguments or parameters


def fun1(*a):
    print(type(a))
    print(a)
    
fun1()    #tuple
fun1(10)    
fun1(100,200,300,400,500)    
fun1(101,203,"ramesh","python")    


def add(*values):
    s=0
    for value in values:
        s=s+value
    return s

res1=add(100,200)   
print("Sum ",res1) 



