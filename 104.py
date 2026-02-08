# #global keyword

# a=100 #Global variable
# def fun1():
#    print(a)
# def fun2():
#     global a
#     a=500
#     print(a)   
    
# fun1()    
# fun2()    
# fun1()    


# base=0.0 # Global Variable
# height=0.0 # Global Variable
# def read():
#     global base ,height
#     base=float(input("Enter Base of Triangle "))
#     height=float(input("Enter Height of Triangle "))
# def findArea():
#     a=0.5*base*height
#     print(f'Area of triangle is {a:.2f}')
# read()
# findArea()    

    
#globals()    global function
x=100
def fun1():
    x=200
    y=300
    print(x)
    print(y)
    a=globals()
    print(a['x'])
    a['x']=900
    
fun1()
print(x)    