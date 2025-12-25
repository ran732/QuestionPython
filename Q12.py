# Write a program to find input character is alphabet,digit or sepcial character

ch=input("Enter any character ")
if ch>='A' and ch<='Z' or ch>='a' and ch<='z':
    print("alphabet")
elif ch>='0' and ch<='9':
    print("digit")
else:
    print("special character")
