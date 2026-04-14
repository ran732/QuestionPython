# Count of even and odd number of list
list=[4,8,9,1,2,3,4,12,15,17,19,24,35,76,77,45,54,34,21]

print(list)
EN=0
OD=0
print("Even numbers :")
for i in range(len(list)):
    if list[i]%2==0:
        EN=EN+1
        print(list[i],end=" ")
print("\nEven number count",EN)    
        
print("\nOdd numbers :")
for i in range(len(list)):
    if list[i]%2!=0:
        OD=OD+1
        print(list[i],end=" ")    
        
print("\nOdd number count",OD)    
    