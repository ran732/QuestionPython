class Engine:
    def start(self):
        print("Engine starting....")
        
    def stop(self):
        print("Engine Stoping....")
        
 
class Car:    
    def __init__(self):
        self.p=Engine()
        
    def carStart(self):
        self.p.start()
        
    def carStop(self):
        self.p.stop()
        
        
audi = Car()
audi.carStart()
audi.carStop()                        