import abc 

class Shape(abc.ABC):  #abstract class
    def __init__(self):
        self.dim1=None
        self.dim2=None
        
    def readDim(self):
        self.dim1=float(input("Enter Base :"))
        self.dim2=float(input( 'Enter Height :'))
    
    @abc.abstractmethod 
    def findArea(self):
        pass
    
    
class Triangle(Shape):
    def __init__(self):
        super().__init__()
    
    def findArea(self):
        return self.dim1*self.dim2*0.5
    
class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        
    def findArea(self):
        return self.dim1*self.dim2        
    
t=Triangle()
t.readDim()    
print(f" Area of triangle is {t.findArea()}")

r=Rectangle()
r.readDim()
print(f"Area of rectangle is {r.findArea()}")
        
       