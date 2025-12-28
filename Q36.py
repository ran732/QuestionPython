# Write a program to display sum of even and odd between two numbers

num1=int (input("Enter num1 : "))
num2=int (input("Enter num2 : "))

Esum=0
Osum=0
for i in range (num1,num2):
    if i%2==0 :
        print(i)
        Esum=Esum+i
        
    else:
        Osum=Osum+i
        
print("oddsum= ",Osum)            
print("evensum= ",Esum)            