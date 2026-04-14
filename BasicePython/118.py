def fun1():  #outer function 
    print("Outer functions")
    def fun2():
        print("Inner functions")
    fun2()  #inner function  
        
fun1()       

print("--------------------")
def fun1():  #outer function
    def fun2():  #inner function
        print("fun2") 
    def fun3():  #inner function
        print("fun3")
    def fun4():  #inner function
        print("fun4")
    print("inside fun1")
    fun2()
    fun4()
    fun3()
    
fun1()    
print("--------------------")

# Inner function can access data of outer function but outer function cannot access data of inner function.

# Inner function can access local variables of outer function directly but cannot update or modify values directly.

def fun1():
    a=100
    # print(b)   Error
    def fun2():
        b=100
        print(a)
    def fun3():
        a=500 # Local variable of fun3
        print(a)
    fun2()    
    fun3()
    print(a)   #cannot update outer value
fun1()        


#    nonlocal keyword
# without nonlocal keyword, inner function can access local variables of outer function but cannot modify or update.

# In order to modify or update nonlocal variable or enclosed block variable we have to use “nonlocal” keyword.

# nonlocal variable-name

print("--------------------")

def fun1():
    a=100
    def fun2():
        print(a)
    def fun3():
        nonlocal a  #modified value of a from the outer loop
        a=500
        print(a)
        
    fun2()        
    fun3()
    print(a)        
    
fun1()    

print("--------------------")


# LEGB Rule
# The LEGB rule is a kind of name lookup procedure, which determines the order in which Python looks up names. 

# L ---> Local
# E ---> Enclosed Block
# G ---> Global
# B ---> Built-ins module

x=100 # Global variable
def fun1():
    y=200 # Local variable of fun1
    def fun2():
        z=300 # Local variable of fun2
        print(z)
        print(y)
        print(x)
        print(__name__)
    fun2()


fun1()


print("--------------------")

def calculator(num1,num2,opr):
    res=None
    def add():
        nonlocal res
        res=num1+num2
    def sub():
        nonlocal res
        res=num1-num2
    def multiply():
        nonlocal res
        res=num1*num2
    def div():
        nonlocal res
        res=num1/num2
        
          
    if opr=='+':
        add()
    if opr=='-':
        sub()
    if opr=='*':
        multiply()
    if opr=='/':
        div()
    return res

n1=int(input("Enter first number : "))
op=input("Enter the operator : ")
n2=int(input("Enter second number : "))

n3=calculator(n1,n2,op)
print(f'Result is {n3}')

