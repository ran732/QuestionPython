import pickle

student = {
    "name": "Ranjeet",
    "age": 20,
    "branch": "AIML"
}

with open("student.dat", "wb") as f:
    pickle.dump(student, f)

print("Data saved successfully.")