class A:
    def m1(self):
       print("Inside m1 method")
       
       class B: #local class
           def m2 (self):
               print("m2 inside B(Local class)")
               
       objb=B()
       objb.m2()
               
               
               
obja=A()
obja.m1()          