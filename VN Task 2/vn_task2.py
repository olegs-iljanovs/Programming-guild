### SIMPLE INVENTORY MANAGEMENT
#importing tabulate to print pretty inventory
from tabulate import tabulate

class Inventory:
    def __init__(self):
        self.inventory = []

    '''method to validate only integer user input'''
    def validate_input(self, input_message):
        input_num = None
        while True:
            input_num = input(input_message)
            try:
                input_num = int(input_num)
                if input_num <= 0:
                    raise ValueError
            except ValueError:
                print("You must enter a positive integer number.")
                continue
            return input_num

    '''method to add items to inventory and check if ID of new item is unique'''
    def add_item(self):
        item_id = self.validate_input("Enter ID for item that you want to add: ")

        if next((item for item in self.inventory if item["ID"] == item_id), None):
            print("Item already on  inventory")
            return
        
        item_name = input("Enter name for item that you want to add: ")
        item_quantity = self.validate_input("Enter quantity of items that you want to add: ")

        self.inventory.append({"ID": item_id, "Name": item_name, "Quantity": item_quantity})
        print("Item successfully added.")

    '''method to update item quantity by id'''
    def update_item(self):
        item_id = self.validate_input("Enter ID of item that you want to update: ")
        item_quantity = self.validate_input("Enter new quantity value: ")

        item_index = next((i for i, item in enumerate(self.inventory) if item["ID"] == item_id), None)

        if item_index is not None:
            self.inventory[item_index]["Quantity"] = item_quantity
        else:
            print("Item not found in inventory.")
        print("Item successfully updated.")

    '''method to remove item from inventory by id'''
    def remove_item_by_id(self):
        item_id = self.validate_input("Enter ID of item that you want to remove: ")
        
        item_index = next((i for i, item in enumerate(self.inventory) if item["ID"] == item_id), None)

        if item_index is not None or item_index == 0:
            del self.inventory[item_index]
        else:
            print("Item not found in inventory.")
        print("Item successfully removed.")

    '''shows inventory'''
    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print(tabulate(self.inventory, headers='keys'))

    '''main app menu'''
    def main_menu(self):
        while True:
            user_input = input(
                """It's yours inventory manager, you can: 
                    1. Add Item
                    2. Update Item
                    3. Remove Item by ID
                    4. Show Inventory
                    5. Exit\n"""
            )
            menu_options = {
                "1": self.add_item,
                "2": self.update_item,
                "3": self.remove_item_by_id,
                "4": self.show_inventory,
            }

            if user_input == "5":
                break
            elif user_input in menu_options:
                menu_options[user_input]()
            else:
                print("No such menu option.")

inventory = Inventory()
inventory.main_menu()
