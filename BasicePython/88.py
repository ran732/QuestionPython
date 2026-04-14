#QQ Remove duplicate values from the dictionary

# Original Dictionary ={1:"Aman",2:"Eleven",3:"Aman"}

# New Output= {1:"Aman",2:"Eleven"}

dict1={1:"Aman",2:"Eleven",3:"Aman"}
dict2={}
for i,j in dict1.items():
    if j not in dict2.values():
        dict2[i]=j

print(dict1)
print(dict2)