#How to remove data/items from dictionary

d1={1:10,2:20,3:30,4:40,5:50}
del d1[1]   #delete
del d1[3]   #delete  using key
print(d1)

d1[1]=10   #add
print(d1)


dict1={1:10,2:20,3:30,4:40,5:50}
dict1.pop(1)
dict1.pop(4)
dict1.pop(4,None)  #that good
print(dict1)


stack={101:'nk',
       102:'suresh',
       103:'ramesh',
       104:'kishore'}
stack.popitem()  #delete last (keys, values)
stack.popitem()  #delete last (keys, values)
print(stack)


d1=dict(zip(range(1,6),range(10,60,10)))
print(d1)
d1.clear()  #all remove
print(d1)


#fromkeys(iterable[, value])
sales=dict.fromkeys(range(2000,2011),None)
print(sales)
sales[2003]=10000   #replace
print(sales)

stud=dict.fromkeys((range(1,11)),None)
print(stud)
stud[1]="Ranjeet"
stud[2]="suresh"
print(stud)


#update([other])  overwriting if key exist  else Add

d1={1:10,2:20,3:30,4:40,5:50}
print('Before Updating : ',d1)
d2={6:60,7:70,8:80,2:90,4:80}
d1.update(d2)
print('After Updating',d1)


#  d | other        merge hot h

stud_dict1={'nk':'python',
            'suresh':'java',
            'ramesh':'oracle'}
stud_dict2={'kishore':'java',
            'ramesh':'c++'}
stud_dict=(stud_dict1)|(stud_dict2)
print(stud_dict1)
print(stud_dict2)
print(stud_dict)
