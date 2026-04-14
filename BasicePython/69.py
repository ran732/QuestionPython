# write a program for title case

str1=input("Enter : ")

str1=str1.split()
list=[]
for i in str1:
    i=i.capitalize()
    list.append(i)
    
print(list)

str2=' '.join(list)   
print(str2)   
            