# Write a program to capitalize string


str1=input("enter ")
str2=" "

for i in range(len(str1)):
    if i==0:
        if str1[i]>='a' and str1[i]<='z':
            str2=str2+ chr(ord(str1[i])-32)   #string is immutable so,,
        else:
            str2=str2+str1[i] 
            
    elif str1[i]>='A' and str1[i]<='Z':
            str2=str2+ chr(ord(str1[i])+32)   #string is immutable so,,
    else:
        str2=str2+str1[i]   
        
print(str1)              
print(str2)              
               
            
        
    