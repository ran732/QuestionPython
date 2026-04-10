import Package1.m1

def patch():
    print("This is the patch function.")
    
Package1.m1.fun1=patch    

Package1.m1.fun1()
Package1.m1.fun2()