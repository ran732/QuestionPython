print("****Menu****")
print("1.Area of Circle")
print("2.Area of Triangle")
print("3.Area of Rectangle")
print("4.Exit")


op=int(input("Enter a number from[1-4] : "))
match (op) :
    
 case 1 :
    r=float(input("Enter tha radius of circle : "))
    A=22/7*r*r
    print("Area of circle is ",A)
        
 case 2 :
    b=float(input("Enter tha base of triangle : "))
    h=float(input("Enter tha height of triangle : "))
    A=0.5*b*h
    print("Area of triangle is ",A)
    
 case 3 :
    l=float(input("Enter tha length of rectangle : "))
    b=float(input("Enter tha height of rectangle : "))
    A=l*b
    print("Area of rectangle is ",A)
    
 case 4:
    print("Thanks")    
     
         
 case  _:
    print("Invalid")    