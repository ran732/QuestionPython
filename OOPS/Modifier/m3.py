class A :
    def __m1 (self): #private method
        print("private method")
    
    def m2 (self): #public method
        print("public method")
        self.__m1() #call private methos inside class
        
obj1=A()
obj1.m2()  



