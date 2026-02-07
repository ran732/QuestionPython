# Create dictionary to store details of n players

#Comprehension method
n=int(input(" Enter the players number : "))
details={input("Name "):input("Scores ") for i in range(n)}
# print(details)
for name, scores in details.items():
    print(f'{name}-->{scores}')
    



#Detail Descriptions
dict1={}
for i in range(n):
    name=input("name ")
    scores=input("scores ")
    dict1[name]=scores
    print(dict1)
    