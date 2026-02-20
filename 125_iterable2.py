#using magic method to call directly

L=[10,20,30,40,50]  #iterable

iter_object = L.__iter__()  #iterator
print(type(iter_object))

print(iter_object.__next__()) #10

print(next(iter_object)) #20  

print(iter_object.__next__()) #30 

print()
##################################################################


L1=[10,20,30,40,50]
 
iter_object=iter(L1)
print(id(iter_object)) 

iter_object1= iter(iter_object) 
print(id(iter_object1))
print(type(iter_object1))

print(next(iter_object1))
print(next(iter_object1))
print(next(iter_object1))


print()
##################################################################


#for cheaking program is iterator or iterable
object= eval(input("Enter Object : "))
object_dir=dir(object)
if '__iter__' in object_dir and '__next__' in object_dir :
    print(" Iterator operation goes here")
elif  '__iter__' in object_dir:
    print(" Iterable operation goes here")
else:
    print("not supported")
        
