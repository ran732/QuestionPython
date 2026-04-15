class Car:
    def start(self): #instance method
        print(self,"Car start...")
    def stop(self): #instance method
        print(self,"Car stop...")  
        

audi=Car() #creating object of Car          
audi.start()
audi.stop()

bmw=Car() #creating object of Car          
bmw.start()
bmw.stop()