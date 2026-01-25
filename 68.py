s1="jfgJHHmkhjijkdsHUU"
s2=s1.swapcase()
print(s2)

# Write a program for swapcase
str1=input("Enter : ")
str2=" "

for ch in str1:
    if ch>='A'and ch<='Z':
        str2=str2+chr(ord(ch)+32)
    elif ch>='a'and ch<='z':
        str2=str2+chr(ord(ch)-32)
   
print(str1)   
print(str2)   
            