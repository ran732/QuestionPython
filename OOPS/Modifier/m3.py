class A :
    def __m1 (self): #private method
        print("private method")
    
    def m2 (self): #public method
        print("public method")
        self.__m1() #call private methos inside class
        
obj1=A()
obj1.m2()  

print()      
print()      
print()


class Account:    
    def __init__(self,a,c,b):
        self.__accno =a
        self.__aname =c
        self.__balance =b
    
    def deposit(self,t):
        self.__balance=self.__balance+t
        
    def withdraw(self,t):
        if self.__balance<t: #True
            print("Insufficient Balance")
        else: #False
            self.__balance=self.__balance-t  
            
    def getBalance(self):
        return self.__balance
    
    def printAccount(self):
        print(f'{self.__accno}, {self.__aname},{self.__balance}')          
      
while True :            
    print("1. Create Account ")            
    print("2. Deposit ")            
    print("3. Withdraw ")            
    print("4.Final Balance ")            
    print("5. Print Account Info ")            
    print("6. Exit ")   
             
    opt = int (input("Enter your choice : "))  
    
    if opt == 1:
        a=int(input("AccountNo :") )  
        c=input("Customername :")
        b=float(input("Balance :"))
        obj1=Account(a,c,b)    
        print("Account Created Successfully!!")      
          
    if opt == 2:
        amt=float(input("Amount :"))  
        obj1.deposit(amt) 
        print("Deposite Successfully!!")  
        
    if opt == 3:
        amt=float (input("Withdraw :")) 
        obj1.withdraw(amt)
        print("Withdrawal !")   
        
    if opt ==4 :
        bal=obj1.getBalance()   
        print(f'Balance is {bal:.2f}')
        
    if opt ==5 :
        obj1.printAccount() 
        
    if opt ==6:
        print("Exit Successfully from while loop !!")
        break
               