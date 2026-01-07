# Write a program to read n values into list
# remove given value from list

l=int(input("How much data you want to add : "))
list = []

for i in range(l):
    user=int(input("Bolo kuchh number : "))
    list.append(user)
    
print(list)   

q=int(input("Which one data you want to delete : "))

ard=list.index(q) 
del list[ard]

print("After deletion ",q,",list is ",list)