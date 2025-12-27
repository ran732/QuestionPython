# Write a program to generate math table of input number

# 5
# 5x1=5
# 5x2=10
# ...
# 5x10=50


num=int(input("Enter a number "))
sum=0
for i in range (1,11):
    sum=sum+i
    print(num, "x",i,"=",num*i)
print("Sum=",sum)    