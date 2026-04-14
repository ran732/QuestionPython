# Write a program to add two matrices


matrix1=[]
print("Enter the element of the matrix1  ")
for i in range(3):
    row=[]
    for j in range(3):
        value=int(input("Enter value "))
        row.append(value)

    matrix1.append(row)

print(matrix1)


matrix2=[]
print("Enter the element of the matrix2  ")
for i in range(3):
    row=[]
    for j in range(3):
        value=int(input("Enter value "))
        row.append(value)

    matrix2.append(row)

print(matrix2)


matrix=[]
for i in range(3):
    row=[]
    for j in range(3):
        row.append(matrix1[i][j]+matrix2[i][j])

    matrix.append(row)

print(matrix)
