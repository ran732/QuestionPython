# while…else and for ..else


n=1
while n<=5:
    print(n)
    n=n+1
else:
    print("inside else block")

n=1
while n<=5:
    print(n)
    break
else:
    print("Inside else block")
 
 
 
 #for loop
 
print("  ")
print("  ")
print("  ")
print("  ")
print("  ")



for num in range(1,6): # 1 2 3 4 5
    print(num)
else:
    print("inside else block")


for num in range(1,6):
    print(num)
    break
else:
    print("inside else block")
