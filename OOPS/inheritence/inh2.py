class A:
    def __init__(self):
        self.x =100
        self.y =200
        
class B(A) :
    def __init__(self):
        super().__init__()
        self.p=300
        self.q=400
        
obB=B()
print(obB.p,obB.q)        
print(obB.x,obB.y)        






# Single Level Inheritance

class person:
    def __init__(self):
        self.__name =None
    def setName(self,n):
        self.__name=n
    def getName(self):
        return self.__name        
    
class Student(person):
    def __init__(self):
        super().__init__()
    def setCourse(self,c):
        self.__course = c        
    def getCourse(self):
        return self.__course    
    
s1=Student()
s1.setName("Ran")
s1.setCourse('Python')
name=s1.getName()
course=s1.getCourse()
print(f"Name {name} and Course {course}")
    