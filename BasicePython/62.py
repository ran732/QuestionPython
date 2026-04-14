# Write a program to count alphabets,digits and special characters exists within string
a,d,o=0,0,0
str=input("enter any string :")
for i in str:

    

   if "a"<= i <="z" or "A"<= i <="Z" :
      a=a+1 
   elif "0"<= i<="9":
       d=d+1
   else: 
       o=o+1
              
print("Alphabet",a)
print("Digits",d)       
print("Other Charecters",o)   