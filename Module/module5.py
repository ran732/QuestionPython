import user as u 

uname=input("Enter username: ")
pwd=input("Enter password : ")

if u.login(uname,pwd):
    print(f'{uname}, welcome')
else:
    print("Invalid username or password")    