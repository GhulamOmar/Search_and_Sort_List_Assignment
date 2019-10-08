import unittest
# from unittest.mock import patch
import fun_with_collections.sort_and_search_list as basic_list_exception


class MyTestCase(unittest.TestCase):
    def test_make_list(self):
        self.assertTrue(basic_list_exception.sort_list([6, 3, 9, 7]))
        basic_list_exception.search_list([3, 5, 7, 9])


if __name__ == '__main__':
    unittest.main()
