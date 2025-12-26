# Write a program to find length of number or count digits of input number


user=int(input("Enter any number : "))
count=0

if user==0:
    print("Length of number is 1")  
else:
    while user>0:
      user =user//10
      count= count+1
    
    print("Length of number is ",count)    