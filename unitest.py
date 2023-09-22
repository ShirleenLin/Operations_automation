#!/usr/bin/env python3
import unittest
from emails import find_email

class EmailsTest(unittest.TestCase):
    # Test for basic functionality
    def test_basic(self):
        # Test case: Provide a valid name, expect a valid email address
        testcase = [None, "Bree", "Campbell"]
        expected = "breee@abc.edu"
        self.assertEqual(find_email(testcase), expected)

    # Test for handling missing parameters
    def test_one_name(self):
        # Test case: Provide only one name (missing last name), expect "Missing parameters"
        testcase = [None, "John"]
        expected = "Missing parameters"
        self.assertEqual(find_email(testcase), expected)
    #
    # # Test for handling names not found in the dataset
    def test_two_name(self):
        # Test case: Provide a name not present in the dataset, expect "No email address found"
        testcase = [None, "Roy", "Cooper"]
        expected = "No email address found"
        self.assertEqual(find_email(testcase), expected)



if __name__ == '__main__':
    unittest.main()
