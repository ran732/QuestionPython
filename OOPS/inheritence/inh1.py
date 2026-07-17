#Single Level Inhertence

class A:  # base class/parent class/super class
    def m1(self):
        print("m1 in A")
        
    def m2(self):
        print("m2 in A")    
        
        
class B(A): #derived class/child class/sub class
    def m3(self):
        print("m3 in B")
    def m4(self):
        print("m4 iin B")
        

obB =B()
obB.m1()
obB.m2()
obB.m3()
obB.m4()
                   