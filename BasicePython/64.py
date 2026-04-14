#Python program to check whether the string is Symmetrical or Palindrome

# Input: khokho
# Output: 
# The entered string is symmetrical
# The entered string is not palindrome

# Input:amaama
# Output:
# The entered string is symmetrical
# The entered string is palindrome


n=input("Enter : ")
half=int(0.5*len(n))
half=n[0:half]
full=half+half
print(full)
if n==full:
    print("Symmetrical")
else:
    print("Not Symmetrical")    