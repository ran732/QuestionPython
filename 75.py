#Dictionary
d1={}
print(type(d1))
print(d1)

persons={'nk':50,'suresh':40,'kishore':60,'ramesh':30}
print(persons)

dict1={1:10,2:20,3:30,4:40}
print(dict1)

emp_dict={'empno':[1,2,3],'ename':['nk','ramesh','suresh']}
print(emp_dict)

#Example of creating dictionary using dictionary function
d1=dict()
print(d1)

list1=[12,23,34,45,56]
e=enumerate(list1)
dict1=dict(e)
print(dict1)

sales_list=[5000,6000,7000,8000,9000]
e=enumerate(sales_list,2000)
dict1=dict(e)
print(dict1)

list2=[(1,10),(2,20),(3,30),(4,40),(5,50)]
dict2=dict((list2))
print(dict2)

list1=[1,2,3,4,5,6]
list2=[10,20,30,40,50,60,70]
list3=[(list1[i],list2[i]) for i in range(len(list1))]
print(list3)

#zip()

list1=[1,2,3,4,5,6]
list2=[10,20,30,40]
dict1=dict(zip(list1,list2))
print(dict1)

list1=[1,2,3]
list2=[10,20,30]
z=zip(list1,list2,strict=True)   #list1==list2  must be
dict1=dict(z)
print(dict1)

str1='qwert'
str2='a7sdfg8'
z4=zip(str1,str2)
print(dict(z4))

dict5=dict(zip(range(1,10,2),range(1,20,3)))
print(dict5)

dict6=dict(zip(range(1,10),"ABCDEFGHI"))
dict7=dict(zip(range(1,10,2),["nk","suresh","ramesh","kishore","rajesh"]))
print(dict6)
print(dict7)

