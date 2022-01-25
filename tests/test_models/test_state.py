#!/usr/bin/python3
"""Test State Class """

from models.state import State
import datetime
import unittest


class TestUser(unittest.TestCase):
    """ Test State Class """
    my_object = State()
    my_class = State.__dict__

    def test_checking_for_docstring_User(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(State.__doc__)

    def test_subclass_instance_User(self):
        """Test if my_object is a subclass of BaseModel"""
        self.assertTrue(isinstance(self.my_object, State))

    def test_attribute(self):
        """ Test attributes """
        self.assertEqual(hasattr(self.my_object, "name"), True)

    def test_attribute_type(self):
       t_format = "%Y-%m-%dT%H:%M:%S.%f"
       my_dict = self.my_object.to_dict()
       self.assertEqual(self.my_object.__class__.__name__, 'State')
       self.assertEqual(type(my_dict['created_at']), str)
       self.assertEqual(type(my_dict['updated_at']), str)
       self.assertEqual(my_dict["created_at"],
                        self.my_object.created_at.strftime(t_format))
       self.assertEqual(my_dict["updated_at"],
                        self.my_object.updated_at.strftime(t_format))
       self.assertEqual(type(self.my_class['name']), str)


if __name__ == '__main__':
    unittest.main()
