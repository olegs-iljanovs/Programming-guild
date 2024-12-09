#V.Krjukovs

import unittest
from io import StringIO
from unittest.mock import patch

UNIT_TESTS = 0
ADD_ID = 1
UPDATE_ID = 2
DELETE_ID = 3

ACTIONS_LIST = list(range(0, 4))
PRODUCTS_LIST = [
    {"id": 1, "name": "Apples", "quantity": 50},
    {"id": 2, "name": "Bananas", "quantity": 30},
    {"id": 3, "name": "Oranges", "quantity": 20},
    {"id": 4, "name": "Grapes", "quantity": 40},
    {"id": 5, "name": "Mangoes", "quantity": 25}
]

def integer_validation(obj):
    try:
        obj = int(obj)
        return int(obj)
    except:
        print("!ERROR: Please enter a valid number\n")
        return None

def print_cart(PRODUCTS_LIST):
    print("Now this is your cart:\n")
    for position, product in enumerate(PRODUCTS_LIST): print(str(position+1)+'. id: '+str(product['id'])+", name: "+product['name']+", quantity: "+str(product['quantity']))

class Product:
    def __init__(self, name, prod_id, quantity):
        self.name = name
        self.prod_id = prod_id
        self.quantity = quantity

def menu():

    while True:
        action = input('Please select the action to do:\n0. Perfom Unit tests\n1. Add new product\n2. Update product\n3. Delete product\nOr Enter to exit\n')
        ACTIONS_FUNCS_MAPPING = {UNIT_TESTS : perform_unit_tests,
                                ADD_ID : add_product,
                                UPDATE_ID : update_product,
                                DELETE_ID : delete_product}
        #exit     
        if action == "":
            break

        action = integer_validation(action)
        if action in ACTIONS_LIST:
            
            #action selecting
            ACTIONS_FUNCS_MAPPING[action]()

        #error in action input
        else:
            print("!ERROR: Please select only provided options\n")
        continue
def add_product():
    name = input('Adding Product...\nPlease enter new product name:\n')
    prod_id = input('Please enter new id:\n')
    quantity = input('Please enter new quantity:\n')
    new_product = Product(name, prod_id, quantity)
    
    prod_id = integer_validation(new_product.prod_id)
    quantity = integer_validation(new_product.quantity)

    if prod_id and quantity:
        index = next((position for position, product in enumerate(PRODUCTS_LIST) if product["id"] == prod_id), None)
        
        if index == None:
            PRODUCTS_LIST.append({"name" : name,
                                "id" : prod_id,
                                "quantity" : quantity})
            print("The Prdocut with name: '{}', id: '{}' and quantity '{}' has been successfully created\n".format(name, prod_id, quantity))
            print_cart(PRODUCTS_LIST)
        else:
            print('!ERROR: Product with provided id is already exist, please add product with another id.\n')
def update_product():
    prod_id = integer_validation(input('Enter the id of the product to update:\n'))

    if not prod_id:
        return

    index = next((position for position, product in enumerate(PRODUCTS_LIST) if product["id"] == prod_id), None)

    if index != None:
        quantity = integer_validation(input('Product with provided id has been found\nPlease enter new quantity to update:\n'))
        if quantity != None:
            old_val = PRODUCTS_LIST[index]['quantity']
            PRODUCTS_LIST[index]['quantity'] = quantity
            print("Product with id: '{}' has been successfully updated\nPrevious value: '{}' | New value:'{}'".format(prod_id, old_val, quantity))
            print_cart(PRODUCTS_LIST)
    else:
        print('!ERROR: There is no product with provided id')

def delete_product():
    prod_id = integer_validation(input('Enter the id of the product to remove:\n'))
    index = next((position for position, product in enumerate(PRODUCTS_LIST) if product["id"] == prod_id), None)

    if index != None:
        removed_product = PRODUCTS_LIST.pop(index)
        print("Product with id: '{}', name: '{}', quantity: '{}'\n".format(removed_product["id"], removed_product["name"], removed_product["quantity"])+"has been successfully found and removed")
        print_cart(PRODUCTS_LIST)
    else:
        print('!ERROR: There is no product with provided id')

########################### UNIT TESTS
def perform_unit_tests():
    print("############## PERFORMING UNIT TESTS ########################")
    unittest.main(exit=False)

class Unit_Tests(unittest.TestCase):
    def test_integer_validation_success(self):
        self.assertEqual(integer_validation("123"), 123)

    def test_integer_validation_fail(self):
        self.assertIsNone(integer_validation("asd"))
        self.assertIsNone(integer_validation("123.321"))

    @patch('builtins.input', side_effect=["Unit Test Product", "123", "1100000"])
    def test_add_product_success(self, mock_input):
        add_product()
        self.assertEqual(len(PRODUCTS_LIST), 6)
        self.assertEqual(PRODUCTS_LIST[-1]["name"], "Unit Test Product")
        self.assertEqual(PRODUCTS_LIST[-1]["id"], 123)
        self.assertEqual(PRODUCTS_LIST[-1]["quantity"], 1100000)

    @patch('builtins.input', side_effect=["Unit Test Product", "1", "15"])
    def test_add_product_fail(self, mock_input):
        add_product()
        self.assertEqual(len(PRODUCTS_LIST), 5)

    @patch('builtins.input', side_effect=["1", "123"])
    def test_update_product_success(self, mock_input):
        update_product()
        self.assertEqual(PRODUCTS_LIST[0]["quantity"], 123)

    @patch('builtins.input', side_effect=["1","11111a"])
    def test_update_product_fail(self, mock_input):
        update_product()

        self.assertEqual(PRODUCTS_LIST[0]["quantity"], 50)

    @patch('builtins.input', side_effect=["2"])
    def test_delete_product_success(self, mock_input):
        delete_product()
        self.assertEqual(len(PRODUCTS_LIST), 4)

    @patch('builtins.input', side_effect=["123"])
    def test_delete_product_fail(self, mock_input):
        delete_product()
        self.assertEqual(len(PRODUCTS_LIST), 5)

########################### RUN MENU
menu()