import unittest
import tempfile
import os

# Import the function to be tested
from your_module import update_file

class TestUpdateFile(unittest.TestCase):

    def setUp(self):
        # Create a temporary file with sample content
        self.test_file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        self.test_file.write("192.168.25.60 192.168.140.81 192.168.203.198")
        self.test_file.close()

    def tearDown(self):
        # Remove the temporary test file
        os.remove(self.test_file.name)

    def test_update_file(self):
        # Test if the function updates the file correctly
        remove_list = ["192.168.140.81", "192.168.203.198"]
        update_file(self.test_file.name, remove_list)
        
        # Read the updated file 
        with open(self.test_file.name, "r") as file:
            updated_content = file.read()
        
        # Check if the removed elements are not present in the updated content
        self.assertNotIn("192.168.140.81", updated_content)
        self.assertNotIn("192.168.203.198", updated_content)
        
        # Check if other elements are present
        self.assertIn("192.168.25.60", updated_content)

    def test_update_file_no_remove(self):
        # Test if the function handles an empty remove_list
        update_file(self.test_file.name, [])
        
        # Read the updated file
        with open(self.test_file.name, "r") as file:
            updated_content = file.read()
        
        # Check if the content remains the same
        self.assertEqual(updated_content, "192.168.25.60 192.168.140.81 192.168.203.198")

    def test_update_file_empty_file(self):
        # Test if the function handles an empty file
        empty_file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        empty_file.close()
        update_file(empty_file.name, ["192.168.140.81"])  # Try to remove an element from an empty file

        # Read the updated file
        with open(empty_file.name, "r") as file:
            updated_content = file.read()

        # Check if the file remains empty
        self.assertEqual(updated_content, "")

if __name__ == '__main__':
    unittest.main()
