from tabulate import tabulate
import json

# Session storage creation
def save_session(database):
    with open("session.json", 'w') as f:
        json.dump([product.__dict__ for product in database], f)

def load_session():
    try:
        with open("session.json", 'r') as f:
            data = json.load(f)
            # Convert dictionaries back to Product objects
            return [Product(**item) for item in data]
    except Exception as e:
        print("File was not found. Details: ", e)
        return []

class Product:

    def __init__(self, product_id, name, quantity):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity

class Interface:

    def __init__(self, new_product_id, database):
        self.new_product_id = new_product_id
        self.database = database

    def add_product(self):
        self.new_product_id += 1
        name = str(input("Enter the name of the product."))
        quantity = int(input("Enter the quantitytity of the product."))
        new_product = Product(self.new_product_id, name, quantity)
        self.database.append(new_product)
        self.show_products()

    def update_product(self):
        product_id = int(input("Enter the product_id of the product."))
        quantity = int(input("Enter the quantitytity of the product."))
        current_product = next(iter([obj for obj in self.database if getattr(obj, "product_id") == product_id]), None)
        if current_product:
            current_product.quantity = quantity
        else:
            print("Product was not found")
        self.show_products()

    def delete_product(self):
        product_id = int(input("Enter the product_id of the product."))
        current_product = next(iter([obj for obj in self.database if getattr(obj, "product_id") == product_id]), None)
        if current_product:
            self.database.remove(current_product)
        else:
            print("Product was not found")
        self.show_products()

    def show_products(self):

        headers = ["product_id", "Name", "quantitytity"]
        data = [[product.product_id, product.name, product.quantity] for product in self.database]
        if data:
            print(tabulate(data, headers=headers, tablefmt="grid"))
        else:
            print("Database is empty.")
if __name__ == "__main__":
    database = load_session()

    product_ids = [obj.product_id for obj in database]

    if product_ids:
        new_product_id = max(product_ids)
    else:
        new_product_id = 0

    interface = Interface(new_product_id, database)

    is_repeat = 1

    while is_repeat == 1:
        try:
            operations = {0:interface.show_products, 1: interface.add_product,
                          2: interface.update_product, 3: interface.delete_product}
            
            print("Hello, this is company interactions with products interface.")
            operation = int(input("Press: 0) Show Product; 1) Add Product; 2) Update Product; 3) Delete Product; "))
            
            operation = operations.get(operation)

            if operation:
                operation()
            else:
                print("Invalid input.")

        except Exception as e:
            print("Invalid input. Details: ", e)
        
        try:
            is_repeat = int(input("Would you like to continue? Press '1' to continue: "))
        except ValueError as v:
            print("Invalid input. Details: ", v)
            break
        
    save_session(interface.database)