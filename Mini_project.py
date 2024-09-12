import csv

# Load products from CSV
def load_products():
    try:
        with open("products_list.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []

# Load couriers from CSV
def load_couriers():
    try:
        with open("couriers_list.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []

# Load orders from CSV
def load_orders():
    try:
        with open("orders_list.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []

# Save products to CSV
def save_products(products):
    with open("products_list.csv", "w", newline="") as file:
        fieldnames = ["name", "price"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for product in products:
            writer.writerow(product)

# Save couriers to CSV
def save_couriers(couriers):
    with open("couriers_list.csv", "w", newline="") as file:
        fieldnames = ["name", "phone"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for courier in couriers:
            writer.writerow(courier)

# Save orders to CSV
def save_orders(orders):
    with open("orders_list.csv", "w", newline="") as file:
        fieldnames = ["customer_name", "customer_address", "customer_phone", "courier", "status", "items"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for order in orders:
            writer.writerow(order)

# Main menu
def main_menu():
    while True:
        print("\nMain Menu:")
        print("0: Exit")
        print("1: Products Menu")
        print("2: Couriers Menu")
        print("3: Orders Menu")

        user_input = input("Choose an option: ")
        if user_input == "0":
            save_products(products)
            save_couriers(couriers)
            save_orders(orders)
            print("Exiting the app.")
            break
        elif user_input == "1":
            product_menu()
        elif user_input == "2":
            couriers_menu()
        elif user_input == "3":
            orders_menu()
        else:
            print("Invalid option. Please choose a valid menu option.")

# Product menu
def product_menu():
    while True:
        print("\nProducts Menu:")
        print("0: Return to main menu")
        print("1: Product list")
        print("2: Create new product")
        print("3: Update existing product")
        print("4: Delete product")
        
        user_input = input("Choose an option from 0 - 4: ")
        
        try:
            user_input = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if user_input == 0:
            print("Returning to main menu.")
            break
        elif user_input == 1:
            print(products)
        elif user_input == 2:
            create_product()
        elif user_input == 3:
            update_product()
        elif user_input == 4:
            delete_product()
        else:
            print("Invalid option. Please choose a valid menu option.")

def create_product():
    name = input("Enter new product name: ")
    price = input("Enter new product price: ")
    new_product = {"name": name, "price": price}
    products.append(new_product)
    save_products(products)
    print(f"Product '{name}' added.")

def update_product():
    print("\nProduct list:")
    for index, product in enumerate(products):
        print(f"{index}: {product}")
    try:
        product_index = int(input("Enter the index of the product to update: "))
        if 0 <= product_index < len(products):
            product = products[product_index]
            for key in product:
                new_value = input(f"Enter new value for {key} (leave blank to keep current value): ")
                if new_value:
                    product[key] = new_value
            print(f"Product at index {product_index} updated.")
            save_products(products)
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_product():
    print("\nProduct list:")
    for index, product in enumerate(products):
        print(f"{index}: {product}")
    try:
        product_index = int(input("Enter the index of the product to delete: "))
        if 0 <= product_index < len(products):
            deleted_product = products.pop(product_index)
            save_products(products)
            print(f"Product '{deleted_product}' deleted.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Couriers menu
def couriers_menu():
    while True:
        print("\nCouriers Menu:")
        print("0: Return to main menu")
        print("1: Courier list")
        print("2: Create new courier")
        print("3: Update existing courier")
        print("4: Delete courier")
        
        user_input = input("Choose an option from 0 - 4: ")
        
        try:
            user_input = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if user_input == 0:
            print("Returning to main menu.")
            break
        elif user_input == 1:
            print(couriers)
        elif user_input == 2:
            create_courier()
        elif user_input == 3:
            update_courier()
        elif user_input == 4:
            delete_courier()
        else:
            print("Invalid option. Please choose a valid menu option.")

def create_courier():
    name = input("Enter new courier name: ")
    phone = input("Enter new courier phone number: ")
    new_courier = {"name": name, "phone": phone}
    couriers.append(new_courier)
    save_couriers(couriers)
    print(f"Courier '{name}' added.")

def update_courier():
    print("\nCourier list:")
    for index, courier in enumerate(couriers):
        print(f"{index}: {courier}")
    try:
        courier_index = int(input("Enter the index of the courier to update: "))
        if 0 <= courier_index < len(couriers):
            courier = couriers[courier_index]
            for key in courier:
                new_value = input(f"Enter new value for {key} (leave blank to keep current value): ")
                if new_value:
                    courier[key] = new_value
            print(f"Courier at index {courier_index} updated.")
            save_couriers(couriers)
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_courier():
    print("\nCourier list:")
    for index, courier in enumerate(couriers):
        print(f"{index}: {courier}")
    try:
        courier_index = int(input("Enter the index of the courier to delete: "))
        if 0 <= courier_index < len(couriers):
            deleted_courier = couriers.pop(courier_index)
            save_couriers(couriers)
            print(f"Courier '{deleted_courier}' deleted.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Orders menu
def orders_menu():
    while True:
        print("\nOrders Menu:")
        print("0: Return to main menu")
        print("1: View all orders")
        print("2: Create new order")
        print("3: Update order status")
        print("4: Update order details")
        print("5: Delete order")
        
        user_input = input("Choose an option from 0 - 5: ")
        
        try:
            user_input = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if user_input == 0:
            print("Returning to main menu.")
            break
        elif user_input == 1:
            view_orders()
        elif user_input == 2:
            create_order()
        elif user_input == 3:
            update_order_status()
        elif user_input == 4:
            update_order_details()
        elif user_input == 5:
            delete_order()
        else:
            print("Invalid option. Please choose a valid menu option.")

def view_orders():
    print(orders)

def create_order():
    customer_name = input("Enter customer name: ")
    customer_address = input("Enter customer address: ")
    customer_phone = input("Enter customer phone number: ")
    
    print("\nProducts list:")
    for index, product in enumerate(products):
        print(f"{index}: {product}")
    items = input("Enter product index values (comma-separated): ")
    
    print("\nCouriers list:")
    for index, courier in enumerate(couriers):
        print(f"{index}: {courier}")
    courier_index = input("Enter courier index: ")
    
    new_order = {
        "customer_name": customer_name,
        "customer_address": customer_address,
        "customer_phone": customer_phone,
        "courier": courier_index,
        "status": "preparing",
        "items": items
    }
    orders.append(new_order)
    save_orders(orders)
    print(f"Order for '{customer_name}' added.")

def update_order_status():
    print("\nOrder list:")
    for index, order in enumerate(orders):
        print(f"{index}: {order}")
    try:
        order_index = int(input("Enter the index of the order to update status: "))
        if 0 <= order_index < len(orders):
            print("\nOrder status options:")
            print("0: PREPARING")
            print("1: SHIPPED")
            print("2: DELIVERED")
            status_index = input("Enter new status index: ")
            status_list = ["PREPARING", "SHIPPED", "DELIVERED"]
            if status_index in ["0", "1", "2"]:
                orders[order_index]["status"] = status_list[int(status_index)]
                print(f"Order at index {order_index} status updated to {status_list[int(status_index)]}.")
                save_orders(orders)
            else:
                print("Invalid status index.")
        else:
            print("Invalid order index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def update_order_details():
    print("\nOrder list:")
    for index, order in enumerate(orders):
        print(f"{index}: {order}")
    try:
        order_index = int(input("Enter the index of the order to update: "))
        if 0 <= order_index < len(orders):
            order = orders[order_index]
            for key in order:
                if key != "status":
                    new_value = input(f"Enter new value for {key} (leave blank to keep current value): ")
                    if new_value:
                        order[key] = new_value
            print(f"Order at index {order_index} updated.")
            save_orders(orders)
        else:
            print("Invalid order index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_order():
    print("\nOrder list:")
    for index, order in enumerate(orders):
        print(f"{index}: {order}")
    try:
        order_index = int(input("Enter the index of the order to delete: "))
        if 0 <= order_index < len(orders):
            deleted_order = orders.pop(order_index)
            save_orders(orders)
            print(f"Order '{deleted_order}' deleted.")
        else:
            print("Invalid order index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Initialize data from CSV files
products = load_products()
couriers = load_couriers()
orders = load_orders()

# Run the main menu
main_menu()
            

