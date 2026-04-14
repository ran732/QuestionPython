

import functools

list1 = [1,2,3,4,5,6,7,8,9,10]
res1=functools.reduce(lambda x ,y:x+y,list1)
print(res1) #55

res2=functools.reduce(lambda x ,y:x+y,list1,100)
print(res2)  #155

res3=functools.reduce(lambda x ,y:x if x>y else y,list1)
print(res3)