
class InsuffError(Exception):
    def __str__(self):
        return "Insufficient Balance"


class Account:
    def __init__(self,an,cn,b):
        self.__accno=an
        self.__cname=cn
        self.__balance=b
    def deposit(self,t):
        self.__balance=self.__balance+t
    def withdraw(self,t):
        if t>self.__balance:
            raise InsuffError
        else:
            self.__balance=self.__balance-t
    
    def __str__(self):
        return f"{self.__accno},{self.__cname},{self.__balance}"        
            
            
def main():
    acc1=Account(101,"Ranjeet",200)
    print(acc1)
    try:
        acc1.deposit(400)
        print(acc1)
        acc1.withdraw(700)
        print(acc1)
    except InsuffError as a  :
        print(a) 
                
                
main()                
                    
     
       