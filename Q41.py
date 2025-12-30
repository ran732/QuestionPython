# Write a program to generate the following output
#1 2 3 4 5 6 7 8 9 10
#2 4 6 8 10 12 14 16 18 20
# 3 6 9 12 15 18 21 24 27 30
#....
# 10 20 30 40 50 60 70 80 90 100

# Using While loop
 
n=1
while n<=10 :    # Outer loop

    
    i=1
    while i<=10 :    # inner loop

        print(n*i,end=" ")
        i+=1
    print()
    n+=1    
    