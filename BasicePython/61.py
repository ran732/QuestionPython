#  Maximum and Minimum K elements in Tuple


test_tup = (3, 7, 1, 18,23,34,56,767, 9)
k=2
test_tup=sorted(test_tup)
print(tuple(test_tup[:k])+tuple(test_tup[-k:]))





# Python program to create a list of tuples from given list having number and its cube in each tuple

# Input: list = [1, 2, 3]
# Output: [(1, 1), (2, 8), (3, 27)]

# Input: list = [9, 5, 6]
# Output: [(9, 729), (5, 125), (6, 216)]


list = [9, 5, 6]
list=[(num,num**3) for num in list]
print(list)