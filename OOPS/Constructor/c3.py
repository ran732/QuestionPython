class Calculator:
    def __init__(self):
        self.num1=10
        self.num2=12
    def sum(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    
class Triangle:
    def __init__(self,b=0,h=0):
        if b<0 or h<0:
            raise ValueError(" Base and height must be positive.")
        self.base=b
        self.height=h
    def findArea(self):
        a=0.5*self.base*self.height
        print(f'Area of triangle is {a:.2f}.')       
             
        
cal=Calculator()
ad=cal.sum()
print(ad)  
sb=cal.sub()  
print(sb)     

t=Triangle(12,6)
t.findArea()


###########################################

class Square:
    def __init__(self,a=0):
        self.side=a
        if a<0:
          raise ValueError ("Side can't be negative.")
    def Area(self):
        return self.side*self.side 
    
s1=Square(9)
area=s1.Area()
print(area)    