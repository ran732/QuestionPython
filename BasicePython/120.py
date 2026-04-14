
# Chaining Decorators in Python

# Multiple decorators can be chained in Python.
# To chain decorators in Python, we can apply multiple decorators to a single function by placing them one after the other, with the most inner decorator being applied first.

def drawDollar(f):
    def draw2():
        print("$"*30)
        f()
        print("$"*30)
    return draw2
def drawStars(f):
    def draw1():
        print("*"*30)
        f()
        print("*"*30)
    return draw1

@drawDollar
@drawStars
def display():
    print("PYTHON")
display()   

# display=drawDollar(drawStars(display)) 
# display()
