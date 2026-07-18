
users={'nk':'n123','nit':'n321','ramesh':'r567'}

class LoginError(Exception):
    def __init__(self, msg):
        super().__init__()  #calls the constructor of the parent Exception class.
        self.__msg=msg
    def __str__(self):
        return  self.__msg   
    
    
def login(usr,pwd):
    if usr in users and users[usr]==pwd:
        print("welcome back To my channel")
        
    else:
        raise LoginError("Invalid username or password")    
            
            
def main():
    uname=input("Enter username :")            
    pwd=input("Enter password :")   
    try:
        login(uname,pwd)
    except LoginError as l:
        print(l)      
              
        
(main())        