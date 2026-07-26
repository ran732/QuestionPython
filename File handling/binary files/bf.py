# Creating binary file
with open("file1.dat","wb") as f:
    b=bytes([65,66,67,68,69,70])
    f.write(b)
    
print("Data is written inside file.") 


# Reading data from binary file

with open("file1.dat","rb") as f:
    b=f.read()
    print(b)
    for x in b:
        print(x)


   
