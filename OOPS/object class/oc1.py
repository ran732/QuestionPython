class Student:
    def __init__(self,r,n):
        self.__rollno=r
        self.__name=n
        
    def __str__(self):
        return f"{self.__name},{self.__rollno}"  
    
s1=Student(101,"rk")
print(s1)      
print(s1.__str__())      