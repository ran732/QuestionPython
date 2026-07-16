class Circle:
    __pi=3.14
    def __init__(self,x):
        self.__r=x
    def findArea(self):
        return self.__r*self.__r*Circle.__pi    
    
    @classmethod
    def setPI(cls,p):
        cls.__pi=p
        
c1=Circle(1.5)    
c2=Circle(4.5)    
Circle.setPI(3.147)   
a1=c1.findArea()
a2=c2.findArea()
print(f"Area of c1 {a1:.3f}")
print(f"Area of c2 {a2:.3f}")