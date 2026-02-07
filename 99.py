# Creating contacts application

contacts={}
while True:
   print("1.Add")
   print("2.Update")
   print("3.Remove")
   print("4.Search")
   print("5.List")
   print("6.Exit")
   
   opt=int(input("Enter any Option : "))
   if opt==1:
       name=input("Enter your name : ")
       if name not in contacts:
           number=int(input("Enter your number : "))
           contacts[name]=number  #add
           print(f'Contact Added!')
       else:
           print(f'{name} Exist!')    
           
   elif opt==2:
       name=input("Enter your name : ")
       if name in contacts:
           number=int(input("Enter your number : "))
           contacts[name]=number   #update
           print(f'Updated!')
       else:
           print(f'{name} not Found!')    
           
   elif opt==3:
       name=input("Enter your name : ")
       if name in contacts:
           del contacts[name] #delete
           print("Deleted Contact !")
       else:
           print(f'{name} not Found!')       
            
   elif opt==4:
       name=input("Enter your name : ")
       if name in contacts:    
           print(f'{name} --> {contacts[name]}')   #search 
       else:
           print(f'{name} not Found!')      
               
   elif opt==5:
       
       if contacts:
          for name,number in contacts.items():
              print(f'{name} --> {number}')
       else: 
           print(f'Contact not Found!')
   
   elif opt==6:
       print("Exit")
       break
   
         
                   