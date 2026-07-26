import json

with open("emp.json",'w') as f:
    emp_dict={
        'empno':[1,2,3],'ename':['ak','gy','mn'],'salary':[200,300,400]
    }
    json.dump(emp_dict,f)
    
with open("ipl.json",'w') as f:
    emp_dict={
        
         "empno": [1, 2, 3],
         "ename": ["virat", "rohit", "dhoni"], 
         "salary": [200, 300, 400]

    }
    json.dump(emp_dict,f)    
    
print("data is written inside emp.json file")

with open("emp.json",'r') as f:
    emp_dict=json.load(f)
    print(emp_dict)  
    
print()      
    
with open("emp.json",'r') as f:
    emp_dict=json.load(f)
    for i,j in emp_dict.items():
      print(i,j)   
         
print()   
    
    
try:    
    with open("ipl.json",'r') as f:
        emp_dict=json.load(f)
        for i,j in emp_dict.items():
          print(i,j)    
except Exception as e:
    print("Error",e)               
    