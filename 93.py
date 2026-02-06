std={}
for i in range(2):
    name=(input("Enter the name : "))
    rollno=int(input("Enter the roll no : "))
    sub1=int(input("Enter Subject1 Marks: "))
    sub2=int(input("Enter Subject2 Marks: "))
    sub3=int(input("Enter Subject3 Marks: "))
    sum=print((sub1+sub2+sub3))
    std[rollno]=[name,sub1,sub2,sub3]
print(std)
    