# Write a program to print number in words

# 123

# ONE TWO THREE

# 489

# Four Eight Nine


num=int(input("Enter any number "))

words = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}

result = " "

if num==0 :
    print("Zero")
    
else:
    while num > 0:
       r=num%10
       result =words[r] + " " + result
       num=num//10
    
print(result)    
        