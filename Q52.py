# Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. 
# Examples:  
# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]
# Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
# Output : [1, 5, 3, 4, 2]



list = []
Numlist=int(input("HOw many entites are there : "))

for i in range(1,Numlist+1):
    i=input("Entites : ")
    list.append(i)
    
print(list)   

list[0],list[2]=list[2],list[0] 

print("After swaping : ",list)

    
