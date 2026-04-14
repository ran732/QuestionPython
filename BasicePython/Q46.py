# Write a program to add all the values of list

list=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


sum=0
for i in range(len(list)):
    sum=sum+list[i]
print("Sum = ",sum) 
avg=sum/len(list)
print("Average = ",avg)   
    