# Accept 10 numbers from user and display their avg

sum=0
for i in range (10):
    value=int(input("Enter 10 numbers "))
    sum=sum+value

print(sum)    
avg=sum/10
print("Average = ",avg)    