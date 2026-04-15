class Calculator:
    def add(self,n1,n2):#instance method with parameter
        return n1+n2
    def sub(self,n1,n2): #instance method with parameter
        return n1-n2
    
cal=Calculator()    
print(cal.add(10,20))
print(cal.sub(10,20))