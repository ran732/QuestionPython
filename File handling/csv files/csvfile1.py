import csv
import sys

try:
    with open(r"C:\Users\MANISH\Desktop\PYTHON A\QPython\QuestionPython\File handling\csv files\stud.csv", "w", newline="") as f:
        cw=csv.writer(f)
        while True:
            rollno=int(input("Rollno "))
            name=input("Name ") 
            course=input("Course ")
            cw.writerow([rollno,name,course])
            ans=input("Add another student? ")
            if ans =='no':
                break
except:
    t=sys.exc_info()
    print(t)            

finally:
    f.close()        
