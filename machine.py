# def Add_student(students,name,marks):
#     if name in students:
#         print("duplicate data")
#     else:
#         students[name]=marks
#         print("students added successfully")

# def calculate_average(marks):
#     return round(sum(marks)/len(marks), 2)

# def display_students(students):
#     for name,marks in students.items():
#         average=calculate_average(marks)
#         print(f"NAME: {name} | MARKS: {marks} AVERAGE: {average}")

# def find_topper(students):
#     averages={}
#     for name,marks in students.items():
#         averages[name]=calculate_average(marks)
#     highest_average=max(averages.values())
#     for name,average in averages.items():
#         if average==highest_average:
#             print(f"TOPPER: {name} (AVERAGE:{highest_average})")


# def main_menu():
#     students={}
#     print("---Students Mark Analysis---")
#     print("1.Add student")
#     print("2.Display all students")
#     print("3.Find topper")
#     print("4.Exit")
#     while True:
#         choice=input("Enter your choice: ")
#         if choice=="1":
#             name=input("enter the student name: ")
#             mark_list=input("enter marks (comma seperated,eg.1,23,45): ")
#             marks=[]
#             for i in mark_list.split(","):
#                 number=int(i)
#                 marks.append(number)
#             Add_student(students,name,marks)
        
#         elif choice=="2":
#             display_students(students)
#         elif choice=="3":
#             find_topper(students)
#         elif choice=="4":
#             print("EXISTING...")
#             break
#         else:
#             print(" ")
# main_menu()




# Food Ordering System
class FoodItem:
    def _init_(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price
    def display_info(self):
        print(f"{self.item_id}. {self.name} - Rs {self.price}")

class Order:
    def _init_(self):
        self.cart = {} 

    def add_item(self, food_item, quantity):
        if food_item.item_id in self.cart:
            self.cart[food_item.item_id][1] += quantity
        else:
            self.cart[food_item.item_id] = [food_item, quantity]
        print(f"{food_item.name} x {quantity} added to cart.")

    def remove_item(self, item_id):
        if item_id in self.cart:
            removed_item = self.cart.pop(item_id)
            print(f"{removed_item[0].name} removed from cart.")
        else:
            print("Item not found.")
    def calculate_total(self):
        total = 0
        for item, qty in self.cart.values():
            total += item.price * qty
        return total

    def display_order(self):
        if not self.cart:
            print("Your cart is empty.")
            return
        print("\n---- Your Cart ----")
        for item, qty in self.cart.values():
            print(f"{item.name} x {qty} = Rs {item.price * qty}")
        print(f"Total: Rs {self.calculate_total()}")
def main():
    menu = [
        FoodItem(1, "Pizza", 150),
        FoodItem(2, "Burger", 100),
        FoodItem(3, "Sandwich", 80),
        FoodItem(4, "Fries", 60),
        FoodItem(5, "Coke", 40)
    ]
    order = Order()

    print("\n---- Food Ordering System ----")
    print("1. Show Food Menu")
    print("2. Add Item to Cart")
    print("3. Remove Item from Cart")
    print("4. View Cart")
    print("5. Checkout")
    while True:
        choice = input("Enter choice: ")

        if choice == "1":
            print("---- Food Menu ----")
            for food in menu:
                food.display_info()

        elif choice == "2":
                item_id = int(input("Enter the Item ID to add: "))
                quantity = int(input("Enter Quantity: "))
                food_item = None
                for f in menu:
                    if f.item_id == item_id:
                        food_item = f
                        break
                if food_item:
                    order.add_item(food_item, quantity)
                else:
                    print("Invalid Item ID.")

        elif choice == "3":
                item_id = int(input("Enter the Item ID to remove: "))
                order.remove_item(item_id)
        elif choice == "4":
            order.display_order()

        elif choice == "5":
            print("---- Checkout ----")
            order.display_order()
            print("Thank you for ordering!")
            break
        else:
            print("Invalid choice. Please try again.")
    main()