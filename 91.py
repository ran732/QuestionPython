#Salary more than 25000
emp={1:("Amit",25000),2:("Suman",3000),3:("Ravi",36000) }


 
for key,value in emp.items():
    if value[1]>25000:
        print(key, value)