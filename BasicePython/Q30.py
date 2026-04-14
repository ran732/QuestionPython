# Write a program to genreate ascii table for uppercase letter

# A  --> 65
# B ---> 66
# C ---> 67
# Z --> 90

print("UPPERCASE TABLE")
for i in range (65,91):
    print(f'{i}---->{chr(i)}')
    
print("LOWERCASE TABLE")    
for j in range (97,123):
    print(f'{j}---->{chr(j)}')
    