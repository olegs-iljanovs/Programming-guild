import unittest
from inventory_management import Inventory


class InventoryTest(unittest.TestCase):
    def setUp(self):
        self.products = [
            {"id": 1, "name": "Apples", "quantity": 50},
            {"id": 2, "name": "Bananas", "quantity": 30},
            {"id": 3, "name": "Oranges", "quantity": 20},
        ]
        self.inventory = Inventory(initial_products=self.products)

    # add product test
    def test_add_product(self):
        self.inventory.add_products(4, "Grapes", 40)
        self.assertEqual(len(self.inventory.products), 4)
        self.assertIn({"id": 4, "name": "Grapes", "quantity": 40}, self.inventory.products)

    # test for duplicate ID
    def test_add_duplicate_product(self):
        self.inventory.add_products(2, "Pineapple", 40)  
        self.assertEqual(len(self.inventory.products), 3) 

    # update stock test
    def test_update_stock(self):
        self.inventory.update_stock(1, 50) 
        product = next((p for p in self.inventory.products if p["id"] == 1), None)
        self.assertIsNotNone(product)
        self.assertEqual(product["quantity"], 100)  

     # remove products   
    def test_remove_product(self):
        self.inventory.remove_products(3)  # 
        self.assertEqual(len(self.inventory.products), 2)
        self.assertNotIn({"id": 3, "name": "Oranges", "quantity": 20}, self.inventory.products)

    # invalid product
    def test_remove_invalid_product(self):
        self.inventory.remove_products(10)  
        self.assertEqual(len(self.inventory.products), 3)


if __name__ == "__main__":
    unittest.main()
