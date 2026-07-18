class Person:  #outer class
    
    class Address: #inner / member class
        def __init__(self):
            self.__hno=None
            self.__street=None
            self.__city=None
            
        def readAddress(self):
            self.__hno=input("Enter House No :")
            self.__street=input("Enter street : ")
            self.__city=input("Enter city : ")
            
        def printAddress(self) : 
            print({self.__hno},{self.__street},{self.__city}) 
            
            
    def __init__(self):
        self.__name=None
        self.__add=Person.Address()         
        
    def readPerson(self):
        self.__name=input("Enter name :")
        self.__add.readAddress()
        
    def printPerson(self):
        print(f"{self.__name}")        
        self.__add.printAddress()
            
                
                
p=Person()
p.readPerson()
p.printPerson()                