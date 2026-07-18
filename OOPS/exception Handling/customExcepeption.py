class MultiplyError(Exception):
    def __str__(self):
        return 'Cannot multiply with zero'
    
def muliply(n1,n2):
    if n1==0 or n2==0:
        raise MultiplyError()
    else:
        return n1*n2    
    
    
try:
    num1=int(input("Enter num1 " ))    
    num2=int(input("Enter num2 " ))    
    num3=muliply(num1,num2)
    print(num1,num2,num3,sep='\n') 
except ValueError:  #predefined 
    print("Input must be integer")
except MultiplyError as a: # user-defined
    print(a)           