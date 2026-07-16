#CONSTRUCTOR METHOD & IT CALLs AUTOMATICALLY

class Student:
    def __init__(self):  #constructor method 
        print(" Student object is created. ") 
        
Student()  #print automatically       
Student()        
       
      
print()     
 #Constuctor without parameter
 
class Student:
    def __init__(self):
        self.rollno=0
        self.name=None
        self.course=None
        print("Executed Automatically")
         
s1=Student()         
s2=Student()    
print(s1.rollno,s1.name,s1.course)     
print(s2.rollno,s2.name,s2.course)     





