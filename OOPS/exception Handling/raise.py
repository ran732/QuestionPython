def muliply(n1,n2):
    if n1==0 or n2==0:
        raise ValueError()
    else:
        return n1*n2
    
    
num1=int(input("Enter First Number "))
num2=int(input("Enter Second Number "))
try: 
    num3=muliply(num1,num2)   
    print(num1,num2,num3,sep="\n")
except ValueError:
    print("Number cannot multiply woth zero")    