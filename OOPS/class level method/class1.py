class Student:
    __count = 0 
    
    @classmethod
    def getStudentCount(cls):
        return cls.__count
    
    def __init__(self):
        self.__rollno = 0
        self.__name = None
        Student.__count = Student.__count +1
        
k=Student.getStudentCount()
print(k)      #0  

s1=Student()
s2=Student()

k=Student.getStudentCount()
print(k)   #2