text = "HELLO"

print(text.lower)    # sirf method dikhega
print(text.lower())  # method run hoga


#Recursion 
#when a function call itself

import sys
def sayHello():
    print("hello")
    sayHello() #recursive call
    

sys.setrecursionlimit(3)
sayHello()   
s=sys.getrecursionlimit()
print(s)    