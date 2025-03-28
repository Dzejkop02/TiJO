import unittest
from script1 import find_repeated_elements


class TestFindRepeatedElements(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(find_repeated_elements([1, 1, 3, 2, 2, 2, 4, 5], 2), [1])

    def test_example_2(self):
        self.assertEqual(find_repeated_elements([1, 1, 2, 2, 2, 3, 4, 5], 3), [2])

    def test_example_3(self):
        self.assertEqual(find_repeated_elements([1, 2, 2, 2, 3, 4, 5, 5, 1], 2), [1, 5])

    def test_list_none(self):
        self.assertEqual(find_repeated_elements(None, 2), [])

    def test_lottery_none(self):
        self.assertEqual(find_repeated_elements([1, 2, 3], None), [])

    def test_both_none(self):
        self.assertEqual(find_repeated_elements(None, None), [])

    def test_no_match(self):
        self.assertEqual(find_repeated_elements([1, 1, 2, 2, 3, 4, 5], 7), [])


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
