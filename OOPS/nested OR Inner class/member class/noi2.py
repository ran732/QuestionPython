class A:
    
    class B: #public member class
        def m1(self):
            print("m1 of b class ")
            

objb=A.B()
objb.m1()         




class X:
    class __Y: #private member class
        def m1(self):
            print("M1 of y class")   
            
    def m2(self):
        objy=X.__Y()
        objy.m1()

    
        
objx=X()
objx.m2()                