# Write a program to count
# alphabets, digits and sepcial character exists within input string

str=input("Enter any string ")  
ab=0
d=0
sc=0
for ch in str :
    if  "a"<ch<"z" or "A"<ch<"Z ":
        ab=ab+1
       
    elif "0"<ch<"9" :
        d=d+1
            
    else:
        sc=sc+1
         
print("Alphabates are : ",ab)
print("Digits are : ",d)
print("Special Characters are : ",sc)   
print("The end")