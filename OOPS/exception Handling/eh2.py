# Write a program to input n elements into set and remove specific element
set1=set()
n=int(input("How many elements are in the set? "))
for i in range(n):
    user_inputs=int(input("Enter numbers : "))
    set1.add(user_inputs)

print(set1) 

rem_ele=int(input("Enter elements to remove : "))
try:
  set1.remove(rem_ele)
  print(set1) 
  
except KeyError:
    print("Not exist")     
# except KeyError as k:
#     print(f"{k} not exist in given set")  
    

  
   
    
    