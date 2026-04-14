# Input:
# The original dictionary is : {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}
# Output:
# The unique values list is : [1, 2, 5, 6, 7, 8, 10, 11, 12]


dict1={'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}

list1=[]
for i in dict1.values():
    list1.extend(i)
list1=list(set(list1))
print(list1)
    
