# Program: Online Food Ordering System

# This program allows users to place an order by specifying item names as keyword arguments along with their quantities.


def place_order(name,**items):
    
    if not items:
        print(f'{name}, you have not ordered anything yet!!')
    
    
    
    menu={
        'pizza':100,
        'burger':120,
        'fried':50,
        'Tanduri':200,
        'Komcha':75,
    }
    print("Menu available : ",menu)
    print(f'Ordered summary for {name} : ') 
    total_price=0
    for item,Quantity in items.items():
        
        if item in menu:
            price=menu[item] * Quantity
            total_price += price 
            print(f'{item} * {Quantity} = ₹{price}'  )
        else:
            print("Sorry",name ,item ," is currently not available !!")   
    print(f'Total Bill = {total_price}')     
       

print(place_order)

place_order("Aman",pizza=2,Komcha=2,odds=2)        
    


# def place_order(customer_name, **items):
#     """Function to take orders with keyword arguments."""
    
#     if not items:
#         print(f"Hello {customer_name}, you haven't ordered anything yet!")
#         return
    
#     print(f"\nOrder Summary for {customer_name}:")
    
#     total_price = 0
#     menu = {
#         "burger": 120,
#         "pizza": 250,
#         "pasta": 180,
#         "coffee": 80,
#         "fries": 100,
#     }
    
#     for item, quantity in items.items():
#         if item in menu:
#             price = menu[item] * quantity
#             total_price += price
#             print(f"{item.capitalize()} x {quantity} = ₹{price}")
#         else:
#             print(f"Sorry, {item} is not available.")
    
#     print(f"Total Bill: ₹{total_price}\n")

# # Example Usage
# place_order("Aman", burger=2, pizza=1, coffee=3)
# place_order("Riya", pasta=1, fries=2)
# place_order("John")  # No order placed

