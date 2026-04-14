#ITERATION - process of takeing each item of something one after another.Ex-loop for visiting
#ITERATOR - that allow to programmers to travers through a sequence of data without storing the data in the memory
#ITERABLE -On which iteration occurs. it may be the container

L=[10,20,30,40,50]  #itarable
print(dir(L))
# dir() is a built-in Python function.

# 👉 It shows all properties and methods available for an object.

print()

iter_object=iter(L)      #iterator                     #remembar previous value
print(dir(iter_object))


print(next(iter_object)) #10
print(next(iter_object)) #20

for i in iter_object:
    print(i,end=" ")



