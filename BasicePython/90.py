# WAP to store information of products like product id,product name and product price in a dictionary by taking product is as a key


dict1={}
n=int(input("how many of your product? "))
for i in range(n):
    pNP=input("Enter your productName"),float(input("Enter your productPrice"))
    pI=int(input("Enter your productID"))
    
dict1[pI]=pNP
print(dict1)

for i in range(n):
    pNP=[input("Enter your productName"),float(input("Enter your productPrice"))]
    pI=int(input("Enter your productID"))
    
dict1[pI]=pNP
print(dict1)