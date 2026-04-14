def fun1(a,b,c):   #required Arguments
    print(a,b,c)
    
def fun2(**kwargs):
    print(kwargs['a'],kwargs['b'],kwargs['c'])    
    
fun1(a=10,b=20,c=30)    
fun1(a=10,b=20,c=30)    


def findResult(**kwargs):
    print(f'Rollno {kwargs["rollno"]}')
    print(f'Name {kwargs["name"]}')
    print(f'Subject1 {kwargs["s1"]}')
    print(f'Subject2 {kwargs["s2"]}')
    if kwargs['s1']<40 or kwargs['s2']<40:
        print("Result Fail ")
    else:
        print("Result Pass")
findResult(rollno=1,name="nk",s1=60,s2=70)
findResult(rollno=2,name="suresh",s1=30,s2=90)


def fun1(a,b=10,*c,**d):
    print(a,b,c,d,sep="\n")
fun1(100)
fun1(100,200)
fun1(100,200,300,400,500)
fun1(10,x=100,y=200)
fun1(a=100,b=200,x=300,y=400,z=500)
fun1(100,200,300,400,500,x=1,y=2,z=3)
