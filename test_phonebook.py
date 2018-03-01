import unittest

from phonebook import Phonebook

book = Phonebook() 

class PhonebookTestCase(unittest.TestCase):
    """Test case for the phonebook app"""
    def setUp(self):
        self.name = "steve"
        self.number = "0712762717"

    def test_add(self):
        """Test user can add a new contact"""
        result = book.add(self.name, self.number)
        self.assertEqual(result, "contact added successfully")

    def test_delete(self):
        result = book.delete(self.name)
        self.assertEqual(result, "contact deleted successfully")

    def test_update(self):
        self.old_name = "Jane"
        self.old_number = "0722222222"
        self.new_name = "Mary"
        self.new_number = "0723876543"
        res = book.add(self.old_name, self.old_number)
        self.assertEqual(res, "contact added successfully")

        result = book.update(self.old_name, self.new_name, self.old_number, self.new_number)
        self.assertEqual(result, "contact updated successfully")

if __name__ == '__main__':
    unittest.main()