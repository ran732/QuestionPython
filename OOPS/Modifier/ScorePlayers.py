# Write a program to read the scores of n players and display

class Player:
    def __init__(self,n,s):
        self.__name = n
        self.__score = s
    
    def getName(self):
        return self.__name 
    
    def getScore(self):
        return self.__score
    
n=int(input("Enter the number of players : "))
list1=[]
for i in range(n):
    name=input("Name of players : ")
    score=int(input("Enter the scores : "))
    p=Player(name,score) #Creating Object
    list1.append(p)
        
for p in list1:
    name=p.getName()    
    score=p.getScore()    
    print(name,score )
           