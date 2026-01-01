# Displaying +ve and –ve values from list

list=[1,2,-4,5,-6,6,7,8,9,-10,9,1,2,-3,-4,12,-15,-12,11,-14,-13]
print(list)

num=len(list)

print("positive Numbers : ")
for i in range(num):
    if list[i]>=0:
      print(list[i],end=" ")
      
print("\nNegative Numbers : ")  
for i in range(num):
    if list[i]<0:
      print(list[i],end=" ")
          