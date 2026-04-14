# Write a program to generate the following series
# 1 4 9 16 25 36 ... n**2

num = int(input("Enter a number "))

for i in range (1,num+1):
    print(i*i,end=" ")
    