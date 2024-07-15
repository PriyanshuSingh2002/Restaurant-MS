class MenuItem:
    def __init__(self, item_id, name, category, price, availability):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.price = price
        self.availability = availability
    def display(self):
        availability_status = 'Available' if self.availability else 'Not Available'
        print(f"ID: {self.item_id}, Name: {self.name}, Category: {self.category}, Price: ${self.price}, Availability: {availability_status}")

class Customer:
    def __init__(self, customer_id, name, contact_number, email):
        self.customer_id = customer_id
        self.name = name
        self.contact_number = contact_number
        self.email = email
    def display(self):
        print(f"ID: {self.customer_id}, Name: {self.name}, Contact Number: {self.contact_number}, Email: {self.email}")

class Order:
    def __init__(self, order_id, customer_id, item_id, order_date, quantity):
        self.order_id = order_id
        self.customer_id = customer_id
        self.item_id = item_id
        self.order_date = order_date
        self.quantity = quantity
    def display(self):
        print(f"Order ID: {self.order_id}, Customer ID: {self.customer_id}, Item ID: {self.item_id}, Order Date: {self.order_date}, Quantity: {self.quantity}")

class MenuManager:
    def __init__(self):
        self.menu_items = {}
    def add_menu_item(self, item):
        if item.item_id in self.menu_items:
            raise Exception("Item ID already exists.")
        self.menu_items[item.item_id] = item
    def update_menu_item(self, item):
        if item.item_id not in self.menu_items:
            raise Exception("Item ID not found.")
        self.menu_items[item.item_id] = item
    def delete_menu_item(self, item_id):
        if item_id not in self.menu_items:
            raise Exception("Item ID not found.")
        del self.menu_items[item_id]
    def display_menu(self):
        for item in self.menu_items.values():
            item.display()

class CustomerManager:
    def __init__(self):
        self.customers = {}
    def add_customer(self, customer):
        if customer.customer_id in self.customers:
            raise Exception("Customer ID already exists.")
        self.customers[customer.customer_id] = customer
    def update_customer(self, customer):
        if customer.customer_id not in self.customers:
            raise Exception("Customer ID not found.")
        self.customers[customer.customer_id] = customer
    def delete_customer(self, customer_id):
        if customer_id not in self.customers:
            raise Exception("Customer ID not found.")
        del self.customers[customer_id]
    def display_customers(self):
        for customer in self.customers.values():
            customer.display()

class OrderManager:
    def __init__(self):
        self.orders = {}
    def add_order(self, order):
        if order.order_id in self.orders:
            raise Exception("Order ID already exists.")
        self.orders[order.order_id] = order
    def update_order(self, order):
        if order.order_id not in self.orders:
            raise Exception("Order ID not found.")
        self.orders[order.order_id] = order
    def cancel_order(self, order_id):
        if order_id not in self.orders:
            raise Exception("Order ID not found.")
        del self.orders[order_id]
    def display_orders(self):
        for order in self.orders.values():
            order.display()

def main(): #Console Application Manager
    menu_manager = MenuManager()
    customer_manager = CustomerManager()
    order_manager = OrderManager()
    while True:
        print("\nRestaurant Management System")
        print("1. Manage Menu")
        print("2. Manage Customers")
        print("3. Manage Orders")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            print("\nMenu Management")
            print("1. Add Menu Item")
            print("2. Update Menu Item")
            print("3. Delete Menu Item")
            print("4. Display Menu")

            menu_choice = input("Enter your choice: ")

            if menu_choice == '1':
                item_id = input("Enter item ID: ")
                name = input("Enter item name: ")
                category = input("Enter item category: ")
                price = float(input("Enter item price: "))
                availability = input("Is the item available (yes/no): ").lower() == 'yes'
                menu_manager.add_menu_item(MenuItem(item_id, name, category, price, availability))
            elif menu_choice == '2':
                item_id = input("Enter item ID: ")
                name = input("Enter item name: ")
                category = input("Enter item category: ")
                price = float(input("Enter item price: "))
                availability = input("Is the item available (yes/no): ").lower() == 'yes'
                menu_manager.update_menu_item(MenuItem(item_id, name, category, price, availability))
            elif menu_choice == '3':
                item_id = input("Enter item ID: ")
                menu_manager.delete_menu_item(item_id)
            elif menu_choice == '4':
                menu_manager.display_menu()

        elif choice == '2':
            print("\nCustomer Management")
            print("1. Add Customer")
            print("2. Update Customer")
            print("3. Delete Customer")
            print("4. Display Customers")

            customer_choice = input("Enter your choice: ")

            if customer_choice == '1':
                customer_id = input("Enter customer ID: ")
                name = input("Enter customer name: ")
                contact_number = input("Enter contact number: ")
                email = input("Enter email: ")
                customer_manager.add_customer(Customer(customer_id, name, contact_number, email))
            elif customer_choice == '2':
                customer_id = input("Enter customer ID: ")
                name = input("Enter customer name: ")
                contact_number = input("Enter contact number: ")
                email = input("Enter email: ")
                customer_manager.update_customer(Customer(customer_id, name, contact_number, email))
            elif customer_choice == '3':
                customer_id = input("Enter customer ID: ")
                customer_manager.delete_customer(customer_id)
            elif customer_choice == '4':
                customer_manager.display_customers()

        elif choice == '3':
            print("\nOrder Management")
            print("1. Add Order")
            print("2. Update Order")
            print("3. Cancel Order")
            print("4. Display Orders")

            order_choice = input("Enter your choice: ")

            if order_choice == '1':
                order_id = input("Enter order ID: ")
                customer_id = input("Enter customer ID: ")
                item_id = input("Enter item ID: ")
                order_date = input("Enter order date: ")
                quantity = int(input("Enter quantity: "))
                order_manager.add_order(Order(order_id, customer_id, item_id, order_date, quantity))
            elif order_choice == '2':
                order_id = input("Enter order ID: ")
                customer_id = input("Enter customer ID: ")
                item_id = input("Enter item ID: ")
                order_date = input("Enter order date: ")
                quantity = int(input("Enter quantity: "))
                order_manager.update_order(Order(order_id, customer_id, item_id, order_date, quantity))
            elif order_choice == '3':
                order_id = input("Enter order ID: ")
                order_manager.cancel_order(order_id)
            elif order_choice == '4':
                order_manager.display_orders()

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



