def view_expense():
#     try:
#         with open("expenses.txt", "r") as file:
#             data = file.readlines()

#             print("\nYour Expenses:")
#             for line in data:
#                 name, amount = line.strip().split(",")
#                 print(f"{name} - ₹{amount}")

#     except FileNotFoundError:
#         print("No expenses found.\n")


# def total_expense():
#     total = 0
#     try:
#         with open("expenses.txt", "r") as file:
#             data = file.readlines()

#             for line in data:
#                 name, amount = line.strip().split(",")
#                 total += float(amount)

#         print(f"\nTotal Expense: ₹{total}\n")

#     except FileNotFoundError:
#         print("No data available.\n")


# while True:
#     print("1. Add Expense")
#     print("2. View Expenses")
#     print("3. Total Expense")
#     print("4. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":
#         add_expense()
#     elif choice == "2":
#         view_expense()
#     elif choice == "3":
#         total_expense()
#     elif choice == "4":
#         print("Goodbye 👋")
#         break
#     else:
#         print("Invalid choice\n")