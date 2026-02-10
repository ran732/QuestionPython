def fun1(a,b=10,*c):
    print(a,b,c)
    
def fun2(a,*c,b=10): #
    print(a,b,c)

def fun3(*a,b):
    print(a,b)
    
    

fun1(100)
fun1(100,200)
fun1(100,200,300,400,500,600)

fun2(10)
fun2(10,20,30,40,50,60,70)
fun2(10,20,30,40,50,b=90)

fun3(10,20,30,40,50,b=90)
