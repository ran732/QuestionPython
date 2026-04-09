def printNum(num):    #store just like in stack (FILO)
    if num>1:
        printNum(num-1)
    print(num)
    
def printNumRev(num):    #store just like in stack (FILO)
    if num<10:
        printNumRev(num+1)
    print(num)
        
printNum(10) 
printNumRev(1)       
print()
print()
print()

# WAP for factorial

def fact(num):
    if num==0:
        return 1
    else:
      return(num*fact(num-1))  

n= int(input("Enter a number : "))    
f=fact(n) 
print("Factorial of the number is ",f)