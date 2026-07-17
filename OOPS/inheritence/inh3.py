# Multilevel inheritance

class person:
    def __init__(self):
        self.__name =None
    def setName(self,n):
        self.__name=n
    def getName(self):
        return self.__name   
    
class employee(person):
    def __init__(self):
        super().__init__()
        self.__job =None
    def setjob(self,j):
        self.__job=j
    def getjob(self):
        return self.__job       
    
class SalariedEmployee(employee):
    def __init__(self):
        super().__init__()
        self.__salary=None
    def setSalary(self,s):
        self.__salary=s   
    def getSalary(self):
        return self.__salary
    
em=SalariedEmployee()
em.setName("Ran")
em.setjob("Developer")
em.setSalary(1000000)
name=em.getName()
job=em.getjob()
salary=em.getSalary()
print(f"Name {name} Job {job} Salary {salary}")         
                