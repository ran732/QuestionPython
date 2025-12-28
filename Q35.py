# Accept 10 numbers from user and find maximum and minimum value

# min_num=0
# max_num =0

for i in range (10):
    value=int(input("Enter 10 numbers "))
    
    if i==0 :
       max_num =value
       min_num=value
    else:
      if value>max_num:
        max_num=value
      elif value<min_num :
        min_num=value
        
print("Maximum Value =",max_num)        
print("Minimum Value =",min_num)        
        
        
    
    