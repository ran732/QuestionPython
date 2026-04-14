# Write a program to filter data
#enen and odd

num_list=[2,8,1,2,9,5,11,15,17,18,21,89,34,56,87,23,32,37,87,56,45,34,23,12]

even=[]
odd=[]
for i in range(0,len(num_list)):
    if num_list[i]%2==0:
        even.append(num_list[i])
    else:
        odd.append(num_list[i])
        
print(num_list)        
print("EvenNum = ",even)    
print("OddNum = ",odd)    