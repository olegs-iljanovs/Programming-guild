from os import system
from Inventory import Inventory

if __name__ == "__main__":
    #item = Product()
    inventory = Inventory()
    while True:
        #system("cls")
        print("1) View inventory")
        print("2) Add item to inventory")
        print("3) Update item")
        print("4) Delete item")
        print("5) Exit")

        x = int(input())
        if x == 1:
            inventory.print_table()
        elif x == 2:
            data = input("Please input data like: id, name, quantity\n")
            inventory.add_item()
        elif x == 3:
            inventory.update_item()
        elif x == 4:
            inventory.delete_item()
        elif x == 5:
            break
    