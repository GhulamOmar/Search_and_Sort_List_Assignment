import unittest
import fun_with_collections.sort_and_search_list as basic_list_exception


class MyTestCase(unittest.TestCase):
    def test_make_list(self):
        self.assertTrue(basic_list_exception.sort_list([5, 3, 6, 8,9,10, 4]))
        basic_list_exception.search_list([3])


if __name__ == '__main__':
    unittest.main()
