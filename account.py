class Account:
    def __init__(self,a,b,c):
        self.__accno=a
        self.__accname=b
        self.__accb=c
        
    def deposit(self,t):
        self.__accb=self.__accb + t    
    def withdraw(self,t):
        if self.__accb<t:
            print("Insufficient Balance")
        else:
            self.__accb=self.__accb - t
    def getBalance(self):
        return self.__accb
    def AccountDetails(self):
        print(f'{self.__accno},{self.__accname},{self.__accb}')
        
obj = None
while True :            
    print("1. Create Account ")            
    print("2. Deposit ")            
    print("3. Withdraw ")            
    print("4.Final Balance ")            
    print("5. Print Account Info ")
    print("6. Exit ") 
    
    op = int(input("Enter your choices : "))
    
    
    
    if op == 1:
        a = input("Enter Account no : ")
        b = input("Enter Account Holder :")
        c = float(input("Enter balance :"))
        obj =Account(a,b,c)      
        print("Account Created Successfully!")  
    
    if obj == None:
        print("Account Create first!")    
        
    if op ==2:
        amount = float(input("Enter Amount :") )  
        obj.deposit(amount)
        print("Deposit Successfully!")
        
    if op ==3:
        withdraw = float(input("Enter Amount :"))
        obj.deposit(withdraw)  
        print("Withdraw Successfully!")
        
    if op ==4:
        bal=obj.getBalance()  
        print(f'Balance is {bal}')  
        
    if op == 5:
        det=obj.AccountDetails()    
        
        
    if op==6:
        print("Exit from the loop!")
        break    
                    
                    
        