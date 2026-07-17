# Multilevel inheritence

class A:
    def __init__(self):
        self.x=100
    
class B:
    def __init__(self):
        self.y=200
        
class C(A,B):
    def __init__(self):
        super().__init__()
        B.__init__(self)
        self.z=300     
        
ob=C()
print(ob.x,ob.y,ob.z,sep="\n")        
           
            