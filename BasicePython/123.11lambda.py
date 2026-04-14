# A lambda function in Python is a small anonymous function — meaning a function without a name.
# It is mainly used when you need a short function for a short time.


#normal function
def square(x):
    return x*x

s=square(6)
print(s)


#lambda function

square = lambda x: x*x
print(square(5))

add = lambda a, b: a + b
print(add(3, 4))


students = [("Ranjeet", 22), ("WAmit", 20), ("Rahul", 21)]
students.sort(key=lambda x:x[1])
print(students)
s=dict(students)
print(s)


# ✅ What happens step-by-step

# map() reads the list num.

# Then it sends each value one by one into x.

nums = [1,2,3,4]
result = list(map(lambda x:x*x, nums))    #map(function, iterable)
print(result)
