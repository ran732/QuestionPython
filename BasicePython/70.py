
# Membership testing

# Example:

# Count of each value in list
# Input:
# list1=[10,20,30,10,10,10,20,30,30,50]
# Output:
# 10 --> 4
# 20 --> 2
# 30 --> 3
# 50 --> 1


list1=[10,20,30,10,10,10,20,30,30,50]
set1=set(list1)
for value in set1:
    out=list1.count(value)
    print(f'{value} --> {out}')