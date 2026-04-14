def add (*varg, **kwargs):
    s=0
    for value in varg:
        s=s+value
    for value in kwargs.values():
        s=s+value 
        
    return s      


res1=add(10,20,30,40,50)
res2=add(a=10,b=20,c=30,d=40)
print(res1)
print(res2)
res3=add(10,20,30,a=40,b=50)
print(res3)

def displayStudInfo(**kwargs):
    for name,course in kwargs.items():
        print(f'{name}-->{course}')
        
        
stud_dict={'nk':'python', 'suresh':'java','ramesh':'oracle','kishore':'c++'}        
displayStudInfo(**stud_dict)

def displayTuple(*vararg):
    for value in vararg:
        print(value)

t1=(10,20,30,40,50)   
displayTuple(*t1)     