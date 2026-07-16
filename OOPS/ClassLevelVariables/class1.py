class A:
    x=100 #class level variables
    
    def __init__(self):
        self.y=200 #object level variables
        
print(A.x)        

ob = A()  #object create
print(ob.y)