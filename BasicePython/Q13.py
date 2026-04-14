# Write a program to convert input alphabet into uppercase to lower case,
# lowercase to uppercase


alpha =str(input("Enter any Alpabate "))

if   'A'<=alpha<='Z' :
    new=ord(alpha)+32
    new=chr(new)
    print("Lowercase Alphabate is ",new)
    
elif 'a'<=alpha<='z' :
    new=ord(alpha)-32
    new=chr(new)
    print("Uppercase Alphabate is ",new)
else:
    print("Please type a single alphabate")    

    
    