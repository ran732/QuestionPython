Q=[]
while True:
    print("1. Adding")
    print("2. Removing")
    print("3. Display")
    print("4. Exit")
    opt=int(input("Enter your option  (1-4) : "))
    
    if opt==1:
        value=int(input("Enter any value : "))
        Q.append(value)
        print(value,"added inside Queue!")
        
    elif opt==2: 
        if len(Q)==0:
            print("Queue is Empty" )
            
        else:    
            value=Q[0]
            del Q[0]
            print(value,"deleted from the Queue!")   
        
    elif opt==3:
        print(Q)
    elif opt==4:
        break    
    else:
        print("Invalid options")