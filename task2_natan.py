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
    id = 0
    name = ''
    quan = 0
    def __init__(self, id, name, quan):
        self.id = id
        self.name = name
        self.quan = quan

class Interface:

    new_id = 0
    database = []

    def __init__(self, new_id, database):
        self.new_id = new_id
        self.database = database

    def add_product(self):
        self.new_id += 1
        name = str(input("Enter the name of the product."))
        quan = int(input("Enter the quantity of the product."))
        new_product = Product(self.new_id, name, quan)
        self.database.append(new_product)
        self.show_products()

    def update_product(self):
        id = int(input("Enter the id of the product."))
        quan = int(input("Enter the quantity of the product."))
        current_product = next(iter([obj for obj in self.database if getattr(obj, "id") == id]), None)
        if current_product:
            current_product.quan = quan
        else:
            print("Product was not found")
        self.show_products()

    def delete_product(self):
        id = int(input("Enter the id of the product."))
        current_product = next(iter([obj for obj in self.database if getattr(obj, "id") == id]), None)
        if current_product:
            self.database.remove(current_product)
        else:
            print("Product was not found")
        self.show_products()

    def show_products(self):

        headers = ["ID", "Name", "Quantity"]
        data = [[product.id, product.name, product.quan] for product in self.database]
        if data:
            print(tabulate(data, headers=headers, tablefmt="grid"))
        else:
            print("Database is empty.")

database = load_session()

product_ids = [obj.id for obj in database]

if product_ids:
    new_id = max(product_ids)
else:
    new_id = 0

interface = Interface(new_id, database)

flag = 1

while flag == 1:
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
        flag = int(input("Would you like to continue? Press '1' to continue: "))
    except:
        break
    
save_session(interface.database)