# Functions
def drewLine():   #function definition
    for i in range(40):
      print("*",end="")
    print()


drewLine()    #function calling 
print("Python")  
drewLine()     
print("Programming language")
drewLine() 

print("Welcome")
def sayHello():
    print("Hello, This os my first function.")
    
sayHello()    
print("HEllo")
a=100
b=200
c=a+b
print(c)

def fun1():
    print("inside fun1")
    
def fun2():
    print("inside fun2")
    
def fun3():
    print("inside fun3")
    
fun1()    
fun2()    
fun3()    
    
def fun1():
    print("function without parameters")
fun1()
   
def add():
    n1=int(input("enter "))  #local variable
    n2=int(input("enter "))
    n3=n1+n2
    print(f'Sum of {n1} and {n2} is {n3}')
    
add()    

    
def fun1():
    x=100 # Local variable
    print(f'{x} of fun1')

def fun2():
    x=200 # Local variable
    print(f'{x} of fun2')

fun1()
fun2()
fun1()

num1=100 # Global variable
num2=200 # Global variable
def add():
    print(f'sum of {num1} and {num2} is {num1+num2}')
def sub():
    print(f'diff of {num1} and {num2} is {num1-num2}')


add()
sub()
    
    
x=100 # Global variable
def fun1():
    y=200 # Local variable
    print(f'Global variable x={x}')
    print(f'Local variable y={y}')

def fun2():
    z=300 # Local Variable
    x=500 # Local Variable
    print(f'Local variable z={z}')
    print(f'Local variable x={x}')

fun1()
fun2()
    
x=100 # Global variable

def fun1():
    print(x)

def fun2():
    x=500
    print(x)

fun1()
fun2()
fun1()
    
        