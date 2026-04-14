# Closure Function
def calulatar ():   #outer function
    n1=int(input("Enter : "))
    n2=int(input("Enter : "))
    
    def sum():    #inner funct
       n3=n1+n2
       return n3
   
    def diff():   #inner function
       n3=n1-n2
       return n3
   
    op=input("Enter operator : ")
    
    if op =='+':
        print(f'Sum of {n1}+{n2}={sum()}')  #calling inner function  
        
    if op =='-':
        print(f'Difference of {n1}-{n2}={diff()}')  #calling inner function    
        
        
calulatar() #calling outer function        

#############################################################


def power (num,p):
    r=num**p
    return r
res1=power(5,2)
print(res1)


########################################################


#using nested function

def power(num):  #outer function
    def findpow(p):  #inner function
        return num**p
    return findpow  #outer function returning inner function

pwr=power(2)  #calling outer function
res=pwr(5)    #calling inner function
print(res)


#########################################################


def draw(ch):  #outer function
    def drawLine(n):#inner function
        print(ch*n) 
    return drawLine   

drawStars=draw("*")
drawDollar=draw("@") 
drawStars(10)
drawStars(20)
drawDollar(24)
drawDollar(13)

###############################################################

def calculator (n1,n2):
    def operation(op):
        if op == '+':
            return n1+n2
        elif op =='-':
            return n1-n2
        elif op =='*':
            return n1*n2
        elif op=='/' and n2!=0:
            return n1/n2
    return operation
    
c1=calculator(4,7)
r1=c1('+')    
r2=c1('-')    
r3=c1('*')    
r4=c1('/')   
print(r1,r2,r3,r4) 

######################################################

def greet(msg):
    def display(name):
        print(name+" "+msg)
    return display
    
greet1=greet("Hello")
greet1("Ranjeet")    
greet1("Aj")    
greet2=greet("Hii")
greet2("Ran")
greet2("kaubf")

