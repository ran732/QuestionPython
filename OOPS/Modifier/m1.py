class A :
    def __init__(self): #constructor and call autometically
      self.__x=10   #private data
      self.__y=20   #private data
      self.x=30   #public data
      
    def m1(self):
        print("Public method")  
        
        
obj1=A()    
obj1.m1()
# print(obj1.__x)    throw error b'coz out of class
     
     