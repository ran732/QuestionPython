# Variable=lambda [parameters]:expression/statement

a=lambda:print("Hello world!")
a()
sum=lambda a,b:a+b
sub=lambda a,b:a-b
multiply=lambda a,b:a*b
r1=sum(23,43)
r2=sum(12,45)
r3=sub(223,42)
r4=multiply(2,6)
print(r1,r2,r3,r4)

##########################################################

def calculator (a,b,fun):
    n3=a+b
    return n3


res1=calculator(10,20,lambda a,b:a+b)
print(res1)
res2=calculator(5,2,lambda a,b:a-b)
res3=calculator(5,8,lambda a,b:a*b)
res4=calculator(5,3,lambda a,b:a**b)
print(res2,res3,res4,sep="\n")
