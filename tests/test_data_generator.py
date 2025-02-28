import unittest
from search import data_generator, constants


class TestDataGenerator(unittest.TestCase):
    def test_random_list_size(self):
        size = 100
        result = data_generator.get_random_sorted_list(size)
        self.assertEqual(len(result), size)

    def test_random_list_range(self):
        size = 100
        result = data_generator.get_random_sorted_list(size)
        self.assertTrue(all(0 <= x <= constants.MAX_VALUE for x in result))

    def test_sorted(self):
        size = 100
        result = data_generator.get_random_sorted_list(size)
        self.assertEqual(result, sorted(result))