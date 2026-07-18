import abc 

class Shape(abc.ABC):  #abstract class
    def readDim(self):
        self.dim1=float(input("Enter Base :"))
        self.dim2=float(input( 'Enter Height :'))
    
    @abc.abstractmethod 
    def findArea(self):
        pass
    
    
class Triangle(Shape):
    # def readDim(self):
    #     return super().readDim()
    #     # self.dim1=float(input())
    #     # self.dim2=float(input())
    
    def findArea(self):
        return self.dim1*self.dim2*0.5
    
t=Triangle()
t.readDim()    
print(t.findArea())
        
       