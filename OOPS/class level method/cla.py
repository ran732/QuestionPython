import datetime

class Person:
    def __init__(self,n,a):
        self.__name=n
        self.__age=a
        
    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age    
    
    @classmethod
    def createPerson(cls,n,dy):
        cy=datetime.date.today().year
        a=cy-dy
        p=Person(n,a)
        return p
    
p1=Person("RS",21)
print(p1.getName(),p1.getAge())
p2=Person.createPerson("Suru",2000)
print(p2.getName(),p2.getAge())
    