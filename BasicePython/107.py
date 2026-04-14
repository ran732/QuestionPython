#username and password
users={'nk':'n123','ramesh':'r321','kishore':'k678'}
def signin(u,p):
    if u in users and users[u]==p:
        return True
    else:
        return False
  
user=input("Enter the username")    
pwd=input("Enter the password")  

if signin(user,pwd):
    print("welcome!")
else:
    print("Invalid username or password")    
  
    
    
#username and password
users={'nk':'n123','ramesh':'r321','kishore':'k678'}
def signin(u,p):
    if u in users and users[u]==p:
        print("Valid Password")
    else:
        print("Invalid username or password")
 
signin(user,pwd)
      