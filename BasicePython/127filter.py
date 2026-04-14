list1 = [1,3,6,7,878,3,45,45,56,6,7,78,9,5,45,434,54,56,667,677,87878,8,34,33,45,9,9,8,8,23.34,45,5667,7887,981,2,23,3443,4,54,5]
a=filter(lambda value:value%2==0,list1)   #filter function returns iterator.  it accepts ( function,iterator)
for value in a:
    print(value,end=" ")
print()

b=filter(lambda value:value%2!=0,list1)  
for value in b:
    print(value,end=" ")    