
# Ways to sort list of dictionaries by values in Python – Using itemgetter

# Input
# List1=[{"name": "Nandini", "age": 20},
#        {"name": "Manjeet", "age": 20},
#        {"name": "Nikhil", "age": 19}]

# Output:
# The list printed sorting by age: 
# [{'age': 19, 'name': 'Nikhil'}, {'age': 20, 'name': 'Nandini'}, {'age': 20, 'name': 'Manjeet'}]


from operator import itemgetter


list1=[{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

print(list1)
list2=sorted(list1,key=itemgetter("age"))
print(list2)

lsit3=sorted(list1,key=itemgetter("name","age"))
print(lsit3)