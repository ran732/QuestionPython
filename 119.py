# Decorator function
print("-" * 40)


def drawStar(fun1):  #outer function
    def draw():
        print("."*20)
        fun1()
        print("$"*20)
    return draw    

@drawStar    # ---> drawStar(display)
def display():
    print("PYTHON")

@drawStar
def studInfo():
    print("Rollno :101")
    print("Name : Rajesh")
    
display()
studInfo()

x=drawStar(display)
x()    

#####################################################
print("-"*50)

def greet():
    print("Hello Ranjeet")
    
x=greet
x()    

def outer():
    def inner():
        print("Inside inner function")
    inner()

y=outer
y()
###################################################
def decorator_func(original_func):
    def wrapper_func():
        print("Something before original function")
        original_func()
        print("Something after original function")
    return wrapper_func  

def display():
    print("Hello Bhai!!")
    
decorated_display=decorator_func(display)
decorated_display()      

####################################################
print("==========================================")
def drawLine(msg):
    def Inner():
       print("-"*18)
       msg()
       print("-"*18)
    return Inner

@drawLine
def msg():
    print("Learning Full Stack Python")  
msg()    
    
def msg():
    print("Learning Full Stack Python")      
# f=drawLine(msg)   
# f()    
    
###################################################    

def smartDiv(f):
    def newDiv(n1,n2):
        if n2==0:
            return 0
        else:
            return f(n1,n2)
    return newDiv
    
@smartDiv
def div(n1,n2):  #( div ---> newDiv)
    n3=n1/n2
    return n3

a=int(input("Enter first number :"))        
b=int(input("Enter second number :"))   
c=div(a,b)
print(f'{a}/{b}={c:.2f}')     