
# write a program to generate factorials of all numbers from 1-5

# 1 --> 1
# 2 --> 2
# 3 --> 6
# 4 --> 24
# 5 --> 120


# fact=1
# for i in range (1,6):
#     fact=fact*i
#     print(f'{i} --> {fact}')
    
    
for i in range (1,6):
    fact=1
    for j in range (1,i+1):
        fact=fact*j    
    print(f'{i} --> {fact}')
        
        

        