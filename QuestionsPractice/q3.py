# student ={
#     "name": "Ranjeet",
#     "age":20,
#     "branch":"AIML",
#     "Course":"B-Tech",
# }

# print(student)

# student["age"]=21
# student["city"]="kanpur"

# for key in student:
#     print(key,student[key])

# print(student.keys())
# print(student.values())


student ={
    "name": "Ranjeet",
    "age":20,
    "marks":{
        "math":90,
        "history":94
    },
    "branch":"AIML",
    "Course":"B-Tech",
}

student["marks"]["history"] = 98
(student["marks"])["Physics"] = 96
print(student)