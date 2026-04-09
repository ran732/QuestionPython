import module2

module2.msg()  #executable statement

def isEven(num):
    return num%2==0

def isPrime(num):
    c=0
    for i in range(1, num+1):
        if num%i==0:
            c=c+1
    return c==2
    
def isFactorial(num):
    if num==0:
        return 1
    else:
        return num*isFactorial(num-1)        