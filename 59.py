#Comprehension

# list=[]
# for num in range(1,21):
#     list.append(num)
# print(list)    


# #Comprehension
list=[num for num in range(1,21)]
print(list)

num=[chr(i) for i in range(65,91)]
print(num)

num=[chr(i) for i in range(97,123)]
print(num)


nameslist=["nk","ramesh","suresh","kishore"]
print(nameslist)

nameslist=[i.upper() for i in nameslist]
print(nameslist)


# Create a list with n values
n=int(input("Enter the value of n "))
list_item=[ int(input("enter values : ")) for i in range(n)]
print(list_item)
