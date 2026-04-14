#Accept a key from the user and modify its values
email_dict={'naresh':'naresh@gmail.com',
            'suresh':'suresh@nareshit.com',
            'kishore':'k@gmail.com',
            'ramesh':'ramesh@gmail.com'}

# n=(input("ENTER : "))
# ky=list(n.split())
# val=[]
# for i in ky:
#     s=i+'@gmail.com'
#     val.append(s) 
# z=(zip(ky,val))
# print(dict(z)) 


print("before Updating : ")
print(email_dict)
name=input("Enter the name which has to update their email : ")
if name in email_dict:
    new=input( "new_email_id : ")
    email_dict[name]=new
    print(email_dict)
else:
    print("Not Found")    
    
    
    
