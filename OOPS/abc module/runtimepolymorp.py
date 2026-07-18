import abc 

class Debitcard(abc.ABC):
    @abc.abstractmethod
    def withdraw(self):
        pass


class HDFCDebitcard(Debitcard):
    def withdraw(self):
        print("Withdraw 50000")
        
            

class SBIDebitcard(Debitcard):
    def withdraw(self):
        print("Withdraw 20000")
        
        
class ICICIATM:
    def insert(self,d):
        d.withdraw()
        


card1=HDFCDebitcard()
card2=SBIDebitcard()
atm1=ICICIATM()
atm1.insert(card1)                
atm1.insert(card2)                
                    