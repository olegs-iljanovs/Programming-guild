class Inventory:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        self.inventory.append({"id": item.id, "name": item.name, "quantity": item.quantity})

    def update_item(self):
        pass

    def delete_item(self):
        pass

    def print_table(self):
        print(self.inventory)
