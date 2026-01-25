# Reverse Words in a Given String in Python
# Input : str =" geeks quiz practice code"
# Output : str = code practice quiz geeks  
# Input : str = "my name is laxmi"
# output : str= laxmi is name my 

str =" geeks quiz practice code"
  
str=str.split()
str=str[::-1]
str=' '.join(str)
print(str)  