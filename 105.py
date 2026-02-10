def power(num,p):
    res=num**p
    print(res)

power(5,3)
power(4,3)

def add (a,b):
   c=a+b
   print(c)

add(34,756)
add(23+56j,27+44j)
add('python ',"language")

def fun1(a:int,b:int):
    print(a,b)
fun1(34,56)
# fun1('ew','ere')

def fun1(a,b,c,d):
    print(a,b,c,d)
fun1(12,34,45,56)

def maximum(a,b):
    if a>b:
        print("Max is ",a)
    else:
        print("Max is ",b)
maximum(34,56)

# return keyword
def simple_interest(amt,t,r):
    si=(amt*t*r)/100
    return si
print(simple_interest(1000,2,10))
# u=simple_interest(1000,2,10)
# print(u)

def fun1():
    return 10,20,30,40,50
print(fun1()) #tuple

#factorial of a functions
def factorial(num:int)->int: #->int return only integer
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact     #we only return the value name not function name

user=int(input("Enter a number : "))
print(factorial(user))
# print(factorial(5))