#palindrome
num=int(input("Enter a num : "))
def reverse(num,rev=0):
    if num==0:
        return rev
    else:
        return reverse(num//10,rev *10 +num%10)
    
if num==reverse(num):
    print("Palindrome")
else:
    print("Not Palindrome")        
    