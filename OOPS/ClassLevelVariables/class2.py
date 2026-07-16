class Product:
    count = 0 #class level variable
    def __init__(self,n,p):
        self.__name = n  #object level variable
        self.__price = p #object level variable
        
        Product.count=Product.count+1
        
    def printProduct(self):
        print(f'{self.__name},{self.__price}')  
        
print(Product.count)    #0   
p1=Product("Mouse",100)
p2=Product("Keyword",300)    

p1.printProduct()
p2.printProduct()

print(Product.count)  #2