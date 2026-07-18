import abc

class Animal(abc.ABC): #abstract class
    @abc.abstractmethod
    def eat(self):
        pass
    

class Dog(Animal):
    def eat(self): #method overriding
        print("Dog eats non-veg")
        
class Cow(Animal):
    def eat(self): #method overriding
        print("Cow eats veg") 
        
        
d1=Dog()
d1.eat()

c1=Cow() 
c1.eat()       
                   