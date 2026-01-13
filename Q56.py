# Creating nested list by input values at runtime (OR) create 2x2 matrix

matrix=[]
print("Enter the element of the matrix  ")
for i in range(3):
    row=[]
    for j in range(3):
        value=int(input("Enter value "))
        row.append(value)

    matrix.append(row)

print(matrix)
