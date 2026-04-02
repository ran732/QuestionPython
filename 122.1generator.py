# A generator function is a special type of function in Python that produces values one-by-one instead of all at once.

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
        
gen = count_up_to(39)
print(next(gen))        
print(next(gen))        
print(next(gen))        
print(next(gen))        

print()
print()
print()
for num in gen:
    print(num)
    
#Generator Expression
gen = (x*x for x in range(5))

for i in gen:
    print(i)    
    
    
    
#     ✅ 5. Why Use Generator Functions?
# ⭐ Memory Efficient

# Normal list:

# nums = [x for x in range(1000000)]

# ➡ stores 10 lakh numbers in memory.

# Generator:

# nums = (x for x in range(1000000))



