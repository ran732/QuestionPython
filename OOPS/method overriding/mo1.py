class Person: 
    
    def __init__(self):
        self.__name=None
        
    def read(self): #overriden method
        self.__name=input("Name ")    
        
    def print_info(self):  #overriden method
        print(f'Name {self.__name}')
       
class Employee(Person):
    def __init__(self):
        super().__init__()   
        self.__job=None        
    
    def read(self): #overriding method 
        # super().read()        ##############
        Person.read(self)
        self.__job=input("Enter job ")   
        
    def print_info(self):
        # Person.print_info(self)
        super().print_info() 
        print(f'job {self.__job}')   
        
em=Employee()
em.read()
em.print_info()