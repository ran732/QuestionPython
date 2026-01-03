# Write a program read scores of n players and display



scores = []

num=int(input("How many palyers : "))
for i in range (1,num+1):
    sc=int(input("Scores of the player is "))
    scores.append(sc)
    
        
    
print("Scores = ",scores) 
print("Max_Score = ",max(scores))    #max and min are predefined in list
print("Min_Score = ",min(scores))    
