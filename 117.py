# Program: Online Food Ordering System

# This program allows users to place an order by specifying item names as keyword arguments along with their quantities.


def place_order(customer_name, **items):
    """Function to take orders with keyword arguments."""
    
    if not items:
        print(f"Hello {customer_name}, you haven't ordered anything yet!")
        return
    
    print(f"\nOrder Summary for {customer_name}:")
    
    total_price = 0
    menu = {
        "burger": 120,
        "pizza": 250,
        "pasta": 180,
        "coffee": 80,
        "fries": 100
    }
    
    for item, quantity in items.items():
        if item in menu:
            price = menu[item] * quantity
            total_price += price
            print(f"{item.capitalize()} x {quantity} = ₹{price}")
        else:
            print(f"Sorry, {item} is not available.")
    
    print(f"Total Bill: ₹{total_price}\n")

# Example Usage
place_order("Aman", burger=2, pizza=1, coffee=3)
place_order("Riya", pasta=1, fries=2)
place_order("John")  # No order placed

