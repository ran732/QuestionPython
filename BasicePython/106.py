# Write a function to convert string to uppercase

def upper(s:str)->str:
    us=""
    for ch in s:
        if ch>='a' and ch<='z':
            us=us+chr(ord(ch)-32)
        else:
            us=us+ch
    return(us)    

str1=input("Enter any string : ") 
str2=upper(str1)
print(str1)       
print(str2)       
    
    