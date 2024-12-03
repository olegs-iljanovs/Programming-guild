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

def addProduct():
    id = int(input("Enter the id of the product."))
    name = str(input("Enter the name of the product."))
    quan = int(input("Enter the quantity of the product."))
    new_product = Product(id, name, quan)
    database.append(new_product)
    showProducts(database)

def updateProduct():
    id = int(input("Enter the id of the product."))
    quan = int(input("Enter the quantity of the product."))
    current_product = next(iter([obj for obj in database if getattr(obj, "id") == id]), None)
    if current_product:
        current_product.quan = quan
    else:
        print("Product was not found")
    showProducts(database)

def deleteProduct():
    id = int(input("Enter the id of the product."))
    current_product = next(iter([obj for obj in database if getattr(obj, "id") == id]), None)
    if current_product:
        database.remove(current_product)
    else:
        print("Product was not found")
    showProducts(database)

def showProducts(database):
    headers = ["ID", "Name", "Quantity"]
    data = [[product.id, product.name, product.quan] for product in database]
    if data:
        print(tabulate(data, headers=headers, tablefmt="grid"))
    else:
        print("Database is empty.")

database = load_session()
ans = 1

while ans==1:
    try:
        x = int(input("Hello, this is company interactions with products interface. Press: 0) Show Product; 1) Add Product; 2) Update Product; 3) Delete Product; "))
        if x==0:
            showProducts(database)
        elif x==1:
            addProduct()
        elif x==2:
            updateProduct()
        elif x==3:
            deleteProduct()
        else:
            print("Good job, Oleg. You entered an incorrect value.")
    except Exception as e:
        print("Invalid input. Details: ", e)
    
    try:
        ans = int(input("Would you like to continue? Press '1' to continue: "))
    except:
        break
    
save_session(database)