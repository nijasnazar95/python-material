# # 1.  pattern for diamond

# n=5
# for i in range(1,n+1):
#     spaces = n-i
#     stars = 2*i-1
#     print( " " * spaces + "*" * stars)

# for i in range(n-1,0,-1):
#     spaces = n-i
#     stars = 2*i-1
#     print(" " * spaces + "*" * stars)


# # 2. Armstrong or not

# n=int(input("Enter the numbers: "))
# sum=0
# temp=n
# digit=0
# while n>0:
#     rem=n%10
#     digit=rem**3
#     sum=sum+digit
#     n=n//10
# if sum==temp:
#     print(f"{temp} is armstrong")
# else:
#     print(f"{temp} is not armstrong")



# 1. BUfferfly pattern

# n=4
# for i in range(1, n + 1):

#     for j in range(1, i + 1):
#         if j == 1 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")


#     space = 2 * (n - i)
#     print("  " * space, end="")

#     for j in range(1, i + 1):
#         if j == 1 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")


# for i in range(n, 0, -1):

#     for j in range(1, i + 1):
#         if j == 1 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")


#     space = 2 * (n - i)
#     print("  " * space, end="")

#     for j in range(1, i + 1):
#         if j == 1 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()




# 1. Hollow Butterfly Pattern

# n = 5  # number of rows 

# Upper 
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if j == 1 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
    
#     for j in range(2 * (n - i)):
#         print(" ", end=" ")
    
#     for j in range(1, i + 1):
#         if j == 1 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# Lower 
# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         if j == 1 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
    
#     for j in range(2 * (n - i)):
#         print(" ", end=" ")
    
#     for j in range(1, i + 1):
#         if j == 1 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()






# class FoodItem:
#     def _init_(self, item_id, name, price):
#         self.item_id = item_id
#         self.name = name
#         self.price = price

#     def display_info(self):
#         print(f"{self.item_id}. {self.name} - Rs {self.price}")


# class Order:
#     def _init_(self):
#         self.cart = {}

#     def add_item(self, food_item, quantity):
#         if food_item.item_id in self.cart:
#             self.cart[food_item.item_id]['quantity'] += quantity
#         else:
#             self.cart[food_item.item_id] = {'item': food_item, 'quantity': quantity}
#         print(f"{food_item.name} x {quantity} added to cart.")

#     def remove_item(self, item_id):
#         if item_id in self.cart:
#             removed_item = self.cart.pop(item_id)
#             print(f"{removed_item['item'].name} removed from cart.")
#         else:
#             print("Item not found in cart.")

#     def calculate_total(self):
#         total = 0
#         for entry in self.cart.values():
#             total += entry['item'].price * entry['quantity']
#         return total

#     def display_order(self):
#         if not self.cart:
#             print("Your cart is empty.")
#         else:
#             print("\nYour Cart:")
#             for entry in self.cart.values():
#                 item = entry['item']
#                 qty = entry['quantity']
#                 print(f"{item.name} x {qty} = Rs {item.price * qty}")
#             print(f"Total: Rs {self.calculate_total()}")


# # -------- Main Program ----------
# def main():
#     # Preload Menu
#     menu = [
#         FoodItem(1, "Pizza", 150),
#         FoodItem(2, "Burger", 100),
#         FoodItem(3, "Sandwich", 80),
#         FoodItem(4, "Fries", 60),
#         FoodItem(5, "Coke", 40),
#     ]

#     order = Order()

#     while True:
#         print("\n---- Food Ordering System ----")
#         print("1. Show Food Menu")
#         print("2. Add Item to Cart")
#         print("3. Remove Item from Cart")
#         print("4. View Cart")
#         print("5. Checkout")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             print("\n---- Food Menu ----")
#             for item in menu:
#                 item.display_info()

#         elif choice == "2":
#             try:
#                 item_id = int(input("Enter Item ID to add: "))
#                 quantity = int(input("Enter Quantity: "))
#                 found = next((item for item in menu if item.item_id == item_id), None)
#                 if found:
#                     if quantity > 0:
#                         order.add_item(found, quantity)
#                     else:
#                         print("Quantity must be greater than 0.")
#                 else:
#                     print("Invalid Item ID.")
#             except ValueError:
#                 print("Invalid input. Please enter numbers only.")

#         elif choice == "3":
#             try:
#                 item_id = int(input("Enter Item ID to remove: "))
#                 order.remove_item(item_id)
#             except ValueError:
#                 print("Invalid input. Please enter a number.")

#         elif choice == "4":
#             order.display_order()

#         elif choice == "5":
#             print(f"Final Bill: Rs {order.calculate_total()} Thank you for ordering!")
#             break

#         else:
#             print("Invalid choice. Please try again.")


# if __name__ == "_main_":
#    main()


# class FoodItem:
#     def _init_(self, item_id, name, price):
#         self.item_id = item_id
#         self.name = name
#         self.price = price

#     def display_info(self):
#         print(f"{self.item_id}. {self.name} - Rs {self.price}")


# class Order:
#     def _init_(self):
#         self.cart = {}

#     def add_item(self, food_item, quantity):
#         if food_item.item_id in self.cart:
#             self.cart[food_item.item_id]['quantity'] += quantity
#         else:
#             self.cart[food_item.item_id] = {'item': food_item, 'quantity': quantity}
#         print(f"{food_item.name} x {quantity} added to cart.")

#     def remove_item(self, item_id):
#         if item_id in self.cart:
#             removed_item = self.cart.pop(item_id)
#             print(f"{removed_item['item'].name} removed from cart.")
#         else:
#             print("Item not found in cart.")

#     def calculate_total(self):
#         total = 0
#         for entry in self.cart.values():
#             total += entry['item'].price * entry['quantity']
#         return total

#     def display_order(self):
#         if not self.cart:
#             print("Your cart is empty.")
#         else:
#             print("\nYour Cart:")
#             for entry in self.cart.values():
#                 item = entry['item']
#                 qty = entry['quantity']
#                 print(f"{item.name} x {qty} = Rs {item.price * qty}")
#             print(f"Total: Rs {self.calculate_total()}")


# # -------- Main Program ----------
# def main():
#     # Preload Menu
#     menu = [
#         FoodItem(1, "Pizza", 150),
#         FoodItem(2, "Burger", 100),
#         FoodItem(3, "Sandwich", 80),
#         FoodItem(4, "Fries", 60),
#         FoodItem(5, "Coke", 40),
#     ]

#     order = Order()

#     while True:
#         print("\n---- Food Ordering System ----")
#         print("1. Show Food Menu")
#         print("2. Add Item to Cart")
#         print("3. Remove Item from Cart")
#         print("4. View Cart")
#         print("5. Checkout")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             print("\n---- Food Menu ----")
#             for item in menu:
#                 item.display_info()

#         elif choice == "2":
#             try:
#                 item_id = int(input("Enter Item ID to add: "))
#                 quantity = int(input("Enter Quantity: "))
#                 found = next((item for item in menu if item.item_id == item_id), None)
#                 if found:
#                     if quantity > 0:
#                         order.add_item(found, quantity)
#                     else:
#                         print("Quantity must be greater than 0.")
#                 else:
#                     print("Invalid Item ID.")
#             except ValueError:
#                 print("Invalid input. Please enter numbers only.")

#         elif choice == "3":
#             try:
#                 item_id = int(input("Enter Item ID to remove: "))
#                 order.remove_item(item_id)
#             except ValueError:
#                 print("Invalid input. Please enter a number.")

#         elif choice == "4":
#             order.display_order()

#         elif choice == "5":
#             print(f"Final Bill: Rs {order.calculate_total()} Thank you for ordering!")
#             break

#         else:
#             print("Invalid choice. Please try again.")


# if __name__ == "_main_":
#     main()




