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
        self.base=b
        self.height=h
    def findArea(self):
        a=0.5*self.base*self.height
        print(f'Area of triangle is {a:2f}.')       
        return a     
        
cal=Calculator()
ad=cal.sum()
print(ad)  
sb=cal.sub()  
print(sb)     

t=Triangle(12,4)
print(t.findArea())