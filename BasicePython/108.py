def fun1(w=100):
    print(w)
    
fun1()    #by default 100 if we not pass 
fun1(67)    

def DL(ch='*',length=45):
    for i in range(length):
        print(ch,end="")
    print()
DL()        
DL("&")        
DL(length=10)        
DL("<",50)        
        