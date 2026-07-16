class  Math:
    
    @staticmethod
    def power(num,p):
        return num**p
    
    @staticmethod
    def factorial(num):
        if num==0:
          return   1
        else:
            return num*Math.factorial(num-1)
        
    @staticmethod
    def isEven(num):
        return num%2==0
    
    @staticmethod
    def isOdd(num):
        return num%2 !=0
    
r1=Math.power(2,3) #8
r2=Math.factorial(5) #120
r3=Math.isEven(34) #True
r4=Math.isOdd(45)  #True
r5=Math.factorial(0) #1
print(r1,r2,r3,r4,r5)        
      
      