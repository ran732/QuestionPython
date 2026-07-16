class Date:
    def __init__(self,d=0,m=0,y=0):
        self.dd=d
        self.mm=m
        self.yy=y
        
d1=Date()
print(d1.dd,d1.mm,d1.yy)
d2=Date(19,4,2026)
print(d2.dd,d2.mm,d2.yy)   
     

print()
#################################################
class Employee:
    def __init__(self,eno,en,s): #constuctor bind with instance method
        self.empno=eno
        self.empname=en
        self.salary=s
    def printEmployee(self):
        print(self.empno,self.empname,self.salary)
        
e1=Employee(1022,"Ranjeet",2000000)
e2=Employee(1023,"Auran",2500000)
# print(e1.empno,e1.empname,e1.salary)
# print(e2.empno,e2.empname,e2.salary)

e1.printEmployee()
e2.printEmployee()
        
    
#########################################

class Employee:
    def __init__(self,eno,en,s):
        self.empno=eno
        self.ename=en
        self.salary=s
        
    def EmployeeAddress(self):
       print(self.empno,self.ename,self.salary)        
        
e1=Employee(23,"Arav",30000) 
e2=Employee(233,"Niwas",450000) 

e1.EmployeeAddress()
e2.EmployeeAddress()
     