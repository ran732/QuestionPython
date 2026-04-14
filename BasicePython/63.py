# Python program to check if a string is palindrome or not
# madam --> madam
# aba --> aba


n = input("enter : ")
for i in n:
    p=(n[::-1])
if n==p:
    print("Palindrome!")
else: 
    print("No palindrome")       