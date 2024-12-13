import unittest
from unittest.mock import patch
from vn_task2 import Inventory

class Test(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        self.inventory.inventory = [{"ID": 1, "Name": "Apple", "Quantity": 4}]

    #adding item with unique ID
    @patch('builtins.input', side_effect = [2, 'Qiwi', 4])
    def test_add_item_success(self, mock_input):
        self.inventory.add_item()
        self.assertEqual(len(self.inventory.inventory), 2)
        self.assertIn({"ID": 2, "Name": 'Qiwi', "Quantity": 4}, self.inventory.inventory)
    
    #adding item with duplicate ID
    @patch('builtins.input', side_effect = [1, 'Pinepple', 4])
    def test_add_item_failed(self, mock_input):
        self.inventory.add_item()
        self.assertEqual(len(self.inventory.inventory), 1)
        self.assertNotIn({"ID": 1, "Name": "Pinepple", "Quantity": '4'}, self.inventory.inventory)
    
    #removing item by existing id
    @patch('builtins.input', return_value=1)
    def test_remove_item_success(self, mock_input):
        self.inventory.remove_item_by_id()
        self.assertEqual(len(self.inventory.inventory), 0)

    #removing item by not existing id
    @patch('builtins.input', return_value=1337)
    def test_remove_item_failed(self, mock_input):
        self.inventory.remove_item_by_id()
        self.assertEqual(len(self.inventory.inventory), 1)
    
    #updating item by existing id
    @patch('builtins.input', side_effect = [1, 3])
    def test_update_item_success(self, mock_input):
        self.inventory.update_item()
        self.assertIn({"ID": 1, "Name": "Apple", "Quantity": 3}, self.inventory.inventory)
    
    #updating item by not existing id
    @patch('builtins.input', return_value=1337)
    def test_update_item_failed(self, mock_input):
        self.inventory.update_item()
        self.assertIn({"ID": 1, "Name": "Apple", "Quantity": 4}, self.inventory.inventory)

if __name__ == '__main__':
    unittest.main()
