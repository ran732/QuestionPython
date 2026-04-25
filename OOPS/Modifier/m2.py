class Student :
    def __init__(self,r,n,c):
        self.__rollno = r   #private
        self.__name = n     #private
        self.__course = c   #private
        
    def displayStudent(self):
        print(f'Rollno : {self.__rollno}')    
        print(f'Name : {self.__name}')    
        print(f'Course : {self.__course}')    
        
obj1 = Student(106, "Ranjeet","Python")        

obj1.displayStudent()