import abc

class A (abc.ABC):  #abstract method
    @abc.abstractmethod
    def m1(self):
        pass
    
    
class B(A):
    def m1(self):  #overriding method
        print("overriding method")    
        
        
objb = B()
objb.m1()        