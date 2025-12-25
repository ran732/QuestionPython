# Write a program to find input year is leap or not


#2017 is not a leap year
#1900 is a not leap year
#2012 is a leap year
#2000 is a leap year

yr= int(input("Enput a year "))

if (yr%400==0 or yr%100!=0 and yr%4==0):
    print(yr," is a leap year.")
else:
    print(yr," is not a leap year.")    


