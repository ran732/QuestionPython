# factorial of a number
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
    
f=factorial(5)    
print(f"Factorial of number is {f}")        