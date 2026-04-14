# example

users_dict={'nk':'nit123','suresh':'s123','kishore':'t543'}
uname=input("username :")
pwd=input("password :")

if uname in users_dict:
    p=users_dict[uname]
    if p==pwd:
        print("Success")
    else:
        print("Invalid password")
else:
    print("Invalid username")            
    