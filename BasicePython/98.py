# Input:
# The original dictionary is : {‘name’: [‘Jan’, ‘Feb’, ‘March’], ‘month’: [1, 2, 3]}

# Output:
# Flattened dictionary : {1: ‘Jan’, 2: ‘Feb’, 3: ‘March’}

dict1={'name': ['Jan', 'Feb', 'March'], 'month': [1, 2, 3]}
print(dict1)
dict2=dict(zip(dict1['month'],dict1['name']))
print(dict2)