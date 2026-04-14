# write a program to read marks for 3 students and 3 subjects (3x3)

marks=[]

for i in range(3):
    row=[]
    for i in range(3):
        mark=int(input("Enter the marks of the students : "))
        row.append(mark)
        
    marks.append(row )   
    
print(marks)    
        