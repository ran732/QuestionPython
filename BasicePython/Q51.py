# Python program to interchange first and last elements in a list

input = [12, 35, 9, 56, 24]
print(input)


# temp=input[0]
# input[0]=input[-1]
# input[-1]=temp

input[0],input[-1] =input[-1],input[0]

print(input)