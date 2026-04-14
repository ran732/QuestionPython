def fun1(a):
    a[0]=99
    a.append(100)
    
    
    
    
def fun2():
    list1=[10,20,30]
    print(f'Before calling function {list1}')
    fun1(list1)
    print(f'After calling function {list1}')

fun2()    




def simple_interest(amt,t,r=1.5):
    si=(amt*t*r)/100
    return si

res1=simple_interest(5000,12)
print(f'Simple interest is {res1:.2f}')
res2=simple_interest(9000,24,2.5)
print(f'Simple interest is {res2:.2f}')



