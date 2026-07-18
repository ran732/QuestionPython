import abc

class Sim(abc.ABC):
    @abc.abstractmethod
    def connect(self):
        pass
    

class Airtel(Sim):
    def connect(self):
        print("Good network of Airtel Bharti")
        
        
class BSNL(Sim):
    def connect(self):
        print("Respect TATA network")           
            
            
class Jio(Sim):
    def connect(self):
        print("Yeah have a network of jio")       
        
        
class Mobile:
    def insert(self ,s):
        s.connect()                 
        
        
        
s1=Airtel()
s2=BSNL()
s3=Jio()

m=Mobile()

m.insert(s1)        
m.insert(s2)        
m.insert(s3)        