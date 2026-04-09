# Fibonacci Number
# Find nth Fibonacci number.
#  0 1 1 2 3 5 8 ...

def Fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
    
    
print(Fib(3))    
    
def fib_series(n):
   for i in range(n):
        print(Fib(i),end="  " )   
    
fib_series(10)    