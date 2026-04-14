#Example

list1=[i for i in range(1,6)]
list2=[i for i in range(10,60,10)]
print(dict(zip(list1,list2)))

d1={1:10,2:20,3:30}
print(d1[1])
print(d1[2])
print(d1[3])

prod_dict={'keyboard':1000,'mouse':300,'monitor':7000}
for products in prod_dict:
    print(products)   #keys

for products in prod_dict:
    print(prod_dict[products])    #values
    
for products in prod_dict:
    print(products,prod_dict[products])    #both    
    