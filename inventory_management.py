class Inventory():
    def __init__(self, initial_products=None):
        self.products = initial_products if initial_products else []
 
    def add_products(self, product_id, product_name, product_quantity):

        product_exists = False
        for product in self.products:
            if product.get("id") == product_id:
                product_exists = True
                break

        if product_exists:
            print("Product with ID {} already exists".format(product_id))
        
        else:
            self.products.append({"id": product_id, "name": product_name, "quantity": product_quantity})
            print("{} {} added".format(product_quantity, product_name))

    def update_stock(self, product_id, product_quantity):
        for product in self.products:
            if product.get("id") == product_id:
                product["quantity"] += product_quantity
                print("Stock for product with ID {} is updated. Quantity is now {}".format(product_id, product_quantity))
                return 
        print("Cannot update stock. Product is not found.")

    def remove_products(self, product_id):
        for product in self.products:
            if product.get("id") == product_id:
                self.products.remove(product)
                print("Product with ID {} removed".format(product_id))
                return
        print("Error: Product with ID {} not found.".format(product_id))

    def display_inventory(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            print("{:<10}{:<20}{:<10}".format("ID", "Name", "Quantity"))
            print("-" * 40)
            for product in self.products:
                # Display each product in a tabular format.
                print("{:<10}{:<20}{:<10}".format(product["id"], product["name"], product["quantity"]))
            print("-" * 40)


products = [{"id": 1, "name": "Apples", "quantity": 50},
            {"id": 2, "name": "Bananas", "quantity": 30},
            {"id": 3, "name": "Oranges", "quantity": 20},
            {"id": 4, "name": "Grapes", "quantity": 40}, 
            {"id": 5, "name": "Mangoes", "quantity": 25}]

inventory = Inventory(initial_products=products)

# add products
inventory.add_products(6, "Lemon", 10)
inventory.add_products(7, "Strawberry", 20)

# add duplicate product
inventory.add_products(2, "Pineapple", 40)

# update stock
inventory.update_stock(1, 500)
inventory.update_stock(4, 200)
# update using invalid ID
inventory.update_stock(9, 100) 

# remove products
inventory.remove_products(3)
# remove using invalid ID
inventory.remove_products(10)  # invalid ID

# display inventory
inventory.display_inventory()