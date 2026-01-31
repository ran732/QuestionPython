
# Count of each character exist within string
# input:
# abcaaabbca
# Output
# 5a3b2c

str1="abcaaabbca"
set1=set(str1)
str2=""
print(set1)
for i in set1:
    c=str1.count(i)
    str2=str2+str(c)+i
print(str2)