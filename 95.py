#Q.WAP to accept a key from the user and remove that key from the dictionary if present.

dict1={1:10,2:20,3:30,4:40,5:50}
print('Before removing anything : ',dict1)
user=int(input(" Enter any key : "))
if user in dict1:
    dict1.pop(user)
    print('After Updating : ',dict1)
else:
    print("Not in dict1")    