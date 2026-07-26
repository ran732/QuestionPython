import csv

with open (r"C:\Users\MANISH\Desktop\PYTHON A\QPython\QuestionPython\File handling\csv files\stud.csv",'r') as f:
    cr=csv.reader(f)
    for row in cr:
        print(row)
        
with open (r"C:\Users\MANISH\Desktop\PYTHON A\QPython\QuestionPython\File handling\csv files\stud.csv",'r') as f:
    cr=csv.reader(f)
    stud_details=list(cr) 
    print(stud_details)
    for s in stud_details:
        print(s)       
        
        