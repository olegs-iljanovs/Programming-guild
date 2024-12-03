import unittest
from unittest.mock import patch
from task2_natan import Product, Interface

class TestProduct(unittest.TestCase):
  def setUp(self):
        self.new_id = 64
        self.name = "Oleg"
        self.quan = "1"
  def test_init(self):
    self.product = Product(self.id, self.name, self.quan)
    self.assertEqual(self.product.id, self.id)
    self.assertEqual(self.product.name, self.name)
    self.assertEqual(self.product.quan, self.quan)

class TestInterface(unittest.TestCase):
    def setUp(self):
        new_id = 24
        database = [
            Product(23, "Oleg", 5),
            Product(24, "Olegoria", 52),
        ]
        self.interface = Interface(new_id, database)

    def test_init(self):
        self.assertEqual(self.interface.new_id, 24)

    @patch("builtins.input", side_effect=["OlegBuda", 10])
    def test_add_product(self, mock_input):
        self.interface.add_product()
        self.assertEqual(len(self.interface.database), 3)
        self.assertEqual(self.interface.database[-1].name, "OlegBuda")
        self.assertEqual(self.interface.database[-1].quan, 10)
    
    @patch("builtins.input", side_effect=["24", "18"])
    def test_update_product(self, mock_input):
        self.interface.update_product()
        self.assertEqual(len(self.interface.database), 2)
        self.assertEqual(self.interface.database[-1].id, 24)
        self.assertEqual(self.interface.database[-1].quan, 18)
    
    @patch("builtins.input", side_effect=["24"])
    def test_delete_product(self, mock_input):
        self.interface.delete_product()
        self.assertEqual(len(self.interface.database), 1)
        
if __name__ == "__main__":
  unittest.main()