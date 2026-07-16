class Account:
    minBalance =500
    def __init__(self,a,n,b):
        self.__accno=a
        self.__cname =n
        self.__balance =b
        
    def deposit(self,t):
        self.__balance=self.__balance+t
        
    def withdraw(self,t):
        if (self.__balance-t)>self.minBalance:
          self.__balance=self.__balance-t 
        else:
            print("Insufficient") 
    
    
    def printAcc(self):
        return (f'AccountNo = {self.__accno},CustomerName = {self.__cname},Balance = {self.__balance}')       
        
c1=Account(102,"Ranjeet",0)
print(c1.printAcc())                 

c2=Account(107,"VK",10000000)
print(c2.printAcc())