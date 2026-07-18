class Person:
    
    class __Date:
        
        def __init__(self):
            self.__dd=0
            self.__mm=0
            self.__yy=0
            
        def setDate(self,dd,mm,yy):
           self.__dd=dd
           self.__mm=mm
           self.__yy=yy   
        
        def printDate(self):
            return (f'{self.__dd}/{self.__mm}/{self.__yy}')
            
            
    def __init__(self):
        self.__name =None
        self.__dob=Person.__Date()  
        
    def setPerson(self,n,d,m,y):
        self.__name =n  
        self.__dob.setDate(d,m,y)
        
    def printPerson(self):
        p= self.__dob.printDate()
        print(f"{self.__name} date of birth {p}")
                    
        
        
p=Person()
p.setPerson("Ranjeet",17,7,2006)
p.printPerson()        