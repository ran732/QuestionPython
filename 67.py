str="pythonKFJGHRIUD"
str=str.lower()
print(str)

# Write a program to convert to string into lowercase

str1=input("enter : ")
str2=" "

for i in range(len(str1)):
   if str1[i]>='A' and str1[i]<='Z':
       str2=str2+chr(ord(str1[i])+32)
   else:
       str2=str2+str1[i]
       
print(str1)          
print(str2)          
    
