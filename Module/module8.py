def fun1():
    print("Inside fun1")
    
def fun2():
    print("Inside fun2")
    
def fun3():
    print("Inside fun3")   
    
def fun4():
    print("Inside fun4")


# How to use executable module as a reusable module
if __name__=='__main__':
    fun1()
    fun2()
    fun3()
    fun4()