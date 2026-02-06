#To Count the frequency of each words in a given string accepted from the user using dictionary

str1=input("Enter any striing : ")
words=str1.split()
d={}
for num in set(words):
   count= words.count(num)
   d[num]=count
print(d)   
    

