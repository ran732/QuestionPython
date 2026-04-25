class Triangle:  #constructor or magic method or instance method
    def __init__(self):
        self.base=0.0
        self.height=0.0
    
    def setBase(self,b): #instance method
        self.base=b
    def setHeight(self,h):  #instance method
        self.height=h
        
    def findArea(self):   #instance method
        return self.base*self.height*0.5
    
t1=Triangle() #object creation

t1.setBase(2.43)              
t1.setHeight(4.56)       

area1=t1.findArea()       

print(f'Area of triangle is {area1}')


t2=Triangle() #object creation

t2.setBase(2.43)              
t2.setHeight(2.346)       

area2=t2.findArea()       

print(f'Area of triangle is {area2}')