# Python program to find smallest & gratest number in a list

run=[50, 30, 20, 10, 50, 60]
print(run)

min=run[0]
max=run[0]
total=0
for i in range (len(run)):
    total = total + run[i]
    if run[i]<min :
      min=run[i]
    if run[i]>max :
      max=run[i]  
print("Minimun = ",min)      
print("maximum = ",max)            
print("Total",total)        
        
        
        