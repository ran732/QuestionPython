#map(function, (iterable or *iterables))

#map(function,list)

#iterator= map(function(),iterable)

list1=[1,2,3,4,5]
a=map(lambda num:num**2,list1)
for value in a:
    print(value, end=" ")

