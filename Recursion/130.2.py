# Find length of the digits
res=-1
def CountDigit(num):
    global res
    if num!=0:
        CountDigit(num//10)
    res=res+1
    
n= int(input("Enter a number : "))    
CountDigit(n) 
print("Digits in the number are ",res)    


# function Overloading

def fun1():  
    print("fun1 without parameter")
    
def fun1(a):
    print("fun1 with parameter")    
    
#  fun1(a) has repalced fun1()
print(100) 